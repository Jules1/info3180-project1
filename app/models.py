from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(80), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(6))
    biography = db.Column(db.String(300))
    image = db.Column(db.String(120))
    creation = db.Column(db.Date)

    def __repr__(self):
        return '<Profile %r %r %r %r %r %r>' % (self.username, self.first_name, self.last_name, self.age, self.sex, self.biography)
        
    def __init__(self,id,username,first_name,last_name,age,sex,biography,image,creation):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.biography = biography
        self.image = image
        self.creation = creation