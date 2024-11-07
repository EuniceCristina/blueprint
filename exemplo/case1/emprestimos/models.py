from database import get_connection

class Emprestimo():
    def __init__(self, data, user_id, book_id):
        self.data = data
        self.user_id = user_id
        self.book_id = book_id
    
    @classmethod
    def save(cls, data, user_id, book_id):
        conn = get_connection()
        
        conn.execute("INSERT INTO emprestimos (data_emp, user_id, book_id) VALUES (?,?,?)",(data, user_id, book_id))
        conn.commit()
       
        conn.close()
    
    @classmethod
    def all(cls):
        conn = get_connection()
        
        
        emprestimos = conn.execute("SELECT * FROM emprestimos").fetchall()
        
        conn.close()
        return emprestimos
