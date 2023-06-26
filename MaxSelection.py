# ---------------------------------------------------------------------------
# MaxSelection.py
# Created : Jan 2009
# Name: David W. Allen, GISP
#   (Boolean sript for iterations in ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting
# Create the Geoprocessor object
gp = arcgisscripting.create(9.3)

# Get the input from the model - convert to an integer
InputVal = gp.GetParameterAsText(0)

# Statement to check status of condition variable
# Model will continue to run until condition is met

if int(InputVal) < 80:
    gp.AddMessage("The selection count is still less than 80.")
    gp.SetParameterAsText(1,1)
else:
    gp.AddMessage("The selection count has exceeded 80. The model will stop!")
    gp.SetParameterAsText(1,0)


