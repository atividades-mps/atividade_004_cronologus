from src.domain.ports.iuser_repository import IUserRepository

class Login:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self, nome: str, senha: str) -> str | None:
        return self.repository.login(nome, senha)