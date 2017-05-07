## To run...

- python -B main.py
    - (-B prevents .pyc files from being generated)

## How to use...

In `main.py`, there are 2 variables `source_directory`, and `target_directory`. Change those to the directory where your files are, and where you'd like them to go. This will not move files; it copies files.

By default, they are:
```
source_directory = '.'
target_directory = './out'
```

Files found in `source_directory` will be copied to `target_directory` such that an os-safe version of the filename will be used for the directory name, as a subdir in `target_directory`.

So, for example if we had:
```
# source directory -->

/
|-- main.py
|-- /classes
|   |-- directoryWalker.py
|   |-- fileFilter.py

```

You would end up with:
```
# target directory-->

/
|-- /main
|   |-- main.py
|-- /directoryWalker
|   |-- directoryWalker.py
|-- /fileFilter
|   |-- fileFilter.py
```
