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
# This code will join parcels fcs from a gdb with their respective tables in another gdb

import arcpy
import os

#Define Gdb path
featureGDB = "C:/GIS_Tools/TN_Parcels_Tools_Pro/Parcels_features.gdb"
tableGDB = "C:/GIS_Tools/TN_Parcels_Tools_Pro/Parcels_tables.gdb"

#Create Feature List Variable
arcpy.env.workspace = featureGDB
featureList = arcpy.ListFeatureClasses()

#Create Table List Variable
arcpy.env.workspace = tableGDB
tableList = arcpy.ListTables()

#Set table Names to featurelist names equivalent
for table in tableList:
    tableNum = table[0:-5]
# Find table and Feature from Lists with the same name and join them
    for feature in featureList:
        if feature == tableNum:
            in_data = featureGDB + "\\" + feature
            in_field = "GISLINK"
            join_table = tableGDB + "\\" + table
            join_field = "GISLINK"
            fields = []
            arcpy.JoinField_management(in_data, in_field, join_table, join_field, fields)


