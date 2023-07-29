# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# AddCPCLayersToMap.py
# Version: 0.1
# Date: 6/8/22
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code adds FDC CPC practices from ArcGIS Online to the current map
# Requires a stored path of the CPC Points layer file
# Must be signed in to ArcGIS Online

# Import the libraries you will need
import os, arcpy
def AddCPCLayersToMap():
    arcpy.AddMessage("starting Add CPC Layers to Map")

# Set workspace, project, map, and layerfile location
proj = arcpy.mp.ArcGISProject("CURRENT")
map = proj.listMaps("Conservation Planner Workspace")[0]
grp = map.listLayers("Conservation Planning")[0]
PointsLyr = arcpy.mp.LayerFile(r"C:\GIS_Tools\TN_Conservation_Planner_Tools\Support\TN GEO COLLECT CPC Points.lyrx")
LinesLyr = arcpy.mp.LayerFile(r"C:\GIS_Tools\TN_Conservation_Planner_Tools\Support\TN GEO COLLECT CPC Lines.lyrx")
PolyLyr = arcpy.mp.LayerFile(r"C:\GIS_Tools\TN_Conservation_Planner_Tools\Support\TN GEO COLLECT CPC Polygons.lyrx")

# Add layer files to group
map.addLayerToGroup(grp, PointsLyr, 'TOP')
map.addLayerToGroup(grp, LinesLyr, 'TOP')
map.addLayerToGroup(grp, PolyLyr, 'TOP')


