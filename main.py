import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from config.database import engine
from models import Base
from routers import userProfile
from routers.stocks import core_stocks, fundamental_data
from routers.forex import forex
from routers.cryptocurrencies import crypto
from routers.auth import get_user_info
from schemas import userPayload

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


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


@app.get("/secure")
async def root(user: userPayload = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


app.include_router(userProfile.router)
app.include_router(core_stocks.router)
app.include_router(fundamental_data.router)
app.include_router(forex.router)
app.include_router(crypto.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=os.getenv("HIFI_APP_HOST", "localhost"), port=int(os.getenv("HIFI_APP_PORT", 5000)),
                reload=True)
