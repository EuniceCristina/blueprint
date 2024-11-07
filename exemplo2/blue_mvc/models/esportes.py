from database import get_connection

class Esporte:
    def __init__(self, nome,user_id):
        self.nome = nome
        self.user_id = user_id
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO esportes(nome,user_id) values(?,?)", (self.nome,self.user_id))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM esportes").fetchall()
        return users