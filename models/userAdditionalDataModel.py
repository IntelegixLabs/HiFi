from config.database import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from datetime import datetime


class userAdditionalDataModel(Base):
    __tablename__ = 'userAdditionalData'

    userId = Column(String, ForeignKey("userProfile.userId"), primary_key=True, unique=True, nullable=False, index=True)
    salary = Column(Integer, unique=False, nullable=False)
    no_of_dependents = Column(Integer, unique=False, nullable=False)
    medical_insurance_cover = Column(Integer, unique=False, nullable=False)
    term_insurance_cover = Column(Integer, unique=False, nullable=False)
    disabilities = Column(Boolean, default=False, nullable=False)
    liabilities_amount = Column(Integer, unique=False, nullable=False)
    stocks_mutual_funds_investment = Column(Integer, unique=False, nullable=False)
    fixed_deposit = Column(Integer, unique=False, nullable=False)
    isDeleted = Column(Boolean, default=False, nullable=False)
    createdAt = Column(String, default=datetime.now, nullable=False)
    updatedAt = Column(String, default=datetime.now, nullable=False)
