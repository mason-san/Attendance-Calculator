from dotenv import load_dotenv
import os

#Loading variables from .env file 
load_dotenv()

class Config: 
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:////home/mazinmoosa/my_files/Attendance-Calculator/attendance_webapp/database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 