from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse
from starlette import status
from models import panModel, eKycModel
from config.database import SessionLocal
from .auth import get_user_info
from schemas.userPayload import userPayload
from schemas.kycSchema import kycSchema
import os

from ml.ekyc import video_stream
from ml.pan_card_extractor import Pan_Info_Extractor

router = APIRouter(
    prefix='/kyc',
    tags=['KYC Verification Endpoint']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/pan-card", status_code=status.HTTP_200_OK)
async def get_pan_card(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')

        pan_profile_model = db.query(panModel).filter(panModel.userId == user.id).first()

        if pan_profile_model is None:
            raise HTTPException(status_code=404, detail='Profile not found.')
        return pan_profile_model
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/pan-card", status_code=status.HTTP_200_OK)
async def upload_extract_pan_data(db: db_dependency, file: UploadFile = File(),
                                  user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        pan_profile_model = db.query(panModel).filter(panModel.userId == user.id).first()

        data = await file.read()
        file_name = f"{user.id}{os.path.splitext(file.filename)[1]}"
        # Create a file path with the media folder
        file_path = f"static/pan/{file_name}"
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            buffer.write(data)

        if pan_profile_model is None:
            pan_profile_model = panModel(
                userId=user.id,
                file_url=file_path,
            )

            db.add(pan_profile_model)
            db.commit()
        else:
            pan_profile_model.file_url = file_path
            db.add(pan_profile_model)
            db.commit()

        return Pan_Info_Extractor().info_extractor(file_path)
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/pan-card-detail', status_code=status.HTTP_200_OK)
async def pan_card_detail(db: db_dependency, user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(eKycModel).filter(eKycModel.userId == user.id).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/pan-card-detail", status_code=status.HTTP_201_CREATED)
async def add_pan_card_detail(db: db_dependency, kyc_data: kycSchema,
                              user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')
        eKyc_model = eKycModel(
            userId=user.id,
            pan=kyc_data.pan,
            aadhar=kyc_data.aadhar,
            kycVerified=kyc_data.kycVerified
        )

        db.add(eKyc_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/pan-card-detail/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_pan_card_detail(db: db_dependency,
                                 kyc_data: kycSchema,
                                 user: userPayload = Depends(get_user_info), profile_id: str = Path):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        kyc_data_model = db.query(eKycModel).filter(
            eKycModel.userId == profile_id).first()
        if kyc_data_model is None:
            raise HTTPException(status_code=404, detail='KYC data not found.')

        kyc_data_model.pan = kyc_data.pan
        kyc_data_model.aadhar = kyc_data.aadhar
        kyc_data_model.kycVerified = kyc_data.kycVerified
        kyc_data_model.updatedAt = datetime.now()

        db.add(kyc_data_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get("/video_kyc")
async def video_endpoint(user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return StreamingResponse(video_stream(), media_type="multipart/x-mixed-replace; boundary=frame")
