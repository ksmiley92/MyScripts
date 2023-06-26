# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.1
# Date: 2/27/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code will join  fcs from a gdb with their respective tables in another gdb
# There must be an equal number of features and tables in their respective geodatabases
# Hard-coded to join parcels from TN comptroller. If distribution of data changes, the field names and names may
# Need to be edited.

# Import libraries
import arcpy
import os

#Define workspace and parameters
featureGDB = arcpy.GetParameterAsText(0) #r"C:\GIS_Tools\TN_Data_Management_Tools\temp_features.gdb" #arcpy.GetParameterAsText(0)
tableGDB =  arcpy.GetParameterAsText(1)  #r"C:\GIS_Tools\TN_Data_Management_Tools\temp_tables.gdb" #arcpy.GetParameterAsText(1)
in_field = arcpy.GetParameterAsText(2)  #Target field
join_field = arcpy.GetParameterAsText(3)  #Field being joined
arcpy.env.overwriteOutput = True

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
            #in_field = "GISLINK"
            join_table = tableGDB + "\\" + table
            #join_field = "GISLINK"
            fields = []
            arcpy.JoinField_management(in_data, in_field, join_table, join_field, fields)


