# ---------------------------------------------------------------------------
# Template.py
# Created : Date
# Name:
#   (Boolean sript for iterations in ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
# Add the ArcGIS tools with the arcpy module
import arcpy, sys, os


# Get the input from the model
InputVal = arcpy.GetParameterAsText(0)

# Statement to check status of condition variable
# Model will continue to run until condition is met
if int(InputVal) XX : #Mathematical express of condition
    arpy.SetParameterAsText(1,"True")
else:
    arcpy.SetParameterAsText(1,"False")


