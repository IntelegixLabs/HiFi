from pydantic import BaseModel


class kycSchema(BaseModel):
    pan: str
    aadhar: str
    kycVerified: bool
