from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models import itinerary 
from flask_app.models import user 

@app.route('/create') 
def create_recipe(): 
    if not session['user_id']: 
        redirect('/home') 
    itinerary.Itinerary.save(request.form)
    return render_template('add_itinerary.html', current_user = user.User.getById({'id': session['user_id']}))

@app.route('/save/new/itinerary', methods=['post']) 
def save_new(): 
    if not session['user_id']: 
        return redirect('/home') 
    print("trying to save itinerary")
    if not itinerary.Itinerary.validate_create(request.form):
        return redirect('/create') 
    print('makes it here')
    itinerary.Itinerary.save(request.form) 
    return redirect('/home') 

@app.route('/review/itinerary/<int:post_id>')
def view_recipe(post_id):
    current_user = user.User.getById({'id': session['user_id']})
    output= itinerary.Itinerary.getById({'id': post_id})
    # output = [itinerary]

    return render_template('review_itinerary.html', current_user=current_user, itinerary=itinerary, output=output)


@app.route('/edit/itinerary/<int:post_id>')
def edit(post_id):
    return render_template('edit.html', itinerary = itinerary.Itinerary.getById({'id':post_id})) 

@app.route('/update', methods=['post'])
def update():
    if not session['user_id']:
        redirect('/home')
    if not itinerary.Itinerary.validate_create(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    itinerary.Itinerary.update(request.form)
    return redirect('/home')

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    itinerary.Itinerary.deleteById({'id':post_id})
    return redirect('/home')