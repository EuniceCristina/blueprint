-- Cria a tabela 'users' se não existir
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Cria a tabela 'esportes' se não existir, com uma chave estrangeira referenciando a tabela 'users'
CREATE TABLE IF NOT EXISTS esportes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
);