# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.2
# Date: 2/27/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code will read and copy tables to a gdb in ArcGIS Pro. It will search and extract the tables from folders
# of other datatypes
# Code needs editing to include a search string

# Import libraries
import arcpy
import os

#Set workspace and parameters
arcpy.env.overwriteOutput = True
workspace = arcpy.GetParameterAsText(0)  # DataType = folder
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace
featurename_strg = arcpy.GetParameterAsText(2)   # string to give a name for the title of the features (streets etc..)

# Copy the tables to the gdb
walk = arcpy.da.Walk(workspace, datatype = "Table")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if file.startswith("Logfile"):
            continue
        intable = os.path.join(dirpath, file)
        outtableName = featurename_strg + "_" + os.path.basename(dirpath) + "Table"  #"Parcels" + "_" +
        outtable = os.path.join(outgdb, outtableName)
        arcpy.management.CopyRows(intable, outtable)

