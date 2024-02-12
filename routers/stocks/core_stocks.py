import os
import requests
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, Request
from starlette import status
from ..auth import get_user_info
from schemas.userPayload import userPayload
from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_URL = os.getenv("ALPHA_VANTAGE_URL")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

router = APIRouter(
    prefix='/core_stocks',
    tags=['Core Stocks APIs']
)


@router.get('/SYMBOL_SEARCH/query', status_code=status.HTTP_200_OK)
async def SYMBOL_SEARCH(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_INTRADAY/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_INTRADAY(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_DAILY/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_DAILY(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_WEEKLY/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_WEEKLY(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_WEEKLY_ADJUSTED/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_WEEKLY_ADJUSTED(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_MONTHLY/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_MONTHLY(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/TIME_SERIES_MONTHLY_ADJUSTED/query', status_code=status.HTTP_200_OK)
async def TIME_SERIES_MONTHLY_ADJUSTED(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/GLOBAL_QUOTE/query', status_code=status.HTTP_200_OK)
async def GLOBAL_QUOTE(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/MARKET_STATUS/query', status_code=status.HTTP_200_OK)
async def MARKET_STATUS(request: Request, user: userPayload = Depends(get_user_info)):
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




