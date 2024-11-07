from flask import Flask, render_template, redirect, url_for, request, Blueprint
from models.user import User
from models.book import Book
from models.emprestimos import Emprestimo




bp = Blueprint('emprestimos', __name__, url_prefix='/emprestimos', template_folder='templates')

@bp.route('/')
def index():
    return render_template('emprestimos/index.html',emprestimos=Emprestimo.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        data = request.form['data']
        user = request.form['user']
        book = request.form['book']
        Emprestimo.save(data, user, book)

       
        
        return redirect(url_for('emprestimos.index' ))


    return render_template('emprestimos/register.html', users=User.all(), books = Book.all())