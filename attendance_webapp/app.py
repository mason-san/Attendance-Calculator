from flask import Flask
from config import Config
from models import db, bcrypt, login_manager
from routes import app_blueprint

app = Flask(__name__)

#Load configuration from config.py
app.config.from_object(Config) 

db.init_app(app) #Initiazlie the database. 
bcrypt.init_app(app) #init password hashing.
login_manager.init_app(app) #init login_manager.

app.register_blueprint(app_blueprint) #init blueprint so that routes are registerd. 

if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all() # Create teh tables if the don't exist. 
    app.run(debug=True) #Running the