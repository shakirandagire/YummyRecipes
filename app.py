from flask import Flask
from flask import render_template
from flask import *
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/addrecipe')
def addrecipe():
    return render_template('addrecipe.html')


if __name__=="__main__":
    app.run(debug=True)
    