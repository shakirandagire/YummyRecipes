from flask import Flask
from flask import render_template
from flask import *
app = Flask(__name__)

User = {}
Recipes = {}
Categories = {}

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/categories')
def categories():

    if request.method=='POST':
        name = request.form['name']
        description=request.form['description']
        
        if name in Category :
            Categories['name']= name
            Categories['description']=description
            
        return redirect(url_for('categories'))
    return render_template('categories.html')

@app.route('/addrecipe') 
def addrecipe():
    if request.method=='POST':
        name=request.form['name']
        category=request.form['category']
        description=request.form['description']
        
        if name in Recipe :
            Recipes['name']=name
            Recipes['category']=category
            Recipes['description']=description
            
        return redirect(url_for('addrecipe'))
    return render_template('addrecipe.html')

    
if __name__=="__main__":
    app.run(debug=True)
    
    