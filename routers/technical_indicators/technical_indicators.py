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
    prefix='/technical_indicators',
    tags=['Technical Indicators APIs']
)


@router.get('/SMA/query', status_code=status.HTTP_200_OK)
async def SMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/EMA/query', status_code=status.HTTP_200_OK)
async def EMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/WMA/query', status_code=status.HTTP_200_OK)
async def WMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/DEMA/query', status_code=status.HTTP_200_OK)
async def DEMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/TEMA/query', status_code=status.HTTP_200_OK)
async def TEMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/TRIMA/query', status_code=status.HTTP_200_OK)
async def TRIMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/KAMA/query', status_code=status.HTTP_200_OK)
async def KAMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MAMA/query', status_code=status.HTTP_200_OK)
async def MAMA(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/VWAP/query', status_code=status.HTTP_200_OK)
async def VWAP(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/T3/query', status_code=status.HTTP_200_OK)
async def T3(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MACD/query', status_code=status.HTTP_200_OK)
async def MACD(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MACDEXT/query', status_code=status.HTTP_200_OK)
async def MACDEXT(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/STOCH/query', status_code=status.HTTP_200_OK)
async def STOCH(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/STOCHF/query', status_code=status.HTTP_200_OK)
async def STOCHF(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/RSI/query', status_code=status.HTTP_200_OK)
async def RSI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/STOCHRSI/query', status_code=status.HTTP_200_OK)
async def STOCHRSI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/WILLR/query', status_code=status.HTTP_200_OK)
async def WILLR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ADX/query', status_code=status.HTTP_200_OK)
async def ADX(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ADXR/query', status_code=status.HTTP_200_OK)
async def ADXR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/APO/query', status_code=status.HTTP_200_OK)
async def APO(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/PPO/query', status_code=status.HTTP_200_OK)
async def PPO(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MOM/query', status_code=status.HTTP_200_OK)
async def MOM(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/BOP/query', status_code=status.HTTP_200_OK)
async def BOP(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/CCI/query', status_code=status.HTTP_200_OK)
async def CCI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/CMO/query', status_code=status.HTTP_200_OK)
async def CMO(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ROC/query', status_code=status.HTTP_200_OK)
async def ROC(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ROCR/query', status_code=status.HTTP_200_OK)
async def ROCR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/AROON/query', status_code=status.HTTP_200_OK)
async def AROON(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/AROONOSC/query', status_code=status.HTTP_200_OK)
async def AROONOSC(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MFI/query', status_code=status.HTTP_200_OK)
async def MFI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/TRIX/query', status_code=status.HTTP_200_OK)
async def TRIX(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ULTOSC/query', status_code=status.HTTP_200_OK)
async def ULTOSC(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/DX/query', status_code=status.HTTP_200_OK)
async def DX(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MINUS_DI/query', status_code=status.HTTP_200_OK)
async def MINUS_DI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/PLUS_DI/query', status_code=status.HTTP_200_OK)
async def PLUS_DI(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MINUS_DM/query', status_code=status.HTTP_200_OK)
async def MINUS_DM(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/PLUS_DM/query', status_code=status.HTTP_200_OK)
async def PLUS_DM(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/BBANDS/query', status_code=status.HTTP_200_OK)
async def BBANDS(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MIDPOINT/query', status_code=status.HTTP_200_OK)
async def MIDPOINT(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/MIDPRICE/query', status_code=status.HTTP_200_OK)
async def MIDPRICE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/SAR/query', status_code=status.HTTP_200_OK)
async def SAR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/TRANGE/query', status_code=status.HTTP_200_OK)
async def TRANGE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ATR/query', status_code=status.HTTP_200_OK)
async def ATR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/NATR/query', status_code=status.HTTP_200_OK)
async def NATR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/AD/query', status_code=status.HTTP_200_OK)
async def AD(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/ADOSC/query', status_code=status.HTTP_200_OK)
async def ADOSC(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/OBV/query', status_code=status.HTTP_200_OK)
async def OBV(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_TRENDLINE/query', status_code=status.HTTP_200_OK)
async def HT_TRENDLINE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_SINE/query', status_code=status.HTTP_200_OK)
async def HT_SINE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_TRENDMODE/query', status_code=status.HTTP_200_OK)
async def HT_TRENDMODE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_DCPERIOD/query', status_code=status.HTTP_200_OK)
async def HT_DCPERIOD(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_DCPHASE/query', status_code=status.HTTP_200_OK)
async def HT_DCPHASE(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")


@router.get('/HT_PHASOR/query', status_code=status.HTTP_200_OK)
async def HT_PHASOR(request: Request, user: userPayload = Depends(get_user_info)):
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
        raise HTTPException(status_code=400, detail=f"Module - Error - {err}")
