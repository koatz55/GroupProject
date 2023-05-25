from flask_app.config.mysqlconnection import connectToMySQL 
mydb = 'tour_guide'
from flask_app.models.user import User 
from flask import flash 

class Itinerary: 
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.city = data['city'] 
        self.trip_details = data['trip_details'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.guide_id = data['guide_id']
        self.creator = None

    @staticmethod 
    def validate_create(request):
        is_valid = True 
        if len(request['first_name']) < 2: 
            flash('First name must be longer than 2 Characters')
            is_valid = False 
        if len(request['last_name']) <2: 
            flash('Last name Must Be Longer Than 2 Characters')
            is_valid = False 
        if len(request['city']) <2: 
            flash('city name Must Be Longer Than 2 Characters')
            is_valid = False 
        if len(request['trip_details']) < 1:
            flash('tripe details must be at least 1 characters') 
            is_valid = False 
        return is_valid 

    
    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO itineraries
        (first_name, last_name, city, trip_details, user_id)
        VALUES (%(first_name)s, %(first_name)s, %(city)s,%(trip_details)s, %(user_id)s);'''
        results = connectToMySQL(mydb).query_db(query,data) 
        print(f"results: {results}") 
        return results

    @classmethod
    def deleteById(cls,data):
        query  = '''
        DELETE FROM itineraries
        WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        return results
    
    @classmethod
    def update(cls, data):
        query = '''
        UPDATE itineraries
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        trip_details = %(trip_details)s,
        city = %(city)s
        WHERE id = %(id)s;'''
        return connectToMySQL(mydb).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM itineraries LEFT JOIN users ON users.id = itineraries.user_id;"
        results = connectToMySQL(mydb).query_db(query)
        # print(results)
        # recipes = []
        lst = []
        for i in results: 
            # this_recipe =cls(i)
            obj = cls(i)
            # this_recipe_creator = {
            temp = { 
                'id':i['users.id'], # get  their id
                'first_name':i['first_name'], # first name 
                'last_name':i['last_name'], # last name
                'email':i['email'], # email
                'password':i['password'], #password
                'created_at':i['users.created_at'], #created at
                'updated_at':i['users.updated_at'], #updated at
            }
            # this_recipe.creator= User(this_recipe_creator)
            # obj.creator= User(this_recipe_creator)
            obj.creator= User(temp) #the creator is set to equal the temp for every user. so, if gisselle is a user so is also the creator 
            # recipes.append(this_recipe)
            lst.append(obj) # we add the user to out lst array
        # return recipes
        return lst # return the lst which is essentionally all

    @classmethod 
    def getById(cls,data): 
        print(data) 
        query = '''
        SELECT * FROM itineraries 
        LEFT JOIN users ON users.id = itineraries.user_id
        WHERE itineraries .id = %(id)s;'''
        results = connectToMySQL(mydb).query_db(query,data)
        print(f"results: {results}") 
        this_itinerary =cls(results[0]) 
        this_itinerary_creator = {
            'id':results[0]['users.id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'password':results[0]['password'],
            'created_at':results[0]['users.created_at'],
            'updated_at':results[0]['users.updated_at'],
            }
        this_itinerary.creator= User(this_itinerary_creator)
        return this_itinerary