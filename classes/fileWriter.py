import os
from shutil import copyfile

default_genre = "concert"

class FileWriter :

  def __init__(self):
      pass

  def copy_file(self, target_directory, media_item) :
    media_item_dictionary = media_item.to_dict()
    containing_directory, filename_directory, filename = self.get_directories_and_name(target_directory, media_item_dictionary)
    print 'containing dir: ' + containing_directory
    print 'filename dir: ' + filename_directory
    print 'filename: ' + filename
    self.create_directory_if_not_exist(containing_directory)
    self.create_directory_if_not_exist(filename_directory)
    try :
      copyfile(media_item_dictionary['full_name'], os.path.join(os.path.abspath(containing_directory), filename_directory, filename))
    except Exception as e:
      print "there was a problem writing [{0}].\n\t-{1}".format(filename, e)
      pass

  def get_directories_and_name(self, target_directory, media_item_dictionary) :
    main_output_dir = os.path.join(os.path.abspath(target_directory))
    new_output_dir = os.path.join(main_output_dir, self.scrub_file_name(media_item_dictionary['name']))
    filename = "{0}{1}".format(media_item_dictionary['name'],media_item_dictionary['extension'])
    return main_output_dir, new_output_dir, filename

  def scrub_file_name(self, filename) :
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()

  def create_directory_if_not_exist(self, directory) :
    if not os.path.exists(directory):
      try :
        os.makedirs(directory)
      except Exception:
        print "there was a problem creating the {0} directory".format(directory)
        pass

  def write(self, target_directory, media_item) :
    media_item_dictionary = media_item.to_dict()
    containing_directory, filename_directory, filename = self.get_directories_and_name(target_directory, media_item_dictionary)
    targetFilename = "{0}.nfo".format(media_item_dictionary['name'])
    path = None
    try :
      path = os.path.join(os.path.abspath(containing_directory), filename_directory, targetFilename)
      target = open(path, 'w')
      target.write(
        """
<movie>
  <title>{0}</title>
  <genre>{1}</genre>
</movie>
        """.format(filename, default_genre)
      )
      target.close()
    except Exception as e:
      print "there was a problem writing [{0}].\n\t-{1}".format(path, e)
      passc
    

