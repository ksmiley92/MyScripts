﻿# coding: utf-8
arcpy.management.SelectLayerByAttribute("Wetlands", "NEW_SELECTION", "calc_acres IS NULL", None)
# <Result 'Wetlands'>
arcpy.management.CalculateGeometryAttributes("Wetlands", "calc_acres AREA_GEODESIC", '', "ACRES", 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', "SAME_AS_INPUT")
# <Result 'Wetlands'>
