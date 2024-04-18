from config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from datetime import datetime


class paymentModel(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, unique=True)
    userId = Column(String, ForeignKey("userProfile.userId"), nullable=False)
    subscription_id = Column(Integer, ForeignKey("subscriptionPricing.id"), nullable=False)
    totalAmount = Column(Float, default=0, nullable=False)
    days_valid = Column(Integer, nullable=False)
    status = Column(String, default="Pending", nullable=False)
    paymentIntentId = Column(String, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)
