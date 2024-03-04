from config.database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean
from datetime import datetime


class subscriptionPricingModel(Base):
    __tablename__ = 'subscriptionPricing'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float,  default=0)
    currencyCode = Column(String)
    discount = Column(Float, default=0)
    duration = Column(Integer, default=0)
    description = Column(String)
    isDeleted = Column(Boolean, default=False, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)
