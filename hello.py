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
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Menu %r>' % self.title




#db.create_all()
#fall_menu = Menu('New England Fall 2015')
#db.session.add(admin)
#db.session.commit()








####
#### DEFINE ROUTES
####
###
###@app.route("/")
###def hello():
###    return render_template('index.html')
###
###@app.route("/menu")
###def menu_items():
###    ###cursor = mysql.connect().cursor()
###    ###cursor.execute("SELECT * from menu_items ORDER BY id DESC LIMIT 10;")
###    ###menu_items = [
###    ###    dict(
###    ###        id= row[0],
###    ###        category=row[1],
###    ###        title=row[2],
###    ###        calories=row[3],
###    ###        gluten_free=row[4],
###    ###        vegan_safe=row[5],
###    ###        description=row[6]
###    ###    ) for row in cursor.fetchall()
###    ###]
###    ###return render_template('menu-items/index.html', menu_items=menu_items)
###
###@app.route("/form")
###def edit_menu_item():
###    return render_template('menu-items/form.html')
###
###@app.route("/new", methods=['POST'])
###def new_menu_item():
###
###    # CAPTURE, VALIDATE, AND TRANSFORM FORM DATA
###
###    category = request.form['category']
###    title = request.form['title']
###    description = request.form['description']
###
###    try:
###        calories = request.form['calories']
###        calories = int(calories)
###    except ValueError as e:
###        #calories = None
###        flash('Please specify number of calories.') # A VALIDATION!
###        return redirect(url_for('edit_menu_item')) #todo: retain previous form input values instead of resetting the form state
###
###    try:
###        gluten_free = True if request.form['gluten_free'] else False
###    except KeyError as e:
###        gluten_free = False
###    finally:
###        gluten_free = int(gluten_free)
###
###    try:
###        vegan_safe = True if request.form['vegan_safe'] else False
###    except KeyError as e:
###        vegan_safe = False
###    finally:
###        vegan_safe = int(vegan_safe)
###
###    # CREATE NEW RECORD
###
###    ###connection = mysql.connect()
###    ###cursor = connection.cursor()
###    ###sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`gluten_free`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
###    ###cursor.execute(sql, (category, title, calories, gluten_free, vegan_safe, description))
###    ###connection.commit()
###
###    # REDIRECT WITH AN ALERT MESSAGE
###
###    flash('Thanks for adding a menu item.')
###    return redirect(url_for('menu_items'))
###
####
#### START LOCAL WEB SERVER WHEN THIS SCRIPT IS EXECUTED
####
###
###if __name__ == "__main__":
###    app.debug = True
###    app.run()
###
