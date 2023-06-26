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
# This code will print feature classes in a gdb.


import arcpy, os
ws = "C:/path"
gdb = "Database.gdb"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    print(fc_list)