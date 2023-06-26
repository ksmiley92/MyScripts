###################################################################
# Describe_SHP.py
#
# This script will use a data type contraint and allow the
# user to select a shapefile. 
# The outputs will be a print of the data type,
# and the catalog path.
#
# Arguments:
# 0 - Input Shapefile name (required)
#
# David W. Allen, GISP
# Jul 2010
# ArcGIS 10
#
#####################################################################

# Load the arcgisscripting module
import sys, os, arcpy

# Get the input from the model
InputSHP = arcpy.GetParameterAsText (0)

# Create a describe object
#
descSHP = arcpy.Describe (InputSHP)

# Print shapefile properties
#
arcpy.AddWarning (descSHP.ShapeType)
arcpy.AddWarning (descSHP.CatalogPath)






