import csv
import os
import json
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from ..auth import get_user_info
from schemas.userPayload import userPayload

from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_URL = os.getenv("ALPHA_VANTAGE_URL")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

router = APIRouter(
    prefix='/codes',
    tags=['CODES API']
)


@router.get('/currency_codes', status_code=status.HTTP_200_OK)
async def Currency_codes(user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        response = []
        csvfile = open('data/physical_currency_list.csv', 'r')
        fieldnames = ("currency_code", "currency_name")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            response.append(row)
        return response
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST


@router.get('/crypto_currency_codes', status_code=status.HTTP_200_OK)
async def Currency_codes(user: userPayload = Depends(get_user_info)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        response = []
        csvfile = open('data/digital_currency_list.csv', 'r')
        fieldnames = ("currency_code", "currency_name")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            response.append(row)
        return response
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST
