from pony.orm import *
import pymysql

sql_debug(True)

db = Database()

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set("Car")
class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)



db.bind('mysql', host='', user='root', passwd='zh3036', db='pony_test')

db.generate_mapping(create_tables=True)


with db_session:
	p1 = Person(name='John', age=20)
	p2 = Person(name='Mary', age=22)
	p3 = Person(name='Bob', age=30)
	c1 = Car(make='Toyota', model='Prius', owner=p2)
	c2 = Car(make='Ford', model='Explorer', owner=p3)
	# commit()

