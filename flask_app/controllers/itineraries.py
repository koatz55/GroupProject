from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
# from flask_app.models.guide import TV_Show
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



@app.route('/dash')
def logintourpro():
    if 'users_id' not in session:
        return redirect('/logout')
    
    user = User.get_tour_users_id({'id':session['users_id']})
    return render_template('dashboard.html', user=user)