from src.domain.entities.user import User

class IUserRepository:
    def create(self, usuario: User) -> User:
        pass
    def fetchall(self) -> list[User]:
        pass
    def login(self, nome: str, senha: str) -> str | None:
        pass