# ---------------------------------------------------------------------------
# CheckExists.py
# Created on: Wed Jan 3 2008
# Updated on: Wed Mar 17 2010
#
# ---------------------------------------------------------------------------

# Import system modules
import arcpy, sys, string, os

# Get the input in the model
InputFDS = arcpy.GetParameterAsText(0)
Workspace = "C:/ESRIPress/GTK Modelbuilder/MyAnswers/Results.gdb/"
Pathname = Workspace + InputFDS
arcpy.AddMessage(Pathname)


# Statement to check the existence of the feature dataset
if arcpy.Exists(Pathname):
    arcpy.SetParameterAsText(1,Pathname)
    arcpy.AddMessage("Feature Dataset Already Exists!")
else:
    arcpy.SetParameterAsText(1,"")
    arcpy.SetParameterAsText(2,"True")
    arcpy.AddMessage("Feature Dataset Does Not Exist!")