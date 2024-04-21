from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import userAdditionalDataModel
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.userProfileAdditionalDataSchema import userProfileAdditionalDataSchema
from schemas.userPayload import userPayload
from datetime import datetime

router = APIRouter(
    prefix='/investment-profile',
    tags=['User Additional Profile']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/data', status_code=status.HTTP_200_OK)
async def get_user_additional_data_profile(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(userAdditionalDataModel).filter(userAdditionalDataModel.userId == user.id).filter(
            userAdditionalDataModel.isDeleted == False).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/data", status_code=status.HTTP_201_CREATED)
async def create_user_additional_data_profile(db: db_dependency,
                                              user_profile_additional_data: userProfileAdditionalDataSchema,
                                              user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')

        user_profile_additional_data_model = userAdditionalDataModel(
            userId=user.id,
            salary=user_profile_additional_data.salary,
            no_of_dependents=user_profile_additional_data.no_of_dependents,
            medical_insurance_cover=user_profile_additional_data.medical_insurance_cover,
            term_insurance_cover=user_profile_additional_data.term_insurance_cover,
            disabilities=user_profile_additional_data.disabilities,
            liabilities_amount=user_profile_additional_data.liabilities_amount,
            stocks_mutual_funds_investment=user_profile_additional_data.stocks_mutual_funds_investment,
            fixed_deposit=user_profile_additional_data.fixed_deposit
        )

        db.add(user_profile_additional_data_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/data/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_additional_data_profile(db: db_dependency,
                                              user_profile_additional_data: userProfileAdditionalDataSchema,
                                              user: userPayload = Depends(get_user_info), profile_id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        user_profile_additional_data_model = db.query(userAdditionalDataModel).filter(
            userAdditionalDataModel.userId == profile_id).filter(
            userAdditionalDataModel.isDeleted == False).first()
        if user_profile_additional_data_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        user_profile_additional_data_model.salary = user_profile_additional_data.salary
        user_profile_additional_data_model.no_of_dependents = user_profile_additional_data.no_of_dependents
        user_profile_additional_data_model.medical_insurance_cover = user_profile_additional_data.medical_insurance_cover
        user_profile_additional_data_model.term_insurance_cover = user_profile_additional_data.term_insurance_cover
        user_profile_additional_data_model.disabilities = user_profile_additional_data.disabilities
        user_profile_additional_data_model.liabilities_amount = user_profile_additional_data.liabilities_amount
        user_profile_additional_data_model.stocks_mutual_funds_investment = user_profile_additional_data.stocks_mutual_funds_investment
        user_profile_additional_data_model.fixed_deposit = user_profile_additional_data.fixed_deposit
        user_profile_additional_data_model.updatedAt = datetime.now()

        db.add(user_profile_additional_data_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
