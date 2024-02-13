import os
import requests
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from ..auth import get_user_info
from schemas.userPayload import userPayload

from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_URL = os.getenv("ALPHA_VANTAGE_URL")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

router = APIRouter(
    prefix='/news_insights',
    tags=['News Insights APIs']
)


@router.get('/NEWS_SENTIMENT/query', status_code=status.HTTP_200_OK)
async def NEWS_SENTIMENT(request: Request, user: userPayload = Depends(get_user_info)):
    params = request.query_params
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        url = ALPHA_VANTAGE_URL + "/query?" + str(params) + "&apikey=" + ALPHA_VANTAGE_KEY
        payload = {}
        headers = {'User-Agent': 'request'}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST


@router.get('/TOP_GAINERS_LOSERS/query', status_code=status.HTTP_200_OK)
async def TOP_GAINERS_LOSERS(request: Request, user: userPayload = Depends(get_user_info)):
    params = request.query_params
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        url = ALPHA_VANTAGE_URL + "/query?" + str(params) + "&apikey=" + ALPHA_VANTAGE_KEY
        payload = {}
        headers = {'User-Agent': 'request'}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST


@router.get('/ANALYTICS/query', status_code=status.HTTP_200_OK)
async def ANALYTICS(request: Request, user: userPayload = Depends(get_user_info)):
    params = request.query_params
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        url = ALPHA_VANTAGE_URL + "/query?" + str(params) + "&apikey=" + ALPHA_VANTAGE_KEY
        payload = {}
        headers = {'User-Agent': 'request'}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST


@router.get('/ADVANCED_ANALYTICS/query', status_code=status.HTTP_200_OK)
async def ADVANCED_ANALYTICS(request: Request, user: userPayload = Depends(get_user_info)):
    params = request.query_params
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    try:
        url = ALPHA_VANTAGE_URL + "/query?" + str(params) + "&apikey=" + ALPHA_VANTAGE_KEY
        payload = {}
        headers = {'User-Agent': 'request'}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except Exception as err:
        return {"message": f"Module - Error - {err}"}, status.HTTP_400_BAD_REQUEST
