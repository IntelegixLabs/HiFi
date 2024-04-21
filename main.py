import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config.database import engine
from models import Base
from routers import userProfile
from routers.users import userAdditionalData
from routers.auth import get_user_info
from schemas import userPayload

from routers.codes import get_codes
from routers.stocks import core_stocks, fundamental_data
from routers.forex import forex
from routers.cryptocurrencies import crypto
from routers.commodities import commodities
from routers.economic_indicators import economic_indicators
from routers.news_insights import news_insights
from routers.technical_indicators import technical_indicators
from routers.admin import pricing
from routers import ekyc
from routers.payments import stripe
from routers.generative_ai import generative_ai


load_dotenv()

app = FastAPI()

# Define CORS settings
origins = ["*"]  # Allow requests from any origin

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/status/health")
def health_check():
    return {'status': 'Healthy'}


@app.get("/status/security-check")
async def root(user: userPayload = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(userProfile.router)
app.include_router(userAdditionalData.router)

app.include_router(get_codes.router)
app.include_router(core_stocks.router)
app.include_router(fundamental_data.router)
app.include_router(forex.router)
app.include_router(crypto.router)
app.include_router(commodities.router)
app.include_router(economic_indicators.router)
app.include_router(news_insights.router)
app.include_router(technical_indicators.router)
app.include_router(ekyc.router)
app.include_router(generative_ai.router)

app.include_router(pricing.router)
app.include_router(stripe.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=os.getenv("HIFI_APP_HOST", "localhost"), port=int(os.getenv("HIFI_APP_PORT", 5000)),
                reload=True)
