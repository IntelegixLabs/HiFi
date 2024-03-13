from pydantic import BaseModel, Field


class subscriptionPricingSchema(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    price: float = Field(gt=0)
    currencyCode: str = Field(min_length=3, max_length=3)
    discount: float = Field(gt=-1, lt=100)
    duration: int = Field(gt=0)
    description: str = Field(min_length=10, max_length=100)

