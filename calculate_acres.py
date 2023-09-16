# calculate_acres.py
# Author: David Meranus
# Date: 091223
# Description: Tool that calculates acres for polygon shapefile or feature class and displays the acres on the map
# Notes: does not work on a non-editable layer, such as state-configured portal layers
# v2
# modified by Kyle Smiley
# included block that will modify the first label expression in the layer and display

## Import packages ##
import arcpy
import os

arcpy.env.overwriteOutput = True

## Insert Tool parameters ##
inlayer = arcpy.GetParameterAsText(0)

## Set Project ##
#aprx = arcpy.mp.ArcGISProject("CURRENT")
#arcpy.AddMessage(aprx)

## Add Total_Acres field to selected layer ##
arcpy.management.AddField(inlayer, "Tot_Acres", "FLOAT")
arcpy.AddMessage("Adding tot_acres field to the attribute table")

## Calculate the total acres of the polygons ## 
arcpy.management.CalculateGeometryAttributes(inlayer, [["Tot_Acres", "AREA"]],"", "ACRES_US")
arcpy.AddMessage("Calculating US Acres")

# find the layer in the project and display labels w/ custom label expression
aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.activeMap
arcpy.AddMessage("Map: " + m.name)
layer = m.listLayers(inlayer)[0]
arcpy.AddMessage("Input layer: " + inlayer)
layer.showLabels = True
label_class = layer.listLabelClasses()[0]
label_class.expression = "Round($feature.Tot_Acres, 2) + ' Ac.'"
label_class.visible = True
aprx.save()