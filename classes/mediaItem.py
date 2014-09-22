import os

class MediaItem :

  def __init__(self, fullfilename) :
    self.full_name = fullfilename
    n, self.extension = os.path.splitext(fullfilename)
    self.name = os.path.basename(n)

  def to_dict(self):
    return self.__dict__