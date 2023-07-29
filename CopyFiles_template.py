# Copy a file from one place to another using a search by wildcard string
import os
import shutil

# specify the source directory and the search string
source_dir = "path/to/source/directory"
search_string = "*.txt"

# specify the destination directory
dest_dir = "path/to/destination/directory"

# loop through all files in the source directory that match the search string
for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, search_string):
        # construct the full path to the source file and destination file
        source_file = os.path.join(source_dir, file)
        dest_file = os.path.join(dest_dir, file)
        # copy the file to the destination directory
        shutil.copyfile(source_file, dest_file)