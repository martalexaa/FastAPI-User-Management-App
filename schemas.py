# schemas.py is for defining data validation and serialization using Pydantic models
# Validate request data (e.g. input for creating or updating a user)
# Control what data is returned in responses (e.g. hiding passwords)
# Ensure type safety between API and database layers.
from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Annotated, Optional
import re

# Common type constraints
NameStr = Annotated[str, constr(min_length=3, max_length=50)]
PasswordStr = Annotated[str, constr(min_length=8, max_length=128)]

class UserBase(BaseModel):
    name: NameStr
    email: EmailStr

class UserCreate(UserBase):
    password: PasswordStr

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must include at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must include at least one lowercase letter')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must include at least one special character')
        return v

class UserUpdate(BaseModel):
    name: Optional[NameStr] = None
    email: Optional[EmailStr] = None

class UserPasswordUpdate(BaseModel):
    password: PasswordStr

class UserDelete(UserBase):
    name: NameStr
    email: EmailStr

class UserOut(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class UserRead(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }