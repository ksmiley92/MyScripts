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
# This code will read and copy parcels shapefiles to a file gdb for each.

# Copy fcs or shapefiles that start with "Parcels" into a gdb from subdirectories
import arcpy
import os
workspace = "C:/GIS_Tools/TN_Parcels_Tools_Pro/Counties"
outgdb = "C:/GIS_Tools/TN_Parcels_Tools_Pro/Parcels_features.gdb"
walk = arcpy.da.Walk(workspace, datatype = "FeatureClass")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        if not file.startswith("Parcels"):
            continue
        infc = os.path.join(dirpath, file)
        outfcname = os.path.basename(file).split(".")[0] + "_" + os.path.basename(dirpath)
        outfc = os.path.join(outgdb, outfcname)
        arcpy.management.CopyFeatures(infc, outfc)
