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

# Import the libraries you will need
import os
import arcpy
arcpy.env.overwriteOutput = True

# Set input folder as tool parameter
gpx_directory_path = #path
arcpy.env.workspace = gpx_directory_path
gpx_list = arcpy.ListFiles()
#print(gpx_list)

# Define the output paramter
arcpy.SetParameterAsText(1, output_shapefile)


for gpx_file in gpx_list:
    if gpx_file.endswith(".gpx"):
        full_gpx_path = os.path.join(gpx_directory_path, gpx_file)
        print(f"Converting {full_gpx_path} to shapefile")
        output_shapefile = os.path.splitext(full_gpx_path)[0] + ".shp"
        try:
            arcpy.GPXtoFeatures_conversion(full_gpx_path, output_shapefile)
            print(f"Finished Converting {full_gpx_path} to shapefile \n")
        except Exception as e:
            print("failed to convert")
            print(e)




arcpy.AddMessage("Finished converting all gpx to shp")
#print("Finished converting all gpx to shp")

