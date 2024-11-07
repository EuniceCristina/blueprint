from database import get_connection

class User:
    def __init__(self,nome):
        self.nome = nome
    
    def save(self):
        conn = get_connection()
        conn.execute('INSERT INTO users(nome) VALUES(?)',(self.nome))
        conn.commit()
        conn.close()

