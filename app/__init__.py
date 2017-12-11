from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "my secret key"
bootstrap = Bootstrap(app)

from app import views
