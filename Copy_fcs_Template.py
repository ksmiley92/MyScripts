# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.1
# Date: 8/22/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code serves as a template to begin writing tools that copy feature classes or shapefiles into a gdb in ArcGIS Pro

# Copies fcs or shapefiles from one folder into a feature dataset.
import arcpy, os
ws = "C:/path"
gdb = "Database.gdb"
prj = "myprojection.prj"
arcpy.env.workspace = ws
arcpy.CreateFileGDB_management(ws, gdb)
sr = arcpy.SpatialReference(os.path.join(ws, prj))
arcpy.CreateFeatureDataset_management(gdb, "out_name", sr)
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fc_desc = arcpy.Describe(fc)
    if fc_desc.shapeType == "shape_type":
        newfc = os.path.join(gdb, "out_name", fc_desc.basename)
        arcpy.CopyFeatures_management(fc, newfc)

# Looks for all fcs or shapefiles in subdirectories and copies them to a gdb with same name
import arcpy, os
workspace = "D:path"
outgdb = "D: path.gdb"
walk = arcpy.da.Walk(workspace, datatype = "FeatureClass")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
            infc = os.path.join(dirpath, file)
            desc = arcpy.da.Describe(infc)
            outfc = os.path.join(outgdb, desc["baseName"])
            arcpy.management.CopyFeatures(infc, outfc)

# Looks for all fcs or shapefiles in subdirectories and copies them with subdirectory name attached
import arcpy, os
workspace = "D:/Geodata/Cadastral/Parcels/Counties"
outgdb = "D:/Geodata/Cadastral/Parcels/Parcels_features.gdb"
walk = arcpy.da.Walk(workspace, datatype = "FeatureClass")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
            infc = os.path.join(dirpath, file)
            outfcname = os.path.basename(file).split(".")[0] + "_" + os.path.basename(dirpath)
            outfc = os.path.join(outgdb, outfcname)
            arcpy.management.CopyFeatures(infc, outfc)

# Looks for all fcs or shapefiles that start with a specific name and copies them to gbd with subdirectory attached
workspace = "D:/Geodata/Cadastral/Parcels/Counties"
outgdb = "D:/Geodata/Cadastral/Parcels/Parcels_features.gdb"
walk = arcpy.da.Walk(workspace, datatype = "FeatureClass")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if not file.startswith("Parcels"):
            continue
        infc = os.path.join(dirpath, file)
        outfcname = os.path.basename(file).split(".")[0] + "_" + os.path.basename(dirpath)
        outfc = os.path.join(outgdb, outfcname)
        arcpy.management.CopyFeatures(infc, outfc)


