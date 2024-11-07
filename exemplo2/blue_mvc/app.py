from flask import Flask, render_template
from controllers import users,esportes

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(esportes.bp)

@app.route('/')
def index():
          return render_template('index.html')