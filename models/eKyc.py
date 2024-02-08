from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey, DATETIME
from datetime import datetime


class eKycModel(Base):
    __tablename__ = 'eKyc'

    userId = Column(String, ForeignKey("user_entity.id"), primary_key=True, unique=True, nullable=False, index=True)
    pan = Column(String, unique=True, nullable=False)
    aadhar = Column(String, unique=True, nullable=False)
    isekycVerified = Column(Boolean, default=False, nullable=False)
    createdAt = Column(DATETIME, default=datetime.now, nullable=False)
    updatedAt = Column(DATETIME, default=datetime.now, nullable=False)


