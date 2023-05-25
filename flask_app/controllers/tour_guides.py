from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user
from flask_app.models import tour_guide
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 
from datetime import datetime

@app.route('/guide/<city>')
def view_guide(city):
    if 'user_id' not in session:
        return redirect('/logout')
    
    guide_detail = tour_guide.Tour.get_itnerary_with_tour({'city': city})
    print(guide_detail)
    return render_template('showguide.html', guide=guide_detail)

@app.route('/tour_guide')
def see_guides():
    tgui = tour_guide.Tour.get_all_guides()
    current_user = user.User.getById({'id': session['user_id']})
    return render_template('dashboard.html', tgui=tgui, current_user=current_user)


# @app.route('/recipes')
# def loginpan():
#     if 'user_id' not in session:
#         return redirect('/')
#     user_info = User.get_by_user_by_one({'id':session['user_id']})
#     print(user_info,"*"*20)
    
#     return render_template('allrecipes.html', user_info=user_info, recipes=Recipe.get_all_recipe())

# @app.route('/recipes/new')
# def add_recipes():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     return render_template('addrecipe.html')

# @app.route('/create/recipe', methods=['POST'])
# def pro_recipe():
#     if 'user_id' not in session:
#         print('Not logged in')
#         return redirect('/logout')
#     if not Recipe.validate_recipe(request.form):
#         print('Not vaild')
#         return redirect('/recipes/new')

#     data = {
#         'recipe_name': request.form['recipe_name'],
#         'description': request.form['description'],
#         'instruction': request.form['instruction'],
#         'date_made': request.form['date_made'],
#         'under': request.form['under'],
#         'user_id': session['user_id']
#     }
#     print(data,"*"*20)
#     Recipe.save_recipe(data)
#     return redirect('/recipes')

# @app.route('/recipes/<int:id>')
# def show_recipe(id):
#     if 'user_id' not in session:
#         print('Not logged in')
#         return redirect('/logout')
#     user_info = User.get_by_user_by_one({'id':session['user_id']})

#     return render_template('showrecipe.html', user_info=user_info, recipe=Recipe.get_users_with_recipe({'id': id}))

# @app.route('/recipes/edit/<int:id>')
# def edit_recipe(id):
#     if 'user_id' not in session:
#         return redirect('/logout')

#     return render_template('editrecipe.html', recipe=Recipe.get_users_with_recipe({'id': id}))

# @app.route('/recipes/edit/process/<int:id>', methods=['POST'])
# def pro_edit_recipe(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Recipe.validate_recipe_edit(request.form):
#         print('Not vaild')
#         return redirect(f'/recipes/edit/{id}')

#     data = {
#         'id': id,
#         'recipe_name': request.form['recipe_name'],
#         'description': request.form['recipe.description'],
#         'instruction': request.form['recipe.instruction'],
#         'date_made': request.form['date_made'],
#         'under': request.form['under']
#     }
#     Recipe.update(data)
#     return redirect('/recipes')

# @app.route('/recipes/destroy/<int:id>')
# def destroy_recipe(id):
#     if 'user_id' not in session:
#         return redirect('/logout')

#     Recipe.destroy({'id':id})
#     return redirect('/recipes')

# @app.route('/recipes/<int:id>')
# def new_date(self):
#     return render_template('showrecipe.html', new_date_time = datetime.strftime(self,'%B %-d %Y'))

# @app.route('/create/recipe', methods=['POST'])
# def recipe_one():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     # data = {'id': session['user_id']}
#     # recipe_on = User.get_by_user_id(data)
#     recipe_on = session['recipe_on']
#     # if not recipe_on:
#     #     return redirect('/logout')
#     return render_template('allrecipes.html', recipe_on=recipe_on, recipes=Recipe.get_users_with_recipe({'id': session['user_id']}))

# @app.route('/recipes')
# def show_recipes():
#     if 'user_id' not in session:
#         return redirect('/')
#     user = User.get_users_with_recipe({"id":session['user_id']})
#     # print(recipe_all,"*"*20)
#     # session['recipe_all'] = recipe_all
#     return render_template('allrecipes.html', user=user, recipe=Recipe.get_all_recipe)

# # @app.route('/recipe/new')
# # def read_one_id(id):
# #     recipe_in = User.get_user_by_id({'id':id})
# #     print(recipe_in)
# #     session['recipe_on'] = 'recipe_on'
# #     return render_template('addrecipe.html', recipe_in=recipe_in)

# @app.route('/users/<int:id>/new')
# def edit_one_id(id):
#     edited = User.get_user_by_id({'id':id})
#     return render_template('Edit.html', user=edited)

# @app.route('/users/<int:id>/updates', methods=['POST'])
# def edit_page_update(id):
#     data = {
#         'id': id,
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#     }
#     User.sho(data)
#     return redirect(f'/users/{id}')

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect('/user/login')
#     user = User.get_by_id({"id":session['user_id']})
#     # catch for invalid user_id somehow being in session, clear it via logout so user can login
#     if not user:
#         return redirect('/user/logout')     

#     return render_template('dashboard.html', user=user, recipes=Recipe.get_all_recipe())

# @app.route('/recipes/new')
# def create_recipe():
#     if 'user_id' not in session:
#         return redirect('/user/login')

#     return render_template('recipe_new.html')
