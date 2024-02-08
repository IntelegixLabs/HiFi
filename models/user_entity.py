from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey, DATETIME, Integer
from datetime import datetime


class user_entityModel(Base):
    __tablename__ = 'user_entity'

    id = Column(Integer, primary_key=True)