from flask_app import app
from flask import render_template, redirect, session
from flask_app.models import user, itinerary

# @app.route('/home') 
# def dashboard():
#     if 'user_id' in session: 
#         return render_template('dashboard.html', 
#                         current_user = user.User.getById({'id': session['user_id']}), output = itinerary.Itinerary.get_all())
#     return redirect('/')

@app.route('/home') 
# route for home.
def dashboard():
    # when refernced we do the dashboard function
    if 'user_id' in session: 
        print('in session')
        # if user_id is not in session, logged out...
        return render_template('dashboard.html', 
                            #    return dahsbaord.html
                        current_user = user.User.getById({'id': session['user_id']}), output = itinerary.Itinerary.get_all())
    return redirect('/')