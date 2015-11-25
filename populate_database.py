from hello import db, Menu

def create_menu():
    try:
        fall_menu = Menu('New England Fall 2015')
        db.session.add(fall_menu)
        db.session.commit()
    except Exception as e:
        print(e)

def create_menu_item():
    print "todo"
    #sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`gluten_free`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
    #print(sql)
    #cursor.execute(sql, ('SignatureSalad', 'TEST SALAD',  1111, 0, 1,  'a salad to use when testing the web application.'))

def count_menu_items():
    print "todo"
    #sql = "SELECT * FROM menu_items;"
    #cursor.execute(sql)
    #for row in cursor.fetchall():
    #    print(row)

create_menu()

#create_menu_item()

#count_menu_items()
