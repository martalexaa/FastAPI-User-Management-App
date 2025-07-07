# In routes/users.py, I define API endpoints related to users.
# HTTP routes (e.g., @router.get, @router.post)
# Functions that handle user operations, like create, read, update, delete
# Dependency injection (e.g., getting the DB session)
# Connecting schemas with CRUD logic to serve client requests.
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter()

# Get all users
@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Read user by ID
@router.get("/user/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create user
@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Update user
@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_user(
        db,
        user_id=user_id,
        new_name=user_update.new_name,
        new_email=user_update.new_email,
    )

# Delete user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(schemas.UserBase).filter(schemas.UserBase.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return crud.delete_user(db, user_id)

# Authenticate user
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = crud.authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome {authenticated_user.name}"}