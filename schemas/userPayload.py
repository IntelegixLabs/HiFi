from pydantic import BaseModel


class userPayload(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    realm_roles: list
    client_roles: list


class userCompleteData(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    phoneNumber: str
    gender: str
    dob: str
    createdAt: str
    isPremium: bool
    expDate: str
    isDeleted: bool
    updatedAt: str
    createdAt: str
    realm_roles: list
    client_roles: list

