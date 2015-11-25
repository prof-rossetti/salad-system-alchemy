# Salad System (SQL-Alchemy Implementation)

An example database-connected web app,
 demonstrating object-relational mapping with the [Flask/ SQL Alchemy](http://flask-sqlalchemy.pocoo.org/2.1/) Python library.

Represents a partial implementation of [Salad System Requirements](https://github.com/gwu-business/salad-system-requirements).

Based on [Salad System (Python Implementation)](https://github.com/gwu-business/salad-system-py)
 and [Salad System (Flask Implementation)](https://github.com/gwu-business/salad-system-flask).

## Usage

```` sh
git clone git@github.com:gwu-business/salad-system-alchemy.git
cd salad-system-alchemy/
````

Install package dependencies.

```` sh
pip install -r requirements.txt
````

Setup database (requires mysql).

```` sh
mysql -uroot -p -e "DROP DATABASE IF EXISTS salad_db; CREATE DATABASE salad_db;"
python migrate_database.py
python populate_database.py
````

Run local web server, and visit http://localhost:5000/ in a browser.

```` sh
python hello.py
````

![a screenshot depicting a menu page with an alert message at the top which reads: 'thanks for adding a menu item'](static/images/menu-screenshot.png)

## [License](LICENCE)
