from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from models import subscriptionPricingModel
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.subscriptionPricingSchema import subscriptionPricingSchema
from schemas.userPayload import userPayload
from datetime import datetime

router = APIRouter(
    prefix='/admin',
    tags=['Admin API For Subscription Pricing']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/pricing', status_code=status.HTTP_200_OK)
async def get_pricing(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(subscriptionPricingModel).filter(subscriptionPricingModel.isDeleted == False).all()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/pricing", status_code=status.HTTP_201_CREATED)
async def add_pricing(db: db_dependency, subscription_data: subscriptionPricingSchema,
                      user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        add_subscription_model = subscriptionPricingModel(
            name=subscription_data.name,
            price=subscription_data.price,
            currencyCode=subscription_data.currencyCode,
            discount=subscription_data.discount,
            duration=subscription_data.duration,
            description=subscription_data.description,
        )

        db.add(add_subscription_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/pricing/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_pricing(db: db_dependency, subscription_data: subscriptionPricingSchema,
                         user: userPayload = Depends(get_user_info), id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        update_subscription_model = db.query(subscriptionPricingModel).filter(subscriptionPricingModel.id == id).filter(
            subscriptionPricingModel.isDeleted == False).first()
        if update_subscription_model is None:
            raise HTTPException(status_code=404, detail='Subscription Pricing not found.')

        update_subscription_model.name = subscription_data.name
        update_subscription_model.price = subscription_data.price
        update_subscription_model.currencyCode = subscription_data.currencyCode
        update_subscription_model.discount = subscription_data.discount
        update_subscription_model.duration = subscription_data.duration
        update_subscription_model.description = subscription_data.description
        update_subscription_model.updatedAt = datetime.now()

        db.add(update_subscription_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.delete("/pricing/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pricing(db: db_dependency, user: userPayload = Depends(get_user_info), id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        subscription_model = db.query(subscriptionPricingModel).filter(subscriptionPricingModel.id == id).first()
        if subscription_model is None:
            raise HTTPException(status_code=404, detail='Subscription Pricing not found.')

        subscription_model.isDeleted = True
        subscription_model.updatedAt = datetime.now()

        db.add(subscription_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.patch("/pricing/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def reactivate_pricing(db: db_dependency, user: userPayload = Depends(get_user_info),
                             id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        subscription_model = db.query(subscriptionPricingModel).filter(subscriptionPricingModel.id == id).first()
        if subscription_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        subscription_model.isDeleted = False
        subscription_model.updatedAt = datetime.now()

        db.add(subscription_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
