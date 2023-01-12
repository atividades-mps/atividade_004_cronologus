CREATE TABLE IF NOT EXISTS eventos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    data_hora DATE NOT NULL,
    status INT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    status INT NOT NULL
);

CREATE TABLE IF NOT EXISTS feriados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    data_hora DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS feriados_usuarios(
    id_feriado INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_feriado) REFERENCES feriados(id)
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);