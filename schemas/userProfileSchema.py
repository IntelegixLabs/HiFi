from pydantic import BaseModel


class userProfileSchema(BaseModel):
    phoneNumber: str
    gender: str
    dob: str


class userProfileDeleteSchema(BaseModel):
    isDeleted: bool
