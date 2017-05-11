
import hachoir_core
import hachoir_core.cmd_line
import hachoir_metadata
import hachoir_parser
import sys

class FileMetaData :

  def get(self, filename):
      
      returnMeta = None
      filename, realname = hachoir_core.cmd_line.unicodeFilename(filename), filename
      parser = hachoir_parser.createParser(filename, realname)
      
      if not parser:
          print >> sys.stderr, "Unable to parse file"
          return returnMeta
      
      try:
          metadata = hachoir_metadata.extractMetadata(parser)
      except HachoirError, err:
          print "Metadata extraction error: %s" % unicode(err)
          
      if not metadata:
          print >> sys.stderr, "Unable to extract metadata"
          return returnMeta

      returnMeta = metadata

      # do something with metadata if null/None ?
      return returnMeta


