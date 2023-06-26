# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# CopyFCsToNewFD.py
# Version: 0.1
# Date: 2/21/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# gdb var needs to be configured in the tool
# This code  copies feature classes or shapefiles into a gdb in ArcGIS Pro

# Copies fcs or shapefiles from one folder into a feature dataset. The default name for the GDB is "Data".

#import libraries
import arcpy, os

# Set tool parameters and workspace
arcpy.env.overwriteOutput = True
ws = arcpy.GetParameterAsText(0)  # Set the workspace as a tool input parameter DataType = folder
gdb = "Data.gdb"  #GDB name DataType = string
outname = arcpy.GetParameterAsText(1) # String
outlocation = arcpy.GetParameterAsText(2)  #workspace
sr = arcpy.GetParameter(3)  # DataType = spatial reference
arcpy.env.workspace = ws

# Copy
arcpy.CreateFileGDB_management(outlocation, gdb)
arcpy.CreateFeatureDataset_management(gdb, outname, sr)
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fc_desc = arcpy.Describe(fc)
    if fc_desc.shapeType == "Polygon":
        newfc = os.path.join(gdb, outname, fc_desc.basename)
        arcpy.CopyFeatures_management(fc, newfc)

