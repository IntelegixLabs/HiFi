from config.database import Base
from sqlalchemy import Column, String, Boolean
from datetime import datetime


class userProfileModel(Base):
    __tablename__ = 'userProfile'

    userId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    phoneNumber = Column(String, unique=False, nullable=False)
    gender = Column(String, unique=False, nullable=False)
    dob = Column(String, nullable=False)
    expDate = Column(String, default=datetime.now, nullable=False)
    isDeleted = Column(Boolean, default=False, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)
