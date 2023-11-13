## Import packages ##
import arcpy
import os

## To allow overwrite of the outputs ##
arcpy.env.overwriteOutput = True

## Insert Tool parameters ##
layer = arcpy.GetParameterAsText(0)

## Set Project ##
aprx = arcpy.mp.ArcGISProject("CURRENT")

## Add Total_Acres field to selected layer ##
arcpy.management.AddField(layer, "Total_Acres", "FLOAT")

## Calculate the total acres of the polygons ## 
arcpy.management.CalculateGeometryAttributes(layer, [["Total_Acres", "AREA"]],"", "ACRES_US")
