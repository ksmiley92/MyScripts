# calculate_feet.py
# Author: David Meranus
# Date: 091223
# Description: Tool that calculates feet for line shapefile or feature class and displays the feet on the map
# Notes: does not work on a non-editable layer, such as state-configured portal layers. Calc is in the units of the input layer's coordinate system
# v2
# modified by Kyle Smiley
# included block that will modify the first label expression in the layer and display
# modified variable name for input layer


## Import packages ##
import arcpy
import os

## To allow overwrite of the outputs ##
arcpy.env.overwriteOutput = True

## Insert Tool parameters ##
inlayer = arcpy.GetParameterAsText(0)

## Add feet field to selected layer ##
arcpy.management.AddField(inlayer, "Tot_Feet", "FLOAT")
arcpy.AddMessage("Adding tot_feet field to the attribute table")

## Calculate the length in feet for the line ## 
arcpy.management.CalculateGeometryAttributes(inlayer, [["Tot_Feet", "LENGTH"]],"FEET_US")
arcpy.AddMessage("Calculating US Feet")

# find the layer in the project and display labels w/ custom label expression
aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.activeMap
arcpy.AddMessage("Map: " + m.name)
layer = m.listLayers(inlayer)[0]
arcpy.AddMessage("Input layer: " + inlayer)
layer.showLabels = True
label_class = layer.listLabelClasses()[0]
label_class.expression = "Round($feature.Tot_Feet, 2) + ' Ft.'"
label_class.visible = True
aprx.save()

