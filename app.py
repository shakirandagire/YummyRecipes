from flask import Flask
from flask import render_template, request, url_for


from categories import Categories
from recipes import Recipes
from user import User
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html' )

@app.route("/signup", methods =["POST",  "GET"])

def signup():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    new_user = User(firstname,lastname,email,password)
    new_user.signup()
    return render_template('dashboard.html', firstname = firstname)

@app.route("/login", methods =["POST" , "GET"])

def login():
    firstname = request.form['firstname']
    password = request.form['password']
    new_user = User(email,password)
    new_user.login()

    return render_template('dashboard.html', firstname = firstname)


@app.route('/addcategories')

def addcategories():
    new_category = Categories(categoryname)
   

    return render_template('categories.html')

@app.route('/viewcategories', methods=["POST"])

def viewcategories():
    categoryname = request.form['categoryname']
    categories = []
    categories.append(categoryname)

    return render_template('dashboard.html', categoryname =categoryname )

def deletecategories():
    categoryname = request.form['categoryname']
    categories = []
    categories.append(categoryname)

    return render_template('dashboard.html', categoryname =categoryname )



@app.route('/addrecipe') 
def addrecipe():

    return render_template('addrecipe.html')

@app.route('/viewrecipes', methods = ['POST'])

def viewrecipes():

    recipename = request.form['recipename']
    description = request.form['description']
    recipes = []
    recipes.append(recipename)
    recipes.append(description)

   

    return render_template('viewrecipes.html', recipename =recipename, description = description)
 

    
if __name__=="__main__":
    app.run(debug=True)
    
    