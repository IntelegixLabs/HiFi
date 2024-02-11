from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from datetime import datetime


class eKycModel(Base):
    __tablename__ = 'eKyc'

    userId = Column(String, ForeignKey("userProfile.userId"), primary_key=True, unique=True, nullable=False, index=True)
    pan = Column(String, unique=True, nullable=False)
    aadhar = Column(String, unique=True, nullable=False)
    kycVerified = Column(Boolean, default=False, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)