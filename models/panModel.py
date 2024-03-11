from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class panModel(Base):
    __tablename__ = 'panImage'

    userId = Column(String, ForeignKey("userProfile.userId"), primary_key=True, unique=True, nullable=False, index=True)
    file_url = Column(String)
