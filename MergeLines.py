# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# MergePolygonShps.py
# Version: 0.1
# Date: 2/21/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This script will append shapefiles and feature classes from a folder to an new feature class.
# The new feature class is created using a feature from the input folder as its schema.
# The end result is a merged feature class.

#### DRAFT



# import libraries
import arcpy
import os

#Set workspace and parameters
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)  # Set the workspace as a tool input parameter DataType = workspace
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace
outName = arcpy.GetParameterAsText(2)  # DataType = string
template = arcpy.GetParameterAsText(3) # Datatype = feature class (or shp)
cs = arcpy.GetParameter(4)  # DataType = spatial reference
# Set variables for empty fc (you will use the first shp in the folder as a schema template)

#outName = ""
geomType = "LINE"
has_m = "DISABLED"
has_z = "DISABLED"
#proj = "WGS 1984 UTM Zone 16N.prj"
# template = "the first shapefile.shp"

# Create the empty fc
arcpy.AddMessage("Creating the empty feature class")
fc = arcpy.management.CreateFeatureclass(outgdb, outName
, geomType, template, has_m, has_z, cs)

# Create a list for shpfiles and fcs in the input workspace folder
featureList = arcpy.ListFeatureClasses()
#print(fileList)

# Append the parcel shapefiles to the new feature class
for feature in featureList:
    arcpy.AddMessage("Adding features to the new feature class")
    arcpy.management.Append(featureList, fc)