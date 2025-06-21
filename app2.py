from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, Flask"

@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/info")
def info():
    return "This is an informational page."

@app.route("/calc/<num1>/<num2>")
def summa(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return f"The sum of {num1} and {num2} is {num1 + num2}."
    else:
        return "Вы ввели некорректные данные"

@app.route("/reverse/<text>")
def rev(text):
    if len(text) > 0:
        return f"{text[::-1]}"
    else:
        return "Введите какое нибудь слово"

@app.route("/user/<name>/<age>")
def user(name, age):
    if age < 0:
        return f"Hello, {name}. You are {age} years old."
    else:
        return "Возраст не может быть меньше 0"


if __name__ == "__main__":
    app.run(debug=True)