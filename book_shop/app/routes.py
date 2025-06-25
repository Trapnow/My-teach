from flask import render_template, request, redirect, url_for
from book_shop.app import app

@app.route("/")
def index():
    return render_template("index.html")