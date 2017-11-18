from flask import Flask, render_template, request, url_for,redirect,session,flash

from models.categories import Categories

from models.user import User

from models.recipes import Recipe

from flask_bootstrap import Bootstrap
user_store ={}

app = Flask(__name__)

app.secret_key = "my secret key"

bootstrap = Bootstrap(app)
def sign_up(username,password):
    if username and password:
        user_store[username]= User(username,password)
    


def log_in(username,password):
    if username and password:
        if user_store.get(username):
            if  password == user_store[username].password:
                return True


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():   
    return render_template('dashboard.html') 

@app.route("/signup", methods =["POST", "GET"])

def signup():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # new_user.signup(firstname,lastname,email,password)

        sign_up(username,password)

        flash("Signed up successfully, Please log in")

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/login", methods =["POST" , "GET"])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        session["username"] = username

        if username == session["username"] and username != " ":

            result = log_in(username, password)
            if result == True:
                 
                return redirect(url_for('dashboard'))
           
                flash("Logged in successfully")
          
            flash("Wrong details.......Please login") 

            return redirect(url_for('login'))
                
    return render_template('login.html')

@app.route("/logout", methods =["POST" , "GET"])

def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route('/addcategories' , methods = ['POST','GET'])
def addcategories():
  
    if request.method == 'POST':   
        category_name = request.form['categoryname']   
        Categories.add_category(category_name)     
        flash("Category added")
        return redirect(url_for('viewcategories'))       
    return render_template('categories.html')
  

@app.route('/viewcategories')
def viewcategories():
    recipe_category = Categories.view_categories()
    return render_template('viewcategories.html', recipe_category = recipe_category) 

@app.route('/getcategory/<categoryname>')
def getcategory(categoryname):  
    recipe_category = Categories.view_categories()      
    return render_template('addrecipe.html',recipe_category = recipe_category) 


@app.route('/deletecategories/<categoryname>')
def deletecategories(categoryname):
    Categories.delete_category(categoryname) 

    flash ("Category deleted successfully")   
    return redirect(url_for('viewcategories'))


@app.route('/editcategories/<categoryname>', methods = ['POST','GET'])

def editcategories(categoryname):  
    categoryname = session[categoryname]
    if request.method == 'POST':
        
        new_categoryname = request.form["new_categoryname"]
        
        print (categoryname)
    
        Categories.edit_category(categoryname,new_categoryname)

        flash ("Category updated")

        return redirect(url_for('viewcategories'))

    return render_template('editcategories.html', categoryname= categoryname )

@app.route('/addrecipe', methods = ['POST','GET']) 
def addrecipe():   
    if request.method == 'POST':
        recipe_name = request.form['recipename']
        recipe_description = request.form['description']
        Recipe.add_recipe(recipe_name,recipe_description)

        return redirect(url_for('viewrecipes'))

    return render_template('addrecipe.html')


@app.route('/viewrecipes', methods = ['POST', 'GET'])
def viewrecipes():  
    my_recipe = Recipe.view_recipes()
    return render_template('viewrecipes.html', my_recipe = my_recipe) 

@app.route('/deleterecipe/<recipename>/<description>')
def deleterecipe(recipename,description):
    Recipe.delete_recipe(recipename,description)    
    return redirect(url_for('viewrecipes'))



if __name__=="__main__":
    app.run(debug=True)
    
    