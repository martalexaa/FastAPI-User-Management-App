from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(50), index=True)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password = Column(String(200))