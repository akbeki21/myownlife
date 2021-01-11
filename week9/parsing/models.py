from peewee import *
from playhouse.mysql_ext import MySQLConnectorDatabase

user = 'begaiym'
password = 'Python8!'
db_name = 'deputy_db'


dbhandle = MySQLConnectorDatabase(
    db_name, user=user, password=password
)


class BaseModel(Model):
    class Meta:
        database = dbhandle

    
class Deputy(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=50)
    phone_number = CharField(max_length=30)


    class Meta:
        db_table = 'deputies'
        order_by = ('name')