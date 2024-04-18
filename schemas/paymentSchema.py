from pydantic import BaseModel, Field


class paymentSchema(BaseModel):
    id: int = Field(gt=0)
