# export_shp.py
# Author: Kyle Smiley
# Date: 091123
# Description: Tool that accepts selected feautures by the user and exports them to a folder where it will reside as a shapefile
# Notes: designed as a workaround for planners to export their features to a shapefile to avoid using the menu in the TOC. Eliminates need to discriminate between
# a folder or gdb workspace, as this determines whether it will be a shapefile or a GDB fc
# v1
# 
#

# import libraries
import arcpy
import os

# set the project and overwrite flag
arcpy.env.overwriteOutput = True

# set parameters for the ArcGIS tool
layer = arcpy.GetParameterAsText(0)
shp = arcpy.GetParameterAsText(1)   # user-defined folder to store the shpfile. DataType = folder


# Use GP tool export features. use can optionally select features and run it on the selection
arcpy.conversion.ExportFeatures(layer, shp)