import os
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from models import paymentModel, subscriptionPricingModel, userProfileModel
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.userPayload import userPayload
from schemas.paymentSchema import paymentSchema
import stripe
from datetime import datetime, timedelta

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_ENDPOINT_SECRET_KEY")

router = APIRouter(
    prefix='/payments/stripe',
    tags=['Stripe Payments']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/create_payment_intent", status_code=status.HTTP_201_CREATED)
async def create_payment_intent(db: db_dependency, payment_data: paymentSchema,
                                user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')

        subscription_model = db.query(subscriptionPricingModel).filter(
            subscriptionPricingModel.id == payment_data.id).filter(
            subscriptionPricingModel.isDeleted == False).first()
        if subscription_model is None:
            raise HTTPException(status_code=404, detail='Subscription Pricing not found.')

        payment_intent = stripe.PaymentIntent.create(
            amount=int(
                (subscription_model.price - ((subscription_model.price * subscription_model.discount) / 100)) * 100),
            currency=subscription_model.currencyCode,
            description=subscription_model.description
        )

        payment_model = paymentModel(
            userId=user.id,
            subscription_id=payment_data.id,
            totalAmount=float(payment_intent.amount/100),
            days_valid=subscription_model.duration,
            paymentIntentId=payment_intent.id
        )

        db.add(payment_model)
        db.commit()

    except stripe.error.CardError as e:
        # Handle specific card errors
        raise HTTPException(status_code=401, detail=e)
    except stripe.error.StripeError as e:
        # Handle generic Stripe errors
        raise HTTPException(status_code=401, detail=e)
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post('/webhook', status_code=status.HTTP_200_OK)
async def webhook(db: db_dependency, request: Request):

    # Get the raw request body as bytes
    data = await request.body()
    # Get the Stripe signature header
    signature = request.headers.get("stripe-signature")

    try:
        # Verify the webhook signature and construct the event
        event = stripe.Webhook.construct_event(
            payload=data, sig_header=signature, secret=webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        raise HTTPException(status_code=400, detail=str(e))
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise HTTPException(status_code=400, detail=str(e))

    # Handle the event
    # You can access the event type and data as event.type and event.data
    # For example, if the event is a payment_intent.succeeded, you can get the payment intent id as event.data.object.id
    # You can also perform different actions based on the event type
    # For example, you can send an email confirmation, update your database, etc.
    # For a list of possible event types, see https://stripe.com/docs/api/events/types

    intent = event['data']['object']
    intent = str(intent.id)
    intent_Type = "Pending"
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        intent_Type = "Payment Received"
        print("PaymentIntent was successful:", payment_intent.id)
    if event['type'] == 'payment_intent.created':
        payment_created = event['data']['object']
        intent_Type = "Payment Received"  # Needs to change
        print("PaymentIntent was created:", payment_created.id)
    elif event['type'] == 'payment_intent.payment_failed':
        payment_failed = event['data']['object']
        intent_Type = "Payment Failed"
        print("PaymentIntent was Failed:", payment_failed.id)
    elif event['type'] == 'subscription_schedule.canceled':
        subscription_schedule = event['data']['object']
        print("subscription_schedule was cancelled:", subscription_schedule.id)
    elif event['type'] == 'invoice.upcoming':
        invoice = event['data']['object']
        print("Invoice Upcoming:", invoice.id)
    elif event.type == "invoice.payment_succeeded":
        invoice = event['data']['object']
        print("Invoice Payment Success:", invoice.id)
    # ... handle other event types
    else:
        print("Unhandled event type:", event.type)

    payment_model = db.query(paymentModel).filter(
        paymentModel.paymentIntentId == intent).first()

    if payment_model is None:
        raise HTTPException(status_code=404, detail='Payment Intent not found.')

    payment_model.status = intent_Type
    payment_model.updatedAt = datetime.now()

    user_id = payment_model.userId
    days_valid = payment_model.days_valid

    db.add(payment_model)
    db.commit()

    now = datetime.now()

    if intent_Type == "Payment Received":
        user_model = db.query(userProfileModel).filter(
            userProfileModel.userId == user_id).first()
        if user_model is None:
            raise HTTPException(status_code=404, detail='User Not Found')

        date = str(now).split(" ")
        date_split = datetime.strptime(date[0], "%Y-%m-%d")
        modified_date = date_split + timedelta(days=days_valid)
        modified_date = str(modified_date).split(" ")
        validity = str((modified_date[0]) + " " + str(date[1]))

        user_model.expDate = validity
        user_model.updatedAt = datetime.now()

        db.add(payment_model)
        db.commit()

    # Return a success response
    return {"status": "success"}
