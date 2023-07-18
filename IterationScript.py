# ---------------------------------------------------------------------------
# IterationScript.py
# Created : Jan 2009
#   (Boolean sript for iterations in ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting
# Create the Geoprocessor object
gp = arcgisscripting.create(9.3)

# Get the input from the model
InputVal = gp.GetParameterAsText(0)

# Statement to check status of condition variable
# Model will continue to run until input value is greater than 500
if int(InputVal) =< 500: #Mathematical express of condition
    gp.SetParameterAsText(1,"True")
else:
    gp.SetParameterAsText(1,"False")


