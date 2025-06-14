# app/models/user_dto.py
from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr
    password_hash: str

    class Config:
        orm_mode = True