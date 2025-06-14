# app/services/user_service.py
from passlib.context import CryptContext
from app.repositories.user_repository import UserRepository
from app.models.user_dto import UserDTO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, repository: UserRepository):
        self.repo = repository

    def hash_password(self, raw_password: str) -> str:
        return pwd_context.hash(raw_password)

    def verify_password(self, raw: str, hashed: str) -> bool:
        return pwd_context.verify(raw, hashed)

    def get_by_username(self, username: str) -> UserDTO | None:
        user = self.repo.get_by_username(username)
        return UserDTO.from_orm(user) if user else None

    def get_by_email(self, email: str) -> UserDTO | None:
        user = self.repo.get_by_email(email)
        return UserDTO.from_orm(user) if user else None

    def create_user(self, username: str, email: str, password: str) -> UserDTO:
        hashed = self.hash_password(password)
        dto = UserDTO(username=username, email=email, password_hash=hashed)
        user = self.repo.create(dto)
        return UserDTO.from_orm(user)