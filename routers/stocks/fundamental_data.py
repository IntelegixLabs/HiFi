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
    prefix='/fundamental_data',
    tags=['Fundamental Data of Stocks']
)


@router.get('/OVERVIEW/query', status_code=status.HTTP_200_OK)
async def OVERVIEW(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/INCOME_STATEMENT/query', status_code=status.HTTP_200_OK)
async def INCOME_STATEMENT(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/BALANCE_SHEET/query', status_code=status.HTTP_200_OK)
async def BALANCE_SHEET(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/CASH_FLOW/query', status_code=status.HTTP_200_OK)
async def CASH_FLOW(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/EARNINGS/query', status_code=status.HTTP_200_OK)
async def EARNINGS(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/LISTING_STATUS/query', status_code=status.HTTP_200_OK)
async def LISTING_STATUS(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/EARNINGS_CALENDAR/query', status_code=status.HTTP_200_OK)
async def EARNINGS_CALENDAR(request: Request, user: userPayload = Depends(get_user_info)):
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


@router.get('/IPO_CALENDAR/query', status_code=status.HTTP_200_OK)
async def IPO_CALENDAR(request: Request, user: userPayload = Depends(get_user_info)):
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
