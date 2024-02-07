from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .urls import routers


def create_app(app_name: str) -> FastAPI:
    app = FastAPI(title=app_name)
    client = AsyncIOMotorClient("mongodb://localhost:27017/market")
    app.mongodb_client = client

    @app.on_event("startup")
    async def initialize_db():
        # Initialize beanie with the Product document class
        await init_beanie(database=client.market, document_models=["stocks.models.Stocks"])

    @app.on_event("shutdown")
    async def shutdown_db_client():
        app.mongodb_client.close()

    app.include_router(
        routers,
        prefix="/api",
        tags=["HiFi_apis"],
        responses={500: {"description": "Please contact base234"},
                   404: {"description": "page Not found"}},
    )
    return app
