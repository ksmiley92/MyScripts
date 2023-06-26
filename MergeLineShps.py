# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# MergeLineShps.py
# Version: 0.1
# Date: 2/21/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This script will append shapefiles from a folder to an new feature class.
# The new feature class is created using a feature from the input folder as its schema.
# The end result is a merged feature class.




# import libraries
import arcpy
import os

#Set workspace and parameters
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)  # Set the workspace as a tool input parameter DataType = folder
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace
outName = arcpy.GetParameterAsText(2)  # DataType = string
template = arcpy.GetParameterAsText(3) # Datatype = feature class (or shp)

# Set variables for empty fc (you will use the first shp in the folder as a schema template)
#outName = "tn_parcels"
geomType = "LINE"
# template = "the first shapefile.shp"

# Create the empty fc
arcpy.AddMessage("Creating the empty feature class")
fc = arcpy.management.CreateFeatureclass(outgdb, outName
, geomType, template)

# Create a list for shpfiles in the input workspace folder
shpList = arcpy.ListFiles()
#print(shpList)

# Append the shapefiles to the new feature class
arcpy.AddMessage("Adding features to the new feature class")
arcpy.management.Append(shpList, fc)