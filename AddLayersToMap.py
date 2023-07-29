# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# AddLayersToMap.py
# Version: 0.1
# Date:
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# AddCPCLayersToMap.py
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
def AddayersToMap():
    arcpy.AddMessage("starting Add Layers to Map")

# Set workspace, project, map, and layerfile location
proj = arcpy.mp.ArcGISProject("CURRENT")
map = proj.listMaps("MapName")[0]
grp = map.listLayers("LayerGroupName")[0]
PointsLyr = arcpy.mp.LayerFile(r"Path")
LinesLyr = arcpy.mp.LayerFile(r"Path")
PolyLyr = arcpy.mp.LayerFile(r"Path")

# Add layer files to group
map.addLayerToGroup(grp, PointsLyr, 'TOP')
map.addLayerToGroup(grp, LinesLyr, 'TOP')
map.addLayerToGroup(grp, PolyLyr, 'TOP')
