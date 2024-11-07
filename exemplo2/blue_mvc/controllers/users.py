from flask import render_template, Blueprint, url_for, request, redirect
from models.user import User

bp = Blueprint('users',__name__, url_prefix='/users', template_folder='templates')

@bp.route('/')
def index():
    return render_template('users/index.html',users=User.all())

@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        user = User(nome)
        User.save(user)
        return redirect(url_for('users.index'))
    return render_template('users/register.html')