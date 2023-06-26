hb# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# CopyFCsToNewFD.py
# Version: 0.1
# Date: 2/27/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# This code  copies feature classes or shapefiles into a gdb in ArcGIS Pro by searching for a string that they
# begin with


# Import libraries
import arcpy
import os

# Set workspace parameters
arcpy.env.overwriteOutput = True
workspace = arcpy.GetParameterAsText(0)  # DataType = folder
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace
searchstrg = arcpy.GetParameterAsText(2)  # DataType = string

# Copy fcs or shapefiles that start with "Parcels" into a gdb from subdirectories
walk = arcpy.da.Walk(workspace, datatype = "FeatureClass")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if not file.startswith(searchstrg):
            continue
        infc = os.path.join(dirpath, file)
        outfcname = os.path.basename(file).split(".")[0] + "_" + os.path.basename(dirpath)
        outfc = os.path.join(outgdb, outfcname)
        arcpy.management.CopyFeatures(infc, outfc)
