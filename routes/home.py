from core import app
from flask import render_template

@app.get('/')
def home():
    return render_template("index.html")
