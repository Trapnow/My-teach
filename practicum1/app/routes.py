from flask import render_template, request, redirect, url_for
from practicum1.app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"{name}, Ваше сообщение доставлено, отправим Вам ответ на {email}"
    else:
        return redirect(url_for("contact"))
