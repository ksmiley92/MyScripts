# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.1
# Date:
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code serves as a template to begin writing new scripts

# Import the libraries you will need
import os
import arcpy
def currentfunction(argl):
    arcpy.AddMessage("starting currentfunction")

argl = arcpy.GetParameterAsText(0)

currentfunction(argl)

# parameter1 = arcpy.GetParameterAsText(0)
# parameter2 = arcpy.GetParameterAsText(1)
# parameter3 = arcpy.GetParamterAsText(2)


# Function for viewing a gbd table in ArcGIS Pro using notebooks
# This needs editing because field names don't show up. Use view_table function below as an alternative
import pandas as pd # import library
def view_table(gdb,out_table,n=5):
    # Set workspace to the gdb
    arcpy.env.workspace = gdb

    # Create a pandas dataframe from the table
    df = pd.DataFrame.from_records(arcpy.da.SearchCursor(out_table,["*"]))

    # Return the first few records
    return df.head(n)

# Example: view_table(gdb, out_table,10)

# Function for viewing a feature class or GDB tablein ArcPro using notebooks
import pandas as pd  #  import library
def view_gdbtable(gdbtable):    # fc or gdb table (either can be viewed)
    fields = [field.name for field in arcpy.ListFields(fc)]
    data = [row for row in arcpy.da.SearchCursor(fc,fields)]
    df = pd.DataFrame(data,columns=fields)
    return.df.head()

arcpy.da.Describe
arcpy.FeatureClassToFeatureClass_conversion