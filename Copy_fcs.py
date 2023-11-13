# coding: utf-8
import arcpy, os
ws = "C:/GIS_Training/ArcPro_templates/Tennessee_Conservation_Planner_Pro_v1"
gdb = "Backup.gdb"
prj = "NAD 1983 StatePlane Tennessee FIPS 4100 (US Feet.prj"
arcpy.env.workspace = ws
arcpy.management.CreateFileGDB(ws, gdb)
# <Result 'C:/GIS_Training/ArcPro_templates/Tennessee_Conservation_Planner_Pro_v1\\Backup.gdb'>
sr = arcpy.SpatialReference(os.path.join(ws, prj))
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'os' is not defined
sr = arcpy.SpatialReference(os.path.join(ws, prj))
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "C:\Program Files\ArcGIS\Pro\Resources\ArcPy\arcpy\arcobjects\mixins.py", line 942, in __init__
#     self._arc_object.createFromFile(item, vcs)
# RuntimeError: SpatialReference: Error in CreateFromFile
prj = "NAD 1983 StatePlane Tennessee FIPS 4100 (US Feet)"
sr = arcpy.SpatialReference(os.path.join(ws, prj))
arcpy.management.CreateFeatureDataset(gdb, "Conservation_Planner", sr)
# <Result 'C:\\GIS_Training\\ArcPro_templates\\Tennessee_Conservation_Planner_Pro_v1\\Backup.gdb\\Conservation_Planner'>
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fc_desc = arcpy.Describe(fc)
    newfc = os.path.join(gdb, "Conservation_Planner", fc_desc.basename)
    arcpy.management.CopyFeatures(fc, newfc)
for fc in fc_list:
    arcpy.management.CopyFeatures(fc, newfc)
#   File "<string>", line 2
#     arcpy..management.CopyFeatures(fc, newfc)
#           ^
# SyntaxError: invalid syntax
for fc in fc_list:
    arcpy.management.CopyFeatures(fc, newfc)
fc_list = arcpy.ListFeatureClasses(TN)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'TN' is not defined
ws = "C:/GIS_Training/ArcPro_templates/Tennessee_Conservation_Planner_Pro_v1/Layers"
arcpy.env.workspace = ws
fc_list = arcpy.ListFeatureClasses()
print(fc_list)
# []
