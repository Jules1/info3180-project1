"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, time, json

from app import app, db
from app.models import UserProfile
from flask import render_template, request, redirect, url_for, flash,jsonify
from wtforms import TextAreaField, TextField, IntegerField, SelectField, validators, Form


class profileForm(Form):
    username = TextField('username', [validators.Required()])
    first_name = TextField('first_name', [validators.Required()])
    last_name = TextField('last_name', [validators.Required()])
    age = IntegerField('age', [validators.Required()])
    sex = SelectField('sex',choices=[('male', 'Male'), ('female','Female')])
    biography = TextAreaField('Biography',[validators.Required()])

def date():
    return time.strftime("%m %d %Y")

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=('GET', 'POST'))
def addProf():
    form = profileForm(csrf_enables=False)  
    file_folder = app.config['UPLOAD_FOLDER']
    
    if request.method == 'POST':
        if form.validate():
            username = request.form['username']
            firstname = request.form['first_name']
            lastname = request.form['last_name']
            age = request.form['age']
            sex = request.form['sex']
            biography = request.form['biography']
            image = request.form['image']
            creation = date()
            newprofile = UserProfile(id,username,firstname,lastname,age,sex,biography,image,creation)
            db.session.add(newprofile)
            db.session.commit()
        addSuccess()
    return render_template('profile.html', form=form)

def addSuccess():
    flash('New user has been successfully added!', 'success')
    
@app.route('/failure')
def failure():
    return render_template('failure.html')
    
@app.route('/profiles', methods=["GET", "POST"])
def profiles():
    profList = []
    if request.method=="POST":
        profs = db.session.query(UserProfile).all()
        for prof in profs:
            profInfo = {'username':prof.username, 'userid':prof.id}
            profList.append(profInfo)
        return jsonify(profList)
    
@app.route("/profile/<userid>", methods=["GET","POST"])
def viewProf(userid):
    return render_template('viewprofile.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
