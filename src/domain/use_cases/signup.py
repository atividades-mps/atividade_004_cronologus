from src.domain.ports.iuser_repository import IUserRepository
from src.domain.entities.user import User

class Signup:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self, user: User) -> User:
        return self.repository.create(user)