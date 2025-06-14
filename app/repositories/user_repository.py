# app/repositories/user_repository.py
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.models.user_dto import UserDTO

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str) -> User | None:
        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

    def get_by_email(self, email: str) -> User | None:
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def create(self, dto: UserDTO) -> User:
        user = User(
            username=dto.username,
            email=dto.email,
            password_hash=dto.password_hash
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user