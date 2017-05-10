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

    # uncomment to filter out non-media files, and only keep [".mp4",".avi",".mp3",".mkv",".wav"] files -->
    # filtered_names = MediaFileFilter().get_allowed_file_types(filtered_names)

    fileWriter = FileWriter()

    #for all found files -->
    for name in filtered_names:
      media_item = MediaItem(name)
      fileWriter.copy_file(target_directory, media_item)
      fileWriter.write(target_directory, media_item)

    return 0


if __name__ == "__main__":
    main()
