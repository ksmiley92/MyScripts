# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.2
# Date: 8/22/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Copy the newly joined parcels to an output folder in shapefile format

# Import Libraries
import arcpy
import os

#Set parameters
featureGDB = arcpy.GetParameterAsText(0)
OutShpFolder = arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True

#Create Feature List Variable
arcpy.env.workspace = featureGDB
featureList = arcpy.ListFeatureClasses()

#Copy to folder as shapefile
for feature in featureList:
    arcpy.conversion.FeatureClassToShapefile(feature, OutShpFolder)
