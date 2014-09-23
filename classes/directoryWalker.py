import os

class DirectoryWalker :

  def __init__(self):
      pass

  def get_file_names(self, path):
    return self.__walk_directory__(path, True)

  def get_directory_names(self, path) :
    return self.__walk_directory__(path, False)

  def __walk_directory__(self, path, returnFiles, topdown_for_what=True) :
    names = []
    for root, dirs, files in os.walk(path, topdown=topdown_for_what) :
      if returnFiles :
        for name in files:
          names.append(os.path.join(os.path.abspath(root), name))
      else :
        for name in dirs:
          names.append(os.path.join(os.path.abspath(root), name))
    return names
