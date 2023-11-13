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
# This code will read and copy parcels tables to a file gdb for each.

# Copy the newly joined parcels to an output folder in shapefile format

import arcpy
import os

#Set input GDB
featureGDB = "C:/GIS_Tools/TN_Parcels_Tools_Pro/Parcels_features.gdb"

#Create Feature List Variable
arcpy.env.workspace = featureGDB
featureList = arcpy.ListFeatureClasses()

#Copy to folder as shapefile
OutShpFolder = "C:/GIS_Tools/TN_Parcels_Tools_Pro/TN_Parcels"
for feature in featureList:
    arcpy.conversion.FeatureClassToShapefile(feature, OutShpFolder)
