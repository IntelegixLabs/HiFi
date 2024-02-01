from fastapi import APIRouter
from .models import Stocks
from .schemas import StocksSchema
router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    stocks = await Stocks.find_one(Stocks.name == "Subhransu")

    if stocks is None:
        stocks = Stocks(name="Subhransu")
        await stocks.insert()
    stocks = StocksSchema(**stocks.dict())
    return {"message": stocks.model_dump()}
