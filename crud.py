from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException
import schemas

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, name: str, email: str):
    return db.query(User).filter_by(name=name, email=email).first()
    
    
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

def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.password = new_password  # hash later as you said
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"Deleted user {user.name}"}
