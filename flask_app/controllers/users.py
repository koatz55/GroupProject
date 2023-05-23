from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
# from flask_app.models.guide import TV_Show
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

#Route renders the Login page
@app.route('/')
def tour_login():
    if 'users_id' in session:
        return redirect('/dash')

    return render_template('logguide.html')

@app.route('/register')
def tour_reg():
    if 'users_id' in session:
        return redirect('/dash')

    return render_template('regguide.html')

#Route validates login user
@app.route('/do_tour_login', methods=['POST'])
def tour_login_pro():
    data = { "email" : request.form["email"] }
    users_in = User.get_tour_users_email(data)
    
    if not users_in:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(users_in.password, request.form['password']):
        flash("Invalid Email/Password") 
        return redirect('/')
    session['users_id'] = users_in.id
    return redirect('/dash')

#Route validates registering user
@app.route('/do_tour_register', methods=['POST'])
def register_tour_check():
    if not User.validate_tour_users_reg(request.form):
        flash("Invalid Email/Password") 
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'].lower(),
        "last_name": request.form['last_name'].lower(),
        "email": request.form['email'].lower(),
        "password" : pw_hash
    }
    user_it = User.save_regt_users(data)
    session['users_id'] = user_it
    return redirect('/dash')

#Route logs out user
@app.route('/logout')
def logout_tourpage():
    session.clear()
    return redirect('/')