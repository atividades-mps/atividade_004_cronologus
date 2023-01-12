from datetime import datetime

class User:
    def __init__(self, id: int | None, nome: str, email: str, senha: str, status: int):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
        self.status = status