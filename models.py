# models.py is to define the database structure using SQLAlchemy models. 
# Each class (e.g. User) represents a table, and each class attribute (e.g. name, email) 
# represents a column in that table.
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(50), index=True)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password = Column(String(200))