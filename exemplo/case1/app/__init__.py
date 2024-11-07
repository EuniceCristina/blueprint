from flask import Flask, render_template
from users import users
from books import books
from emprestimos import emprestimos
from auth import auth
from users.models import User
from flask_login import LoginManager, login_required,login_user, logout_user, current_user

app = Flask (__name__, template_folder='templates')

login_manager = LoginManager()
app.config['SECRET_KEY'] = 'SUPERDIFICIL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(emprestimos.bp)
app.register_blueprint(auth.auth_bp)

@app.route('/')
def index():
    return render_template('index.html')