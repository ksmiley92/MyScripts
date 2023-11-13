## Import packages ##
import arcpy
import os

## To allow overwrite of the outputs ##
arcpy.env.overwriteOutput = True

## Insert Tool parameters ##
layer = arcpy.GetParameterAsText(0)

## Set Project ##
aprx = arcpy.mp.ArcGISProject("CURRENT")

## Add feet field to selected layer ##
arcpy.management.AddField(layer, "Total_Feet", "FLOAT")

## Calculate the length in feet for the line ## 
arcpy.management.CalculateGeometryAttributes(layer, [["Total_Feet", "LENGTH"]],"FEET_US")
