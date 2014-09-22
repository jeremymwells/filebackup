from pymongo import MongoClient


class MongoConnector :

  def __init__(self) :
    self.client = MongoClient('localhost', 27017)
    self.db = self.client.test_database
    self.mediaCollection = self.db.media
    #clears all media collection items-->
    self.mediaCollection.remove({ 'name' : { '$ne': '' }})

  #@returns the newly created document id
  def add_media(self, m) :
    return self.mediaCollection.insert(m)

  def get_media_by_name(self, name) :
    return self.mediaCollection.find({"name": name});
