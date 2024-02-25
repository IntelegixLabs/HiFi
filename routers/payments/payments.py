import os

import stripe
from dotenv import load_dotenv
from fastapi import Request, APIRouter

load_dotenv()
# Replace with your Stripe secret key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "localhost")
router = APIRouter(
    prefix='/payments',
    tags=['payments']
)


@router.post('/create-checkout-session')
async def create_checkout_session(request: Request):
    try:
        data = await request.json()

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': data.get("price_id"),
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url="http://localhost:5000/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="http://localhost:5000/cancel",
        )
        return {"session_id": checkout_session["id"]}
    except stripe.error.CardError as e:
        # Handle specific Stripe errors
        return {"status": "error", "message": str(e)}
    except stripe.error.StripeError as e:
        # Handle generic Stripe errors
        return {"status": "error", "message": "Something went wrong. Please try again later."}
    except Exception as e:
        print(e)
        return "Server error", 500
