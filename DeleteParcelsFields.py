# coding: utf-8

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.2
# Date: 8/22/2023
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This tool will delete fields from the joined parcels that are not needed
# Cannot be undone.


# Import libraries
import arcpy
import os

# Set workspace and parameters
featureGDB = arcpy.GetParameterAsText(0)
arcpy.env.workspace = featureGDB

featureList = arcpy.ListFeatureClasses()
for feature in featureList:
     fields = ["COUNTY_ID", "CALC_ACRE", "PARCELID", "ADDRESS", "CLASS", "CITY", "STATE", "ZIP", "DEEDAC", "DISTRICT", "OWNER", "OWNER2", "MAILADDR", "MAILCITY", "LASTUPDATE"]
     Method = "KEEP_FIELDS"
     arcpy.management.DeleteField(feature, fields, Method)
