from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import userProfileModel
from config.database import SessionLocal
from .auth import get_user_info
from schemas.userProfileSchema import userProfileSchema
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/user_profile',
    tags=['User Profile']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/get_user_data")
async def root(user: userPayload = Depends(get_user_info)):
    return user


@router.get('/get_profile', status_code=status.HTTP_200_OK)
async def get_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(userProfileModel).filter(userProfileModel.userId == user.id).filter(
        userProfileModel.isDeleted == False).first()


@router.post("/add_profile", status_code=status.HTTP_201_CREATED)
async def create_user_profile(db: db_dependency, user_profile_data: userProfileSchema,
                              user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user_profile_model = userProfileModel(
        userId=user.id,
        phoneNumber=user_profile_data.phoneNumber,
        gender=user_profile_data.gender,
        dob=user_profile_data.dob
    )

    db.add(user_profile_model)
    db.commit()


@router.put("/update_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_profile(db: db_dependency, user_profile_data: userProfileSchema,
                              user: userPayload = Depends(get_user_info), profile_id: str = Path):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).filter(
        userProfileModel.isDeleted == False).first()
    if user_profile_model is None:
        raise HTTPException(status_code=404, detail='Profile not found.')

    user_profile_model.phoneNumber = user_profile_data.phoneNumber
    user_profile_model.gender = user_profile_data.gender
    user_profile_model.dob = user_profile_data.dob

    db.add(user_profile_model)
    db.commit()


@router.delete("/delete_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info), profile_id: str = Path):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).first()
    if user_profile_model is None:
        raise HTTPException(status_code=404, detail='Profile not found.')

    user_profile_model.isDeleted = True
    db.add(user_profile_model)
    db.commit()


@router.patch("/reactivate_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def reactivate_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info),
                                  profile_id: str = Path):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).first()
    if user_profile_model is None:
        raise HTTPException(status_code=404, detail='Profile not found.')

    user_profile_model.isDeleted = False
    db.add(user_profile_model)
    db.commit()
