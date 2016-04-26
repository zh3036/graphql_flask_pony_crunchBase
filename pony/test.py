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



db.bind('mysql', host='', user='root', passwd='zh3036', db='pony_test',create_db=True)



