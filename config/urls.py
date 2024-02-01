from fastapi import APIRouter
from stocks.crud import router as stocks_router
routers = APIRouter()

routers.include_router(stocks_router)