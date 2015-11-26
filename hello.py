import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
import os
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
from flask_sqlalchemy import SQLAlchemy

#
# INITIALIZE AND CONFIGURE NEW FLASK APPLICATION
#

try:
    DB_ROOT_PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"] # if your root user has a password, assign it to the "MYSQL_ROOT_PASSWORD" environment variable
except KeyError as e:
    DB_ROOT_PASSWORD = "" # most students' root user doesn't have a password

DATABASE_CONNECTION_STRING = "mysql://root:%s@localhost/salad_db" % DB_ROOT_PASSWORD # should be like: 'mysql://username:password@server/db' ... http://flask-sqlalchemy.pocoo.org/2.1/config/?highlight=mysql

app = Flask(__name__)
app.secret_key = os.urandom(24) # to facilitate sessions and flash
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#
# DEFINE MODELS
#

class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Menu %r>' % self.title

class MenuItem(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    gluten_free = db.Column(db.Boolean)
    vegan_safe = db.Column(db.Boolean)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, options):
        self.category = options["category"]
        self.title = options["title"]
        self.calories = options["calories"]
        self.gluten_free = options["gluten_free"]
        self.vegan_safe = options["vegan_safe"]
        self.description = options["description"]

    def __repr__(self):
        return '<MenuItem %r>' % self.title

#
# DEFINE HELPER METHODS
#

def rollback_and_print(error):
    print("ERROR --> %s" % (error.message))
    db.session.rollback() # to avoid sqlalchemy.exc.InvalidRequestError

#
# DEFINE ROUTES
#

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/menu")
def menu_items():
    menu_items =  MenuItem.query.order_by(MenuItem.id.desc()).limit(10)
    return render_template('menu-items/index.html', menu_items=menu_items)

@app.route("/form")
def edit_menu_item():
    return render_template('menu-items/form.html')

@app.route("/new", methods=['POST'])
def new_menu_item():

    # CAPTURE, VALIDATE, AND TRANSFORM FORM DATA

    try:
        calories = int(request.form['calories'])
    except ValueError as e:
        flash('Please specify number of calories.') # A VALIDATION!
        return redirect(url_for('edit_menu_item')) #todo: retain previous form input values instead of resetting the form state

    try:
        gluten_free = True if request.form['gluten_free'] else False
    except KeyError as e:
        gluten_free = False

    try:
        vegan_safe = True if request.form['vegan_safe'] else False
    except KeyError as e:
        vegan_safe = False

    menu_item = MenuItem({
        "category": request.form['category'],
        "title": request.form['title'],
        "calories": calories,
        "gluten_free": int(gluten_free),
        "vegan_safe": int(vegan_safe),
        "description": request.form['description']
    })

    # CREATE NEW RECORD

    try:
        db.session.add(menu_item)
        db.session.commit()
    except Exception as e:
        flash('Please revise form inputs -- %s' % e.message)
        return redirect(url_for('edit_menu_item'))

    # REDIRECT WITH AN ALERT MESSAGE

    flash('Thanks for adding a menu item -- %s.' % menu_item.title)
    return redirect(url_for('menu_items'))

#
# START LOCAL WEB SERVER WHEN THIS SCRIPT IS EXECUTED
#

if __name__ == "__main__":
    app.debug = True
    app.run()
