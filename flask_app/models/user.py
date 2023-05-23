from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models import itinerary
from flask_app.models import guide

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = 'tour_guide'

    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    #Method inserts register user information into database
    @classmethod
    def save_regt_users(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query,data)

    #Method gets user from database by id 
    @classmethod
    def get_tour_users_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if result:
            return cls(result[0])
        return False

    #Method gets user from database by email 
    @classmethod
    def get_tour_users_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    #Method that validates user registration 
    @staticmethod
    def validate_tour_users_reg(user):
        is_valid = True 
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(user['email']) < 2:
            flash("Email cannot be blank. At least 2 characters")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if len(user['email']) < 2:
            flash("Email must be at least 2 characters.")
            is_valid = False 
        if user['password'] != user['confirm_password']:
            flash("Password does not match")
            is_valid = False
        return is_valid
