from flask import Flask, redirect, url_for
from FDS.Blueprint import FDS_BP
from IBR.Blueprint import IBR_BP
from jinja2 import ChoiceLoader,FileSystemLoader
#from app.IBR.Blueprint import IBR_BP
import os


def create_app():
    app = Flask(__name__)

    #app.jinja_loader = ChoiceLoader([
    #    FileSystemLoader('templates'),
    #    FileSystemLoader('templates/FDS')
    #])

    @app.route('/')
    def hello():
        return redirect('/FDS')

    #app.register_blueprint(IBR_BP)
    app.register_blueprint(FDS_BP)
    app.register_blueprint(IBR_BP)

    return app