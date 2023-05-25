from flask_app import app
from flask_app.controllers import users, itineraries, tour_guides
# we also import our controllers to that they may connect to the server.


if __name__=="__main__":
    app.run(debug=True)