#**********************************************************************
# Description:
# Tests if a field exists and outputs two booleans:
#   Exists - true if the field exists, false if it doesn't exist
#   Not_Exists - true if the field doesn't exist, false if it does exist
#                (the logical NOT of the first output).
#
# Arguments:
#  0 - Input Table name (required)
#  1 - Input Field name (required)
#  2 - Output Boolean Variable for Exists (see above)
#  3 - Output Boolean Variable for Not_Exists (see above)
#
# Created by: ESRI
# Fall 2008
# Updated Spring 2010
# ArcGIS 10 using arcpy module
#**********************************************************************


# Import system modules
import arcpy, sys, string, os

# Get input arguments - table name, field name
#
in_Table = arcpy.GetParameterAsText(0)
in_Field = arcpy.GetParameterAsText(1)

# First check that the table exists
#
if not arcpy.Exists(in_Table):
    raise Exception, "Input table does not exist"

# Use the ListFields function to return a list of fields that matches
#  the name of in_Field. This is a wildcard match. Since in_Field is an
#  exact string (no wildcards like "*"), only one field should be returned,
#  exactly matching the input field name.
#
fields = arcpy.ListFields(in_Table, in_Field)

# If ListFields returned anything, the Next operator will fetch the
#  field. We can use this as a Boolean condition.
#
field_found = fields.Next()

# Branch depending on whether field is found or not. Issue a
# message, and then set our two output variables accordingly
#
if field_found:
    arcpy.AddMessage("Field was found!")
    arcpy.SetParameterAsText(2, "True")
else:
    arcpy.AddMessage("Field was not found. :( ")
    arcpy.SetParameterAsText(2, "False")

# Handle script errors
#


