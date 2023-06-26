# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.1
# Date: 8/22/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This script will append parcel shapefiles from a folder to an new feature class. The end result is a merged parcel feature class for a whole state.




# import libraries
import arcpy
import os

#Set workspace and parameters
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)  # Set the workspace as a tool input parameter DataType = folder
outgdb = arcpy.GetParameterAsText(1)  # DataType = workspace
outName = arcpy.GetParameterAsText(2)  # DataType = string
template = arcpy.GetParameterAsText(3) # Datatype = .shp

# Set variables for empty fc (you will use the first shp in the folder as a schema template)
#outName = "tn_parcels"
geomType = "POLYGON"
# template = "the first shapefile.shp"

# Create the empty fc
arcpy.AddMessage("Creating the empty feature class")
fc = arcpy.management.CreateFeatureclass(outgdb, outName
, geomType, template)

# Create a list for shpfiles in the input workspace folder
parcelList = arcpy.ListFiles()
#print(parcelList)

# Append the parcel shapefiles to the new feature class
arcpy.AddMessage("Adding features to the new feature class")
arcpy.management.Append(parcelList, fc)