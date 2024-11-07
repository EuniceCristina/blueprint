from flask import Flask, render_template, url_for, request, Blueprint, redirect
from books.models import Book
from users.models import User
from emprestimos.models import Emprestimo


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