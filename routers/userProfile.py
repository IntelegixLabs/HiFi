import os
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile, File
from starlette import status
from models import userProfileModel, profileImageModel
from config.database import SessionLocal
from .auth import get_user_info
from schemas.userProfileSchema import userProfileSchema
from schemas.userPayload import userPayload, userCompleteData
from datetime import datetime

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


@router.get("/get_user_data", status_code=status.HTTP_200_OK)
async def root(db: db_dependency, user: userPayload = Depends(get_user_info)) -> userCompleteData:
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        user_model = db.query(userProfileModel).filter(userProfileModel.userId == user.id).filter(
            userProfileModel.isDeleted == False).first()

        if user_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        current_date = str(datetime.now())

        isPremium = (user_model.expDate > current_date)

        userdata = userCompleteData(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phoneNumber=user_model.phoneNumber,
            gender=user_model.phoneNumber,
            dob=user_model.dob,
            isPremium=isPremium,
            expDate=user_model.expDate,
            isDeleted=user_model.isDeleted,
            updatedAt=user_model.updatedAt,
            createdAt=user_model.createdAt,
            realm_roles=user.realm_roles,
            client_roles=user.client_roles
        )
        return userdata
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/get_profile', status_code=status.HTTP_200_OK)
async def get_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(userProfileModel).filter(userProfileModel.userId == user.id).filter(
            userProfileModel.isDeleted == False).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/add_profile", status_code=status.HTTP_201_CREATED)
async def create_user_profile(db: db_dependency, user_profile_data: userProfileSchema,
                              user: userPayload = Depends(get_user_info)):
    try:
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
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/update_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_profile(db: db_dependency, user_profile_data: userProfileSchema,
                              user: userPayload = Depends(get_user_info), profile_id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).filter(
            userProfileModel.isDeleted == False).first()
        if user_profile_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        user_profile_model.phoneNumber = user_profile_data.phoneNumber
        user_profile_model.gender = user_profile_data.gender
        user_profile_model.dob = user_profile_data.dob
        user_profile_model.updatedAt = datetime.now()

        db.add(user_profile_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.delete("/delete_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info), profile_id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).first()
        if user_profile_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        user_profile_model.isDeleted = True
        user_profile_model.updatedAt = datetime.now()

        db.add(user_profile_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.patch("/reactivate_profile/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def reactivate_user_profile(db: db_dependency, user: userPayload = Depends(get_user_info),
                                  profile_id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        user_profile_model = db.query(userProfileModel).filter(userProfileModel.userId == profile_id).first()
        if user_profile_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')

        user_profile_model.isDeleted = False
        user_profile_model.updatedAt = datetime.now()

        db.add(user_profile_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/upload_profile_image", status_code=status.HTTP_201_CREATED)
async def upload_profile_image(db: db_dependency, file: UploadFile = File(),
                               user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        user_profile_image_model = db.query(profileImageModel).filter(profileImageModel.userId == user.id).first()

        data = await file.read()
        file_name = f"{user.id}{os.path.splitext(file.filename)[1]}"
        # Create a file path with the media folder
        file_path = f"static/profile/{file_name}"
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            buffer.write(data)

        if user_profile_image_model is None:
            user_profile_image_model = profileImageModel(
                userId=user.id,
                file_url=file_path,
            )

            db.add(user_profile_image_model)
            db.commit()
        else:
            user_profile_image_model.file_url = file_path
            db.add(user_profile_image_model)
            db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get("/get_profile_image", status_code=status.HTTP_200_OK)
async def get_profile_image(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')

        pan_profile_model = db.query(profileImageModel).filter(profileImageModel.userId == user.id).first()

        if pan_profile_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')
        return pan_profile_model
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
