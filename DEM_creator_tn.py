# -*- coding: utf-8 -*-
# V 2.1 Added messages and build raster stats/pyramids tool
# known errors. Does not work with a web map
# Import packages
import arcpy
import os

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Get the parameters
aoi = arcpy.GetParameterAsText(0)
inraster = arcpy.GetParameterAsText(1)
saveloc = arcpy.GetParameterAsText(2)
savename = arcpy.GetParameterAsText(3)

# Remove the tif output if it's in the table of contents already.
# You don't have to do this since the environment is set to overwrite, however
# I'm doing it because the layer will be duplicated in the table of contents each
# time the tool is run otherwise.
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
layers = aprxMap.listLayers()
for layer in layers:
        if layer.name in [savename]:
            aprxMap.removeLayer(layer)

# Project AOI and save. The projection will be in TN State Plane here is more notes
aoi_savename = saveloc + "/aoi.shp"
aoi_reproj = arcpy.management.Project(in_dataset=aoi, out_dataset=aoi_savename,
                                          out_coor_system=arcpy.SpatialReference("NAD 1983 (2011) StatePlane Tennessee FIPS 4100 (US Feet)"))

# Clip to the AOI boundary
final_file_name = saveloc + "/" + savename
arcpy.management.Clip(in_raster=inraster,
                          out_raster=final_file_name,
                          in_template_dataset=aoi_reproj, nodata_value="3.4e+38",
                          clipping_geometry="ClippingGeometry",
                          maintain_clipping_extent="MAINTAIN_EXTENT")

# Load the clipped DEM
aprxMap.addDataFromPath(final_file_name)

arcpy.management.BuildPyramidsandStatistics(final_file_name, "INCLUDE_SUBDIRECTORIES", "BUILD_PYRAMIDS", "CALCULATE_STATISTICS", "NONE", '', "NONE", 1, 1, [], -1, "NONE", "NEAREST", "DEFAULT", 75, "SKIP_EXISTING", '', "NONE")
arcpy.AddMessage("Building pyramids and stats")
arcpy.AddMessage("Done")