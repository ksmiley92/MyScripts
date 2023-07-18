#**********************************************************************
# Description:
# Tests if a field exists and outputs two booleans:
#   Exists - true if the field exists, false if it doesn't exist
#   Not_Exists - true if the field doesn't exist, false if it does exist
#                (the logical NOT of the first output).
#
# Arguments:
#  0 - Table name
#  1 - Exists (boolean - see above)
#  2 - Not_Exists (boolean - see above)
#
# Created by: ESRI
# Modified for "Getting To Know ArcGIS Modelbuilder"
#**********************************************************************

# Standard error handling - put everything in a try/except block
#
try:

    # Import system modules
    import sys, string, os, arcgisscripting

    # Create the Geoprocessor object
    gp = arcgisscripting.create()

    # Get input arguments - table name, field name
    #
    in_Table = gp.GetParameterAsText(0)

    # Check if the table exists
    #
    if not gp.Exists(in_Table):
	gp.AddMessage("The table %s does not currently exist" % (in_Table))
        gp.SetParameterAsText(2, "True")
        gp.SetParameterAsText(3, "False")
    else:
	gp.AddMessage("The table %s already exists" % (in_Table))
        gp.SetParameterAsText(2, "False")
        gp.SetParameterAsText(3, "True")


# Handle script errors
#
except Exception, errMsg:

    # If we have messages of severity error (2), we assume a GP tool raised it,
    #  so we'll output that.  Otherwise, we assume we raised the error and the
    #  information is in errMsg.
    #
    if gp.GetMessages(2):   
        gp.AddError(GP.GetMessages(2))
    else:
        gp.AddError(str(errMsg))  