from config.database import Base
from sqlalchemy import Column, String, Integer, Boolean
from datetime import datetime


class subscriptionPricingModel(Base):
    __tablename__ = 'subscriptionPricing'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer,  default=0)
    currencyCode = Column(String, nullable=False)
    discount = Column(Integer, default=0)
    duration = Column(Integer, default=0)
    description = Column(String, nullable=False)
    isDeleted = Column(Boolean, default=False, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)
