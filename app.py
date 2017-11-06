from flask import Flask
from flask import render_template, request, url_for,redirect,session
from categories import Categories
from recipes import Recipes
from user import User

app = Flask(__name__)
app.secret_key = 'codegirl'

new_user = User()

@app.route('/')
def main():
   
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'firstname' in session:
        firstname = session['firstname']
    
    return render_template('dashboard.html')


@app.route("/signup", methods =["POST",  "GET"])

def signup():

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        new_user = User(firstname,lastname,email,password)

        new_user.signup(firstname,lastname,email,password)

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/login", methods =["POST" , "GET"])
def login():
    if request.method == 'POST':
      session['firstname'] = request.form['firstname']
        
      return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('firstname', None)
   return redirect(url_for('main'))

@app.route('/addcategories' , methods =['POST','GET'])
def addcategories():

    if request.method == 'POST':
        categoryname = request.form['categoryname']
        new_user = User(categories)
        new_user.add_category(categoryname)
        return redirect(url_for('dashboard'))
    return render_template('categories.html')
  

@app.route('/viewcategories', methods =['POST', 'GET'])
def viewcategories():  
    if request.method == "POST":
        categoryname = request.form['categoryname']
        new_user = User.categories
        category = new_user.view_categories(categoryname)
    return render_template('dashboard.html', categories = category)    


@app.route('/deletecategories')
def deletecategories():
    new_user = User(categories)
    new_user.delete_category(categories)
    return render_template('dashboard.html')


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
    
    