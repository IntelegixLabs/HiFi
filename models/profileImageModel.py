from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from datetime import datetime


class profileImageModel(Base):
    __tablename__ = 'profileImage'

    userId = Column(String, ForeignKey("userProfile.userId"), primary_key=True, unique=True, nullable=False, index=True)
    file_url = Column(String, default=datetime.now)
