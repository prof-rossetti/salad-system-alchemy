from hello import db, Menu, MenuItem, code # debug with code.interact(local=dict(globals(), **locals()))

def create_menu():
    try:
        fall_menu = Menu('New England Fall 2015')
        db.session.add(fall_menu)
        db.session.commit()
    except Exception as e:
        print(e)

def create_menu_items():
    try:
        kale_yeah = MenuItem(   'SeasonalSalad',  'KALE YEAH',  540, 0, 1,   'a kale-based salad.')
        newton = MenuItem(      'SignatureGrain', 'NEWTON',     720, 1, 0,   'quinoa + farro, organic arugula, tomatoes, raw corn, organic chickpeas, spicy broccoli, organic white cheddar, roasted chicken, pesto vinaigrette.')
        #test_salad = MenuItem(  'SignatureSalad', 'TEST SALAD', 1111, 0, 1,  'a salad to use when testing the web application.')
        for menu_item in [kale_yeah, newton]:
            db.session.add(menu_item)
            db.session.commit()
    except Exception as e:
        print(e)

def count_menu_items():
    menu_item_count = MenuItem.query.count()
    print("THERE ARE %s MENU ITEMS IN THE DATABASE" % menu_item_count)

create_menu()

create_menu_items()

count_menu_items()
