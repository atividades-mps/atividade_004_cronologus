from src.domain.entities.user import User 
from src.api.repositories.database import get_db, close_connection, query_db
from src.domain.ports.iuser_repository import IUserRepository 

class SQLiteUserRepository(IUserRepository):
    def __init__(self):
        super().__init__()

    def create(self, usuario: User) -> User:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, senha, status) VALUES (?,?,?,?)', 
            [usuario.nome, usuario.email, usuario.senha, usuario.status]
        )
        db.commit()
        return User(cursor.lastrowid, usuario.nome, usuario.email, usuario.senha, usuario.status)

    def fetchall(self) -> list[User]:
        pass

    def login(self,nome: str, senha: str) -> str | None:
        user = query_db("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", [nome, senha], True)
        return str(user[0]) if user != None else None 