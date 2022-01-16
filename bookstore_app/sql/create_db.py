"""
This module is used for creating database BookStore,
"""


import os
import mysql.connector

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
server = os.environ.get('MYSQL_SERVER')
database = os.environ.get('MYSQL_DATABASE')




db = mysql.connector.connect(host=server, user=user, passwd=password, auth_plugin='mysql_native_password')
cursor = db.cursor()
cursor.execute('CREATE DATABASE bookstore')

cursor.execute('SHOW DATABASES')

for db_ in cursor:
    print(db_)



