from flask import Flask, render_template, request, url_for,redirect,session,flash
from app.models.categories import Categories
from app.models.user import User
from app.models.user import user_store
from app.models.recipes import Recipe
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "my secret key"
bootstrap = Bootstrap(app)

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
        User.sign_up(username,password)

        flash("Signed up successfully, Please log in")

        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route("/login", methods =["POST" , "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  
        session["username"] = username     
        if username in session["username"]: 
            User.log_in(username,password) 
            return redirect(url_for('dashboard'))           
            flash("Logged in successfully") 
        flash("Wrong details.Please sign up first or re-enter correct login details")
        return redirect(url_for("login"))        
    return render_template('login.html')

@app.route("/logout", methods =["POST" , "GET"])
def logout():
    session.pop('username')
    flash('You have logged out')
    return redirect(url_for('main'))

@app.route('/addcategories', methods = ['POST','GET'])
def addcategories(): 
    if request.method == 'POST': 
        category = user_store[session["username"]].add_category(request.form['categoryname'])
        if category == True :
            flash("Category added successfully")  
            print (category)  
            return redirect(url_for('viewcategories'))        
    return render_template('categories.html') 

@app.route('/viewcategories')
def viewcategories():
    # recipe_category = user_store[session["username"]].view_categories()
    # return render_template('viewcategories.html', recipe_category = recipe_category)
    return render_template('viewcategories.html', recipe_category=user_store[session['username']].category_store)

@app.route('/deletecategories/<categoryname>')
def deletecategories(categoryname):
    user_store[session['username']].delete_category(categoryname) 
    flash ("Category deleted successfully")   
    return redirect(url_for('viewcategories'))

@app.route('/editcategories/<categoryname>', methods = ['POST','GET'])
def editcategories(categoryname):  
    session['new_categoryname'] = categoryname
    if request.method == 'POST': 
        result = user_store[session["username"]].edit_category(
            session['new_categoryname'],request.form['categoryname'])      
        if result == True:      
            flash ("Category updated")
            return redirect(url_for('viewcategories',))
    return render_template('editcategories.html')


@app.route('/addrecipe/<recipename>', methods = ['POST','GET']) 
def addrecipe(recipename):    

    if request.method == 'POST':
        result = user_store[session["username"]].category_store[session['categoryname']].add_recipe(request.form['recipename'], request.form['description'])
        if result == True:
            flash("Recipe Added")
        else:
            flash("Not added")
        return redirect(url_for('viewrecipes'))
    return render_template('addrecipe.html')


@app.route('/viewrecipes', methods = ['POST', 'GET'])
def viewrecipes():  
    my_recipe = user_store[session["username"]].category_store[session['categoryname']].view_recipes()
    return render_template('viewrecipes.html', my_recipe = my_recipe) 

@app.route('/deleterecipe/<recipename>/<description>')
def deleterecipe(recipename,description):
    Recipe.delete_recipe(recipename,description)    
    return redirect(url_for('viewrecipes'))



if __name__=="__main__":
    app.run(debug=True)
    
    