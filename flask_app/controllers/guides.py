from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
# from flask_app.models.guide import TV_Show
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

