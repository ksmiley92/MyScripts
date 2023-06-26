# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.2
# Date: 8/22/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code will read and copy parcels tables to a file gdb for each.

#Do the same, but for tables
# Edit code to exclude the Logfile and rename with same name as Parcels features.

# Import libraries
import arcpy
import os

#Set workspace and parameters
arcpy.env.overwriteOutput = True
workspace = arcpy.GetParameterAsText(0)  # DataType = folder
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace

# Copy the tables to the gdb
walk = arcpy.da.Walk(workspace, datatype = "Table")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if file.startswith("Logfile"):
            continue
        intable = os.path.join(dirpath, file)
        outtableName = "Parcels" + "_" + os.path.basename(dirpath) + "Table"
        outtable = os.path.join(outgdb, outtableName)
        arcpy.management.CopyRows(intable, outtable)

