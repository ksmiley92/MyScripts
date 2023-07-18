# Name: CountTest.py
# Author: David W. Allen, GISP
# Date: Aug 14, 2008
# Updated: March 16, 2010
# Check the input value to see if it is greather than 0.
#
# --------------------------------------------------------------
# Import the ArcGIS script module
import arcpy

# Set up input parameter for use in a model
InputVal = arcpy.GetParameterAsText(0)
# Preset the output Boolean variable to False
arcpy.SetParameterAsText(1,0)

# Load required toolboxes...
# gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
# Count the features in the InputVal
NumFeatures = arcpy.GetCount_management(InputVal)

# Set the output to True only if there is more than one feature selected
if NumFeatures == 0 :
    arcpy.AddMessage ("No features were selected!")
else:
    arcpy.SetParameterAsText(1,1)
    arcpy.AddMessage (NumFeatures)
    arcpy.AddMessage ("Correct number of features to continue running.")
    



