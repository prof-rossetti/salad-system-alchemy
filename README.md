# Salad System (SQLAlchemy Implementation)

An example database-connected web app,
 demonstrating object-relational mapping with the [Flask/ SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) Python library.

Represents a partial implementation of [Salad System Requirements](https://github.com/gwu-business/salad-system-requirements).

Based on [Salad System (Python Implementation)](https://github.com/prof-rossetti/salad-system-py)
 and [Salad System (Flask Implementation)](https://github.com/prof-rossetti/salad-system-flask).

## Usage

```` sh
git clone git@github.com:prof-rossetti/salad-system-alchemy.git
cd salad-system-alchemy/
````

Install package dependencies.

```` sh
pip3 install -r requirements.txt
````

Setup database (requires mysql).

```` sh
mysql -uroot -p -e "DROP DATABASE IF EXISTS salad_db; CREATE DATABASE salad_db;"
python3 data/migrate_database.py
python3 data/populate_database.py
````

Run local web server, and visit http://localhost:5000/ in a browser.

```` sh
python3 hello.py
````

![a screenshot depicting a menu page with an alert message at the top which reads: 'thanks for adding a menu item'](static/images/menu-screenshot.png)

## [License](LICENSE)
