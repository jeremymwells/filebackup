from classes.directoryWalker import *
from classes.mediaItem import *
from classes.mediaFileFilter import *
from classes.fileWriter import *

source_directory = '.'
target_directory = './out'

def main():
    # get all files -->
    all_file_names = DirectoryWalker().get_file_names(source_directory)

    # filter out files we don't want -->
    filtered_names = FileFilter().get_allowed_file_types(all_file_names)

    fileWriter = FileWriter()

    #for all found files -->
    for name in filtered_names:
      fileWriter.copy_file(target_directory, MediaItem(name))

    return 0


if __name__ == "__main__":
    main()
