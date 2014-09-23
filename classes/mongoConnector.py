from pymongo import MongoClient


class MongoConnector:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.test_database
        self.media_collection = self.db.media
        # clears all media collection items-->
        self.media_collection.remove({'name': {'$ne': ''}})

    # @returns the newly created document id
    def add_media(self, m):
        return self.media_collection.insert(m)

    def get_media_by_name(self, name):
        return self.media_collection.find({"name": name});
