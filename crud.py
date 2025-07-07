# crud.py, defines the core database logic: functions that perform Create, Read, Update, and Delete operations.
# Handles direct interaction with the database.
# Keeps business logic separate from request/response handling.
from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException
import schemas

#List all users from the database
def get_users(db: Session):
    return db.query(User).all()

#Creata a new user with username, email and password, add it to the database
def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Find a user by its unique ID in the database
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
    
#Find a user by ID and update its name and email, then update the database
def update_user(db: Session, user_id: int, new_name: str = None, new_email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if new_name:
        user.name = new_name
    if new_email:
        user.email = new_email

    db.commit()
    db.refresh(user)
    return user

#Find a user by ID and update its password
def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.password = new_password  # hash later!
    db.commit()
    db.refresh(user)
    return user

#Find a user by ID and delete it, commit the change to the database
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"Deleted user {user.name}"}
