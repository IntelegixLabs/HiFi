import os
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi import UploadFile, File
from starlette import status
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.userPayload import userPayload
from schemas.financialTradingInputsSchema import financialTradingInputsSchema
from routers.generative_ai.multi_agent_financial_analysis import financial_trading_crew

from gen_ai.graph_explainer import graph_explainer

router = APIRouter(
    prefix='/generative-ai',
    tags=['Generative AI']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post('/graph_explainer', status_code=status.HTTP_200_OK)
async def get_graph_explainer(file: UploadFile = File(), user: userPayload = Depends(get_user_info)):
    try:
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication Failed')

        data = await file.read()
        file_name = f"{user.id}{os.path.splitext(file.filename)[1]}"
        # Create a file path with the media folder
        file_path = f"static/dumps/{file_name}"
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            buffer.write(data)

        resp = graph_explainer(file_path)

        return Response(content=resp, media_type="application/json")
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post('/stock_analysis', status_code=status.HTTP_200_OK)
async def stock_analysis(financialdata: financialTradingInputsSchema):
    # if user is None:
    #     raise HTTPException(status_code=401, detail='Authentication Failed')
    try:

        financial_inputs = {
            "stock_selection": financialdata.stock_selection,
            "initial_capital": financialdata.initial_capital,
            "risk_tolerance": financialdata.risk_tolerance,
            "trading_strategy_preference": financialdata.trading_strategy_preference,
            "news_impact_consideration": financialdata.news_impact_consideration
        }

        print(financial_inputs)

        resp = financial_trading_crew.kickoff(inputs=financial_inputs)

        print(resp)

        return resp
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
