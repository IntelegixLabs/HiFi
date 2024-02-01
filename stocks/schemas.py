from typing import Optional

from bson import ObjectId
from pydantic import BaseModel as pydanticBaseModel, Field, ConfigDict


class BaseModel(pydanticBaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True, populate_by_name=True)
    id: Optional[ObjectId | str] = Field(None, alias="_id")


class StocksSchema(BaseModel):
    name: str
