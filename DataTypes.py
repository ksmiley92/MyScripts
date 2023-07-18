# Name: DataType.py
# Author: David W. Allen, GISP
# Date: Jan 2009
# Used for demonstrating data types.
#
# --------------------------------------------------------------
# Import arcgisscripting and sys modules
import arcgisscripting, os, sys, string
gp = arcgisscripting.create(9.3)

# Set up input parameter for use in a model
InputVal = gp.GetParameterAsText(0)
InputVal = gp.GetParameterAsText(1)
InputVal = gp.GetParameterAsText(2)
InputVal = gp.GetParameterAsText(3)


