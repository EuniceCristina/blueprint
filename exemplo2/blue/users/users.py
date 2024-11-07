from flask import render_template, url_for, redirect, Blueprint, request

from users.models import User

bp = Blueprint('users',__name__, url_prefix='/users', template_folder='templates')

@bp.route('/')
def index():
    render_template('users/index.html', users = User.all())
