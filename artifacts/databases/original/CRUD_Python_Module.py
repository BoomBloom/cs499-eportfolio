from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Connection variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize the connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=aac' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

    def create(self, data):
        """Insert a document into the collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("An error occurred during insert:", e)
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, query):
        """Query for documents in the collection."""
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print("An error occurred during read:", e)
                return []
        else:
            raise ValueError("Query parameter is empty")
    def update(self, query, update_data):
        """Update documents matching query with the given update_data."""
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print("An error occurred during update:", e)
                return 0
        else:
            raise ValueError("Query and update_data parameters cannot be empty")

    def delete(self, query):
        """Delete documents matching query."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("An error occurred during delete:", e)
                return 0
        else:
            raise ValueError("Query parameter is empty")