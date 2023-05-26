from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re 
from flask_app.models import user
from flask_app.models import itinerary



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


class Tour:
    mydb = 'tour_guide'
    def __init__(self,data): 
        self.id = data['id'] 
        self.city = data['city'] 
        self.img_path = data['img_path'] 
        self.tour_guide_descr = data['tour_guide_descr']
        self.yourguide = []
        self.adminguide = None



    @classmethod 
    def getByEmail(cls,data):
        print(data) 
        query = '''
        SELECT * FROM guides
        WHERE city = %(email)s;''' 
        results = connectToMySQL(cls.mydb).query_db(query,data)
        print(f"results: {results}") 
        if len(results) < 1: 
            return False 
        return cls(results[0])


    @classmethod
    def get_itnerary_with_tour(cls,data):
        query = """
                SELECT * FROM guides LEFT JOIN itineraries ON guides.city = itineraries.city WHERE guides.city = %(city)s;
                """
        result = connectToMySQL(cls.mydb).query_db(query,data)

        if not result:
            return None

        guide_result = cls(result[0])
        descr_data = {
                "id": result[0]['itineraries.id'],
                "first_name": result[0]['itineraries.first_name'],
                "last_name": result[0]['itineraries.last_name'],
                "city": result[0]['itineraries.city'],
                "trip_details": result[0]['trip_details'],
                "created_at": result[0]['itineraries.created_at'],
                "updated_at": result[0]['itineraries.updated_at'],
                "user_id": result[0]['user_id'],
                "guide_id": result[0]['guide_id']
            }
        guide_result.adminguide = itinerary.Itinerary(descr_data)
        return guide_result 
    
    @classmethod
    def get_all_guides(cls):
        query = "SELECT * FROM guides;"
        results = connectToMySQL(cls.mydb).query_db(query)
        gui = []
        for guide in results:
            gui.append( cls(guide) )
        return gui