# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# MakeFolders_template.py
# Version: 0.1
# Date: 3/2/23
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code will use the os module to create folders on the computer. Creates subfolders in folders.
# Can be edited to do different things.

# This one will create folders within existing folders in a folder
# Try on only the first one (either create or remove, the code for both is here)
import os

# specify the path to the directory
directory_path = r"C:\TN_Compliance_Review_2023\Docs\FinalMaps\2023"

# get the first subdirectory in the specified directory
subdirs = [os.path.join(directory_path, d) for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
if len(subdirs) > 0:
    first_subdir = subdirs[0]
    # create a new folder within the first subdirectory
    new_folder = os.path.join(first_subdir, "Employee Tracts")
    if os.path.exists(new_folder):
        raise ValueError(f"Folder {new_folder} already exists")
    os.makedirs(new_folder)
    #if os.path.exists(new_folder):
        #os.rmdir(new_folder)


## Now use this code to do all folders
import os

# specify the path to the directory
directory_path = r"C:\TN_Compliance_Review_2023\Docs\FinalMaps\2023"

# loop through all subdirectories in the specified directory
for subdir in os.listdir(directory_path):
    # check if the item is a subdirectory
    if os.path.isdir(os.path.join(directory_path, subdir)):
        # create a new folder within the subdirectory
        new_folder = os.path.join(directory_path, subdir, "Customer Tracts")
        if os.path.exists(new_folder):
            raise ValueError(f"Folder {new_folder} already exists")
        os.makedirs(new_folder)

##Remove a directory
import os

# specify the path to the directory
directory_path = r"C:\TN_Compliance_Review_2023\Docs\FinalMaps\2023"

# loop through all subdirectories in the specified directory
for subdir in os.listdir(directory_path):
    # check if the item is a subdirectory
    if os.path.isdir(os.path.join(directory_path, subdir)):
        # create a new folder within the subdirectory
        new_folder = os.path.join(directory_path, subdir, "Employee Tracts")
        if os.path.exists(new_folder):
            os.rmdir(new_folder)

## Create a new folder(s) in a directory and then make folders inside (subfolders)
import os
path = r"folder_path"   #may need to change if it doens't work with the path2 variable
for i in range(1,11):  #makes 10 folders but can be changed
    os.chdir(path)
    new_folder = 'folder name' + str(i)
    try:
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        # to make folders inside other folders
        path2 = path + '\\' + new_folder
        os.chdir(path2)
        for j in range(1,3):
            new_folder2 = 'test' + str(j)
            os.makedirs(new_folder2)
    except OSError:
        print('Error: Directory already exists, change the new folder name')
