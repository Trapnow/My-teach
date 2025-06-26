from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаем объект базы данных
db = SQLAlchemy(app)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    img = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Section {self.title}"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}"



@app.route("/")
def index():
    sections = Section.query.all()
    return render_template("index.html", sections=sections)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
