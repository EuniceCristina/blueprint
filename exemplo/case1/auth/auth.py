from flask import Flask, render_template, url_for, request, Blueprint, redirect
from users.models import User


from flask_login import LoginManager,login_user, logout_user



auth_bp= Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@auth_bp.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        nome = request.form['nome']
        email = request.form['email']

        users = User.all()
        login = False
        for user in users:
            if user.nome==nome and user.email==email:
                login = True
                login_user(user)
                    
        if login==True:
            return redirect(url_for('users.index'))
        else:
            return redirect(url_for('auth.login'))
        
    return render_template('auth/index.html')

def logout():
    logout_user()
    return render_template('templates/index.html')