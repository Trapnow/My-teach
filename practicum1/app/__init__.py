from flask import Flask

app = Flask(__name__)
from practicum1.app import routes
