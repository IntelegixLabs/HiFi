import os
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from models import paymentModel, subscriptionPricingModel
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.userPayload import userPayload
from schemas.paymentSchema import paymentSchema
import stripe

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
            PaymentIntentId=payment_intent.id
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
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        print("PaymentIntent was successful:", payment_intent.id)
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

    # Return a success response
    return {"status": "success"}
