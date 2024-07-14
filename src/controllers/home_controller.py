from flask import render_template
from flask import Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='../views/templates')

@home_blueprint.route('/')
def home():
    return render_template('index.html')
