from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
import os

app = Flask(__name__, template_folder=os.getcwd() + "/templates/")
ckeditor = CKEditor()



ckeditor.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///base.db"
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
db = SQLAlchemy()
db.init_app(app)


with app.app_context():
    db.create_all()