from core import app, db
from flask import request
from db import Article

@app.post("/create")
@app.post("/create/")
def create_article():
    
    title = request.form['title']
    content = request.form['ckeditor']

    db.create_all()

    article = Article(title=title, body=content)
    db.session.add(article)
    db.session.commit()


    return "DOne"
    