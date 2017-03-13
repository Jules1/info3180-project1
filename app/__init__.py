from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "SneakyBeaky"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user1:password@localhost/UserProfile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['ALLOWED_EXTENSIONS'] = "set(['jpg', 'png','gif', 'jpeg'])"
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)
from app import views