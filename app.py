from flask import Flask, render_template, request, url_for,redirect,session

from controller.categories import Categories

from controller.user import User

from controller.recipes import Recipe
app = Flask(__name__)

app.secret_key = "my secret key"

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

        User.signup(username,password)

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/login", methods =["POST" , "GET"])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        # new_user.login(firstname, password)
        if User.login(username, password):
            session["username"] = username
                 
            return redirect(url_for('dashboard'))
        else:           
             return redirect(url_for('login'))
                
    return render_template('login.html')

@app.route("/logout", methods =["POST" , "GET"])

def logout():
    session.pop('username', None)
  
    return redirect(url_for('main'))

@app.route('/addcategories' , methods = ['POST','GET'])
def addcategories():
    # return request.method
    if request.method == 'POST':
        # return request.method
        category_name = request.form['categoryname']
        # category = Categories(category_name)
        Categories.add_category(category_name)
        # return Categories.view_categories()
        return redirect(url_for('viewcategories'))
        
    return render_template('categories.html')
  

@app.route('/viewcategories')
def viewcategories():
    # category_name = request.form['categoryname']
    # category = Categories(category_name)
    recipe_category = Categories.view_categories()
    return render_template('viewcategories.html', recipe_category = recipe_category) 

@app.route('/getcategory')
def getcategory():
  
    recipe_category = Categories.view_categories()
    return render_template('addrecipe.html', recipe_category = recipe_category) 


@app.route('/deletecategories/<categoryname>')
def deletecategories(categoryname):
    Categories.delete_category(categoryname)    
    return redirect(url_for('viewcategories'))


@app.route('/editcategories/<categoryname>', methods = ['POST','GET'])
def editcategories(categoryname): 
    
    if request.method == 'POST':
        new_categoryname = request.form["new_categoryname"]
        Categories.edit_category(categoryname,new_categoryname)
        return redirect(url_for('viewcategories'))


@app.route('/addrecipe', methods = ['POST','GET']) 
def addrecipe():   
    if request.method == 'POST':
        recipe_name = request.form['recipename']
        recipe_description = request.form['description']
        Recipe.add_recipe(recipe_name,recipe_description)
        session['recipe_name']= recipe_name
        session['recipe_description'] = recipe_description
        return redirect(url_for('viewrecipes',))

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
    
    