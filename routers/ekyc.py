from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse
from starlette import status
from models import panModel
from config.database import SessionLocal
from .auth import get_user_info
from schemas.userPayload import userPayload
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


@router.get("/get_pan_card", status_code=status.HTTP_200_OK)
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


@router.post("/upload_extract_pan_data", status_code=status.HTTP_200_OK)
async def upload_extract_pan_data(db: db_dependency, file: UploadFile = File(), user: userPayload = Depends(get_user_info)):
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


@router.get("/video_kyc")
async def video_endpoint(user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return StreamingResponse(video_stream(), media_type="multipart/x-mixed-replace; boundary=frame")
