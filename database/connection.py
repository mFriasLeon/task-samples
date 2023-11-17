"""Naralabs task: Managing samples.

In the database folder you will have the file that will make the connection
with the database and create a new one called Naralabs. 
For all this you will use pymongo
"""


from pymongo import MongoClient

#url path
URL_CONNECTION = "mongodb://127.0.0.1:27017/mongodb"
# connection
db_connection = MongoClient(URL_CONNECTION)
# create a new database
naralabs_db = db_connection["naralabs"]

