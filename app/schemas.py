from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    telegram_id: int
    name: str
    username: Optional[str]
    city: Optional[str]
    sphere: Optional[str]
    description: Optional[str]
    category: Optional[str]

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class SwipeCreate(BaseModel):
    to_user_id: int
    is_like: bool
