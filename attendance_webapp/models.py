from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import UserMixin, LoginManager 

#Database
db = SQLAlchemy()  

#Password
bcrypt = Bcrypt() 

#Redirect unauthorized users
login_manager = LoginManager()
login_manager.login_view = "app_blueprint.login"
 
#User class table
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(250), unique=True, nullable=False)
   email=db.Column(db.String(150), unique=True, nullable=False)
   password=db.Column(db.String(155), nullable=False)

#Table to store data about user attendance
class UserAttendance(db.Model):
   __tablename__ = 'user_attendance'

   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   name = db.Column(db.String(250), nullable=False)
   total_classes = db.Column(db.Integer, nullable=False)
   attended_classes = db.Column(db.Integer, nullable=False)

   user = db.relationship('User', backref=db.backref('subjects', lazy=True))

#Help flask_login get the user login details. 
@login_manager.user_loader
def load_user(user_id): 
   return User.query.get(int(user_id))