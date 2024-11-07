from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.esportes import Esporte

bp = Blueprint('esportes',__name__, url_prefix='/esportes', template_folder='templates')

@bp.route('/')
def index():
    return render_template('esportes/index.html',esportes= Esporte.all())

@bp.route('/registro',methods=['POST','GET'])
def register():
    if request.method=='POST':
        nome = request.form['nome']
        user= request.form['user']

        esporte = Esporte(nome,user)
        Esporte.save(esporte)
        
        return redirect(url_for('esportes.index'))
    return render_template('esportes/register.html',user=User.all())