from flask_app import app # this gets imported
from flask_app.controllers import itinerariesControllers, usersControllers, login_regControllers
# we also import our controllers to that they may connect to the server.


if __name__=="__main__":
    app.run(port=5001, debug=True)