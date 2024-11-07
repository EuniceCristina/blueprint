from database import get_connection
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome) values(?,?)", (self.email, self.nome))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return [cls(id=row['id'], nome=row['nome'], email=row['email']) for row in users]
    
    @classmethod
    def get(cls, user_id):
        conexao = get_connection()
        SELECT = 'SELECT * FROM users WHERE id=?'
        row = conexao.execute(SELECT, (user_id,)).fetchone()
        if row:
            return cls(id=row['id'], nome=row['nome'], email=row['email'])
        return None

    def get_id(self):
        # Método necessário pelo Flask-Login
        return str(self.id)
        