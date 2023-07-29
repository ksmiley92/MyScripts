# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# unzipFolders.py
# Version: 0.1
# Date: 4/4/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Unzips folders to a desired folder and then deletes the zipped files. The files will be unzipped to the
# same folder where they were are stored.
# This version is meant for an IDE, not a Pro tool. That version will be in the data management toolbox. 
#BETA

# import libraries
import zipfile
import os

# set the extension to .zip
import arcpy

extension = ".zip"

#infolder = arcpy.GetParameterAsText(0)   # parameter to use for tool in Pro
infolder = input("D:\Geodata\Elevation\LAS")
os.chdir(infolder) ##change directory from working dir to dir with files if needed

for item in os.listdir(infolder): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(infolder) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file