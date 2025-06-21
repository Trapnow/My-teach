import locale
from flask import render_template, request, redirect, url_for
from practicum1.app import app
from datetime import datetime

@app.route("/")
def index():
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    current_time = datetime.now()
    return render_template("index.html", current_time=current_time)


@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)


@app.route("/contact")
def contact():
    info = {
        'name': 'Служба поддержки',
        'address': {
            'street': 'ул. Центральная дом 5',
            'city': 'Москва',
            'zip': '12345'
        }
    }

    return render_template("contact.html", info=info)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"{name}, Ваше сообщение доставлено, отправим Вам ответ на {email}"
    else:
        return redirect(url_for("contact"))
