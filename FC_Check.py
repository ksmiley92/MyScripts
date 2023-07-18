################################################################################
# FC_Check.py
# This script will test for the existence of a user specified Feature Class.
# The ouputs will be either True or False.
#
# Arguments:
# 0 - Input Feature Class Name (required)
# 1 - Output Boolean variable for Exists
# 2 - Output Boolean variable for Does Not Exist
#
# Your name
# Month Year
# ArcGIS 10
#
################################################################################
#

# Load the arcpy module
# This makes all the ArcGIS geoprocessing tools available in Python
import sys, os, arcpy

# Get the input from the model
InputFC = arcpy.GetParameterAsText(0)


# Statement to check the existence of the feature class
if arcpy.Exists(InputFC):
    arcpy.SetParameterAsText(1,”True”)
    arcpy.SetParameterAsText(2,”False”)
    raise Exception, “Feature Class Already Exists!”
else:
    arcpy.SetParameterAsText(1,”False”)
    arcpy.SetParameterAsText(2,”True”)
    arcpy.AddMessage(“Feature Class Does Not Exist!”)


    

