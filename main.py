from classes.directoryWalker import *
from classes.mongoConnector import *
from classes.mediaItem import *
from classes.mediaFileFilter import *

def main() :

  all_file_names = DirectoryWalker().get_file_names('.')
  filtered_names = FileFilter().get_allowed_file_types(all_file_names)

  mongo = MongoConnector()
  
  for name in filtered_names :
    media_item_dict = MediaItem(name).to_dict()
    print mongo.add_media(media_item_dict)

  return 0

if __name__ == "__main__":
  main()
