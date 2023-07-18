# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# AddLayersToMap.py
# Version: 0.1
# Date: 6/8/22
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code adds layers to the current map
# Requires a stored path of layer files
# Must be signed in if layer files reference online content

# Import the libraries you will need
import os, arcpy
def AddLayerToMap():
    arcpy.AddMessage("starting Add CPC Layers to Map")

# Set workspace, project, map, and layerfile location
proj = arcpy.mp.ArcGISProject("CURRENT")
map = proj.listMaps("MapName")[0]
grp = map.listLayers("GroupLayerName")[0]
PointsLyr = arcpy.mp.LayerFile("Path")
LinesLyr = arcpy.mp.LayerFile(r"Path")
PolyLyr = arcpy.mp.LayerFile("Path")

# Add layer files to group
map.addLayerToGroup(grp, PointsLyr, 'TOP')
map.addLayerToGroup(grp, LinesLyr, 'TOP')
map.addLayerToGroup(grp, PolyLyr, 'TOP')
