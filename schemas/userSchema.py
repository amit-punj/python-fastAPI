from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CreateUserSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    role: Optional[str] = None
    password: str = Field(..., min_length=6)
    phone: Optional[str] = None
    address: Optional[str] = None