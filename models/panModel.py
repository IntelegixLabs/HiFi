from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from datetime import datetime


class panModel(Base):
    __tablename__ = 'pan'

    userId = Column(String, ForeignKey("userProfile.userId"), primary_key=True, unique=True, nullable=False, index=True)
    file_url = Column(String, default=datetime.now)
