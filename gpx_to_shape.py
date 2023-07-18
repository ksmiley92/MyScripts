# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# gpx_to_shape_youtube.py
# Version: 0.1
# Date: 2/22/23
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code will convert a folder of GPX files (also called waypoints) to shapefiles in the original folder
#

##Import the libraries you will need
import os
import arcpy
arcpy.env.overwriteOutput = True

# Set input folder as tool parameter
gpx_directory_path = arcpy.GetParameterAsText(0)
outlocation = arcpy.GetParameterAsText(1)
arcpy.env.workspace = gpx_directory_path
gpx_list = arcpy.ListFiles("*gpx")
#print(gpx_list)

for gpx_file in gpx_list:
    #full_gpx_path = os.path.join(gpx_directory_path, gpx_file)
    temp_fc = arcpy.Describe(gpx_file).basename
    #print(temp_fc.basename)
    #print(temp_fc.basename)
    os.path.join(arcpy.env.scratchGDB, temp_fc)
    arcpy.GPXtoFeatures_conversion(gpx_file, temp_fc)
    arcpy.FeatureClassToShapefile_conversion(temp_fc, outlocation)


        #try:
            #arcpy.GPXtoFeatures_conversion(full_gpx_path, output_shapefile)
            #print(f"Finished Converting {full_gpx_path} to shapefile \n")
        #except Exception as e:
            #print("failed to convert")
            #print(e




#arcpy.AddMessage("Finished converting all gpx to shp")
arcpy.AddMessage("Finished converting all gpx to shp")

