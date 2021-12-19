"""
This module is used for creating database BookStore,
"""

import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='Qazxsw101100!', auth_plugin='mysql_native_password')
cursor = db.cursor()
cursor.execute('CREATE DATABASE bookstore')

cursor.execute('SHOW DATABASES')

for db_ in cursor:
    print(db_)