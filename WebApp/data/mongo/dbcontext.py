'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
import os
import pymongo

CONN_STR = ''


def get_db():
    client = pymongo.MongoClient(CONN_STR)
    return client.get_default_database()

def insert(collection, data, database=None):
    if database is None:
        database = get_db()
    database.DATABASE[collection].insert(data)

def find(collection, query):
    return Database.DATABASE[collection].find(query)

def find_one(collection, query):
    return Database.DATABASE[collection].find_one(query)

def update(collection, query, data):
    Database.DATABASE[collection].update(query, data, upsert=True)

def remove(collection, query):
    Database.DATABASE[collection].remove(query)