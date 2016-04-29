
#flask_pony_graphene_crunchbase2013

a graphql api to query data from crunch base

##libraries

http://graphene-python.org/

http://flask.pocoo.org

https://ponyorm.com/


##data_set
https://data.crunchbase.com/v3/docs/2013-snapshot



##文件描述

###orm
pony orm 定义在 pony/learn pony.ipy 这个ipython notebook里，里边还有个转换mysql creatable成pony class的function。这个orm的定义有一个问题就是直接assume了index 类型 （p:11 f:11） 这个问题应该很好解决，只需要还原成object_id然后给每个class加method 来操作就好

###flask+graphiql
这个就是根目录的app.py 是flask。 schema.py 是定义了一个简单的schema。
之后应该return的时候就做对orm做query

### flask_pony_graphene
这个是python的一个virtualenv，可以使用这个来运行这些东西