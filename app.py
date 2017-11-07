from flask import Flask, render_template, request, url_for,redirect,session


from controller.categories import Categories

from controller.user import User
app = Flask(__name__)

app.secret_key = "my secret key"

# users = User("firstname","lastname","email","password")
# my_category = Categories("categoryname","recipename", "description")

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():   
    recipe_category = User.users_store[session['firstname']].categories
    return render_template('dashboard.html', recipe_category = recipe_category) 

@app.route("/signup", methods =["POST", "GET"])

def signup():

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        # new_user.signup(firstname,lastname,email,password)

        User.signup(firstname,lastname,email,password)

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/login", methods =["POST" , "GET"])

def login():
    if request.method == 'POST':
        firstname = request.form['firstname']
        password = request.form['password']
       
        # new_user.login(firstname, password)
        if User.login(firstname, password):
            session["firstname"] = firstname
                 
            return redirect(url_for('dashboard'))
        else:           
             return redirect(url_for('login'))
                
    return render_template('login.html')

@app.route("/logout", methods =["POST" , "GET"])

def logout():
    session.pop('username', None)
  
    return redirect(url_for('main'))

@app.route('/addcategories' , methods =['POST','GET'])
def addcategories():
        
    if 'firstname' not in session:
      
        return render_template('login.html')
    
    if request.method == 'POST':
        category_name = request.form['categoryname']

        category = Categories(category_name)
        session['category_name']= category_name
        User.users_store[category_name] = category
        return redirect(url_for('viewcategories'))

    return render_template('categories.html')
  

@app.route('/viewcategories')
def viewcategories():
    category_name = session['category_name']
    recipe_category = User.users_store
    return render_template('dashboard.html', recipe_category = recipe_category, category_name = category_name) 


@app.route('/deletecategories/<category_name>')
def deletecategories(category_name):
    User.users_store[session['firstname']].delete_category(category_name)
    
    return render_template('dashboard.html')

@app.route('/editcategories')
def editcategories():
    new_user = User(categories)
    new_user.delete_category(categories)

    return render_template('dashboard.html')


@app.route('/addrecipe', methods = ['POST','GET']) 
def addrecipe():

    if 'firstname' not in session: 

        return render_template('login.html')

    if 'categories' not in session: 

        return render_template('categories.html')
        firstname = [session['firstname']]
        category =  [session['category']]
   
    if request.method == 'POST':
        recipe_name = request.form['recipename']
        recipe_description = request.form['description']
        my_category.add_recipe(category,recipe_name,recipe_description)
        return redirect(url_for('viewrecipes'))

    return render_template('addrecipe.html')


@app.route('/viewrecipes', methods = ['POST', 'GET'])
def viewrecipes():  
    my_recipe = my_category.recipes
    return render_template('viewrecipes.html', my_recipe = my_recipe) 

    
if __name__=="__main__":
    app.run(debug=True)
    
    