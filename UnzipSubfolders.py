# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# unzipSubfolders.py
# Version: 0.1
# Date: 4/4/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Chooses a folder where subfolders are located and unzips the zips in the subfolders. The files will be unzipped to the
# their respective subfolders.
#BETA

# Set the extension to zip
import arcpy

extension = ".zip"

# Set the infolder as a text paramter for Pro tools
infolder = arcpy.GetParameterAsText(0)

# Unzip the tiles within each subfolder in the infolder
for root, dirs, files in os.walk(infolder):
    for item in files:
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(root, item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(root) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file