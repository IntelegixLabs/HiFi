from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey, DATETIME
from datetime import datetime


class userProfileModel(Base):
    __tablename__ = 'userProfile'

    userId = Column(String, ForeignKey("user_entity.id"), primary_key=True, unique=True, nullable=False, index=True)
    phoneNumber = Column(String, unique=True, nullable=False)
    gender = Column(String, unique=False, nullable=False)
    dob = Column(String, nullable=False)
    lastActive = Column(DATETIME, default=datetime.now, nullable=False)
    isPremium = Column(Boolean, default=False, nullable=False)
    isDeleted = Column(Boolean, default=False, nullable=False)
    createdAt = Column(DATETIME, default=datetime.now, nullable=False)
    updatedAt = Column(DATETIME, default=datetime.now, nullable=False)
