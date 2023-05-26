from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user, itinerary, tour_guide
# from flask_app.models.guide import TV_Show
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

#Route renders the Login page
@app.route('/')
def tour_login():
    if 'users_id' in session:
        return redirect('/home')

    return render_template('logguide.html')

@app.route('/registerin')
def tour_reg():
    if 'users_id' in session:
        return redirect('/home')

    return render_template('regguide.html')

@app.route('/register', methods=['post'])
def register():
    print(request.form)
    if user.User.validate_create(request.form): 
        print(request.form['password']) 
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash) 
        data = { 
            'first_name': request.form['first_name'], 
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash 
        }
        session['user_id'] = user.User.save(data) 
        return redirect('/home')
    return redirect('/register')

@app.route('/login', methods=["POST"]) 
def login(): 
    data  = {"email" : request.form['email']} 
    user_in_db = user.User.getByEmail(data) 
    if user_in_db: 
        if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            session['user_id'] = user_in_db.id
            return redirect('/home')
    flash("Invalid Email/Password", 'loginError')
    return redirect('/')

@app.route('/home') 
# route for home.
def dashboard():
    # when refernced we do the dashboard function
    if 'user_id' in session: 
        print('in session')
    
        # if user_id is not in session, logged out...
        return render_template('dashboard.html', 
                            #    return dahsbaord.html
                        current_user = user.User.getById({'id': session['user_id']}), output = itinerary.Itinerary.get_all(), tgui = tour_guide.Tour.get_all_guides())

#Route validates login user
# @app.route('/do_tour_login', methods=['POST'])
# def tour_login_pro():
#     data = { "email" : request.form["email"] }
#     users_in = User.get_tour_users_email(data)
    
#     if not users_in:
#         flash("Invalid Email/Password")
#         return redirect('/')
#     if not bcrypt.check_password_hash(users_in.password, request.form['password']):
#         flash("Invalid Email/Password") 
#         return redirect('/')
#     session['users_id'] = users_in.id
#     return redirect('/dash')

#Route validates registering user
# @app.route('/do_tour_register', methods=['POST'])
# def register_tour_check():
#     if not User.validate_tour_users_reg(request.form):
#         flash("Invalid Email/Password") 
#         return redirect('/')
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)
#     data = {
#         "first_name": request.form['first_name'].lower(),
#         "last_name": request.form['last_name'].lower(),
#         "email": request.form['email'].lower(),
#         "password" : pw_hash
#     }
#     user_it = User.save_regt_users(data)
#     session['users_id'] = user_it
#     return redirect('/dash')

#Route logs out user
@app.route('/logout')
def logout_tourpage():
    session.clear()
    return redirect('/')