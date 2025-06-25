from flask import Flask

app = Flask(__name__)

from book_shop.app import routes
