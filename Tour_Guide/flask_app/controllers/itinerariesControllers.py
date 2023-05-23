from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.itinerary import Itinerary 
from flask_app.models.user import User 

@app.route('/create') 
def create_recipe(): 
    if not session['user_id']: 
        redirect('/home') 
    Itinerary.save(request.form)
    return render_template('add_itinerary.html', current_user = User.getById({'id': session['user_id']}))

@app.route('/save/new/itinerary', methods=['post']) 
def save_new(): 
    if not session['user_id']: 
        return redirect('/home') 
    print("trying to save itinerary")
    if not Itinerary.validate_create(request.form):
        return redirect('/create') 
    print('makes it here')
    Itinerary.save(request.form) 
    return redirect('/home') 

@app.route('/review/itinerary/<int:post_id>')
def view_recipe(post_id):
    current_user = User.getById({'id': session['user_id']})
    itinerary = Itinerary.getById({'id': post_id})
    output = [itinerary]

    return render_template('review_itinerary.html', current_user=current_user, itinerary=itinerary, output=output)


@app.route('/edit/itinerary/<int:post_id>')
def edit(post_id):
    return render_template('edit.html', itinerary = Itinerary.getById({'id':post_id})) 

@app.route('/update', methods=['post'])
def update():
    if not session['user_id']:
        redirect('/home')
    if not Itinerary.validate_create(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    Itinerary.update(request.form)
    return redirect('/home')

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    Itinerary.deleteById({'id':post_id})
    return redirect('/home')