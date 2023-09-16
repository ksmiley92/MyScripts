# zip_shp.py
# Author: Kyle Smiley
# Date: 091223
# Description: Tool that zips multiple shapefiles (or other files) by user-selected input in a GP tool in ArcGIS Pro
# Notes: designed for people to ZIP shapefiles by browsing to them so they can upload them into the web
# v1
# ZIP multiple shapfiles by name

import zipfile
import os
import arcpy

shpfolder = arcpy.GetParameterAsText(0)
shpname = arcpy.GetParameterAsText(1)
newZip_name = arcpy.GetParameterAsText(2)

##change directory from working dir to dir with files if needed
os.chdir(shpfolder)
arcpy.AddMessage('Finding the directory')
arcpy.AddMessage('Directory found')

# Make a list to append the shp components
shp_list = []
for (dirpath, dirname, filenames) in os.walk(shpfolder):
    for file in filenames:
        if file.startswith(shpname):
            shp_list.append(file)
arcpy.AddMessage('Assembling the shp components')
arcpy.AddMessage(shp_list)


with zipfile.ZipFile(newZip_name + '.zip', mode='w') as archive:
    for shp in shp_list:
        archive.write(os.path.join(shpfolder, shp), shp)
    arcpy.AddMessage('Zipping shps')
    arcpy.AddMessage('shps succesfully added')