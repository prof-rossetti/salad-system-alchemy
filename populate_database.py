import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
from hello import db, Menu, MenuItem, rollback_and_print

def create_menu():
    try:
        fall_menu = Menu('New England Fall 2015')
        db.session.add(fall_menu)
        db.session.commit()
    except Exception as e:
        rollback_and_print(e)

def create_menu_items():
    menu_items = [
        {
            "category": 'SignatureSalad',
            "title": 'TEST SALAD',
            "calories": 1111,
            "gluten_free": 0,
            "vegan_safe": 1,
            "description": 'a salad to use when testing the web application.'
        },
        {
            "category": 'SeasonalSalad',
            "title": 'KALE YEAH',
            "calories": 540,
            "gluten_free": 0,
            "vegan_safe": 1,
            "description": 'a kale-based salad.'
        },
        {
            "category": 'SignatureGrain',
            "title": 'NEWTON',
            "calories": 720,
            "gluten_free": 1,
            "vegan_safe": 0,
            "description": 'a fall salad with apples.'
        }
    ]

    for menu_item_attribute_dict in menu_items:
        menu_item = MenuItem(menu_item_attribute_dict)
        try:
            db.session.add(menu_item)
            db.session.commit()
        except Exception as e:
            rollback_and_print(e)

def count_menu_items():
    menu_item_count = MenuItem.query.count()
    print("THERE ARE %s MENU ITEMS IN THE DATABASE" % menu_item_count)

create_menu()

create_menu_items()

count_menu_items()
