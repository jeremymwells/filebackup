import os

class FileFilter :

    def __init__(self):
        pass

    default_whitelist = ["*"]

    def extension_is_in_whitelist(self, extension):
        #for each extension in the self.filter array
        for ext in self.default_whitelist:
            if ext.lower() == extension or ext == "*" : return True
        return False

    def get_allowed_file_types(self, filenames):
        whitelist_files = []
        for name in filenames :
            n, file_ext = os.path.splitext(name)
            if self.extension_is_in_whitelist(file_ext) :
                whitelist_files.append(name)
        return whitelist_files