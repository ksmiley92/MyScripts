# -*- coding: utf-8 -*-
# $ID: block_warp_mosaic.py, v 1.02 2020/12/10¶ $
# Name:     block_warp_mosaic
# Project:  Raster Toolset
# Purpose:  Mosaic rasters by individual folders with GDAL warp
# Author:   Alexander Stum, alexander.stum@usda.gov

# v 1.01
    # Incorporated gdal Translate to subset vrt
# v 1.02
    # Blocky clip
# v 1.03
    # Fixed bug where same proj file was used to define dstSRS and outputBoundsSRS
    # time to process added

# v 1.04
    # Eliminated the pre-clipping by cutline extent
    # It seems when a cutline is used in combination with warp, results in resampling
    # striations
v = '1.04'
import os
gdata = r'C:\PROGRA~1\ArcGIS\Pro\Resources\pedata\gdaldata'
os.environ['GDAL_DATA'] = gdata

import arcpy
from osgeo import gdal
from osgeo import osr
from osgeo import ogr
# import importlib
# import imp
import sys
import time
# configure gdal
gdal.SetConfigOption('GDAL_DATA', 
                     'C:/PROGRA~1/ArcGIS/Pro/Resources/pedata/gdaldata')
# calcPy = r'C:/PROGRA~1/ArcGIS\Pro\bin\Python\envs\arcgispro-py3\Lib\site-packages\osgeo_utils/gdal_calc.py'
# calcPy = r'C:/PROGRA~1/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/Lib/site-packages/osgeo/scripts/gdal_calc.py'
# from importlib import reload
# foo = imp.load_source('gdal_calc',calcPy)
# reload()
gdal.UseExceptions()

Polygon = arcpy.Polygon
Array = arcpy.Array
P = arcpy.Point
# PG = arcpy.PointGeometry

def progress_callback(complete, message, data):
    percent = int(complete * 100)  # round to integer percent
    # data.update(percent)  # update the progressbar
    arcpy.SetProgressor('step','Performing GDAL Warp')
    arcpy.SetProgressorPosition(percent)
    return 1

def gParam(flag, params):
    flags = [p for p in params if flag in '-' + p]
    if flags:
        param = flags[0].split(flag)[1]  #only return first
        for f in flags:
            params.remove(f)
        return param.strip()
    else:
        return None
    
def gParams(flag, params):
    flags = [p for p in params if flag in '-' + p]
    if flags:
        param = []
        for f in flags:
            #remove '-' and split from flag
            [p_split] = f.split(flag[1:])[1:]
            param.append(p_split.strip())
            params.remove(f)
            
        return param
    else:
        return None

def gBoolParam(flag, params):
    flags = [p for p in params if flag in '-' + p]
    if flags:
        params.remove(flags[0])
        return True
    else:
        return False

 
inPaths     = arcpy.GetParameter(0)
outPath     = arcpy.GetParameterAsText(1)
outF        = arcpy.GetParameterAsText(2)
XR, YR      = arcpy.GetParameterAsText(3).split() or (None,None)
resample    = arcpy.GetParameter(4) or None
extent      = arcpy.GetParameter(5) or None
cutline     = arcpy.GetParameterAsText(6) or None
blocky      = arcpy.GetParameter(7)
outSR       = arcpy.GetParameter(8) or None

ot          = arcpy.GetParameterAsText(9) or None
te_srs      = arcpy.GetParameter(10)
tap         = arcpy.GetParameter(11)
dstNodata   = arcpy.GetParameter(12) or None
gdalParam   = arcpy.GetParameterAsText(13) or None

day         = 84600

# %% setup
arcpy.AddMessage("version "+v)
# arcpy.AddMessage(gdalParam)
if gdalParam:
    split1 = ' '.join(gdalParam.split())
    split2 = split1.split('-')[1:]

proj_path = os.path.dirname(__file__)
outF = outF.split('-')[0]
drv = gdal.GetDriverByExtensionOrName(outF)
ext = "."+drv.GetMetadataItem(gdal.DMD_EXTENSION)
arcpy.env.workspace = outPath
extF = os.path.join(outPath,'extent.shp') # 'in_memory/extent'
sub = os.path.join(outPath, 'sub.shp') # 'in_memory/sub'
union = os.path.join(outPath, 'union.shp') #'in_memory/union'
unionFlag = False
# if cutline:
#     cutline = cutline.replace('\\', '/')
#     crop = True
# else:
#     crop = False
crop = gBoolParam('-crop_to_cutline', split2)

if blocky and cutline:
    cutG = arcpy.PairwiseDissolve_analysis(cutline, arcpy.Geometry())
    subset = True
elif cutline:
    cutG = arcpy.PairwiseDissolve_analysis(cutline, arcpy.Geometry())
    subset = True
else:
    blocky = False
    subset = False
try:
    # cutline feature coordinate system
    if not outSR.exportToString():
        epsg0 = None    
    else:
        eCode = outSR.factoryCode
        tSR = osr.SpatialReference()
        validEPSG = tSR.ImportFromEPSG(eCode) #returns 0 if code recognized
        if validEPSG != 1:
            arcpy.CreateFeatureclass_management(proj_path,"proj1.shp",'POINT',
                                                spatial_reference=outSR)
            epsg0 = "ESRI::" + os.path.join(proj_path,"proj1.prj")
        else:
            epsgO = "EPSG:" + str(eCode)
    
    # Extent coordinate system
    if not te_srs.exportToString():
        epsg1 = None    
    else: 
        eCode = te_srs.factoryCode
        tSR = osr.SpatialReference()
        validEPSG = tSR.ImportFromEPSG(eCode) #returns 0 if code recognized
        if validEPSG != 1:
            arcpy.CreateFeatureclass_management(proj_path,
                                                "proj2.shp",
                                                'POINT',
                                                spatial_reference=outSR)
            epsg1 = "ESRI::" + os.path.join(proj_path,"proj2.prj")
        else:
            epsg1 = "EPSG:" + str(eCode)
    
    XYR = gParams('tr', split2)
    if XYR:
        XR = XYR[0]
        YR = XYR[-1]
        
    dims = gParams('ts', split2)
    if dims:
        width = dims[0]
        height = dims[-1]
    else:
        width = None
        height = None
    cutlineDSName = gParams('-cutline', split2) or cutline
    # %% Warp Options
    WO = {'format': outF, #-of
          'outputBounds': gParams('-te', split2) or extent, # -te xmin ymin xmax ymax
          'outputBoundsSRS': epsg1, # -te_srs SRS of the outbound coordinates
          'xRes': XR,  # -tr
          'yRes': YR,  # -tr
          'targetAlignedPixels': gBoolParam('tap', split2) or tap, # -tap
          'width': width, # -ts ca't be used with -tr
          'height': height, # -ts cant' be used with -tr
          'srcSRS': gParams('-s_srs', split2), # -s_srs source spatial reference system
          'dstSRS': epsg0,  #-t_srs
          'srcAlpha': gBoolParam('-srcalpha', split2), # -srcalpha force last band to be considered source alpha
          'dstAlpha': gBoolParam('-dstalpha', split2), # -dstalpha Create destination alpha band to id ND
          'warpOptions': gParams('-wo', split2) or None, # -wo
          'errorThreshold': gParams('-et', split2), # -et
          'warpMemoryLimit': gParams('-wm', split2),  # -wm
          'creationOptions': gParams('-co', split2) or None, # -co
          'outputType': gParams('-ot', split2) or 0,  # -ot output datatype
          'workingType': gParams('-wt', split2) or 0,  # -wt
          'resampleAlg': gParams('-r', split2) or resample, # -r
          'srcNodata': gParams('-srcnodata', split2), # -srcnodata
          'dstNodata': gParams('-dstnodata', split2) or dstNodata,  # -dstnodata
          'multithread': gBoolParam('-multi', split2), # -multi
          'tps': gBoolParam('-tps', split2), # -tps
          'rpc': gBoolParam('-rpc', split2),  # -rpc
          'geoloc': gBoolParam('-geoloc', split2),  # -geoloc
          'polynomialOrder': gParams('-order', split2), # -order
          'transformerOptions': gParams('-to', split2) or None,  # -to
          'cutlineDSName': None, # -cutline
          'cutlineLayer': gParams('-cl', split2),  # -cl
          'cutlineWhere': gParams('-cwhere', split2), # -cwhere
          'cutlineSQL': gParams('-csql', split2), # -csql
          'cutlineBlend': gParams('-cblend', split2), # -cblend
          'cropToCutline': False, # gParam('-crop_to_cutline', split2) or crop, # -crop_to_cutline
          'copyMetadata': not gBoolParam('-nomd', split2), # -nomd
          'metadataConflictValue': gParams('-cvmd', split2), # -cvmd
          'setColorInterpretation': gBoolParam('-detci', split2), # -detci
          'callback': gParams('-oo', split2), #progress_callback, # -oo
          'callback_data': gParams('-doo', split2), # -doo
          'options': split2} # eg. -overwrite
    # arcpy.AddMessage(f"{WO}")
    # %% GDAL calls
    if cutlineDSName:
        feat = cutlineDSName
        des = arcpy.Describe(feat)
        if des.dataType == 'FeatureClass':
            vctDriver = ogr.GetDriverByName('OpenFileGDB')
            vct = vctDriver.Open(feat)
        elif des.dataType == 'ShapeFile':
            vctDriver = ogr.GetDriverByName('ESRI Shapefile')
            vct = vctDriver.Open(feat)
        else:
            try:
                vct = gdal.OpenEx(feat, gdal.OF_VECTOR)
            except:
                arcpy.AddWarning(f"Can't open {feat}")
                arcpy.AddWarning(f"Final raster will only be clipped to extent of {feat}")
                cutlineDSName = None
                
        extV = des.extent
        #xmin ymin xmax ymax
        WO['outputBounds'] = [extV.XMin, extV.YMin, extV.XMax, extV.YMax]
        
        cutSR = des.SpatialReference
        eCode = cutSR.factoryCode
        cut_SR = osr.SpatialReference()
        validEPSG = cut_SR.ImportFromEPSG(eCode) #returns 0 if code recognized
        if validEPSG != 1:
            arcpy.CreateFeatureclass_management(proj_path,"proj.shp",'POINT',
                                                spatial_reference=cutSR)
            WO['outputBoundsSRS'] = "ESRI::" + os.path.join(proj_path,
                                                            "proj.prj")
        else:
            WO['outputBoundsSRS'] = "EPSG:" + str(eCode)
                

    # Use Translate to clip to outputBounds
    corners = None
    if WO['outputBounds']:
        xmin, ymin, xmax, ymax = WO['outputBounds']
        #package upper left and lower right corner coords for Translate
        corners = [xmin, ymax, xmax, ymin]
        # WO['outputBounds'] = None
        # arcpy.AddMessage(f"Corners: {corners}")
    
    # %% Iterate by folder         
    outPath = outPath.replace('\\','/')
    for i in range(inPaths.rowCount):
        arcpy.SetProgressor('step','Performing GDAL BuildVRT')
        inPath = inPaths.getValue(i,0)
        R = inPaths.getValue(i,1)
        arcpy.AddMessage("________________________________________")
        arcpy.AddMessage(f"Beginning mosaic of {R}")
        start = time.time()

        vo = {'options' : 'overwrite'} #, 'outputBounds' : extent} requires transform
        arcpy.env.workspace = inPath
        rasters = arcpy.ListRasters()
        arcpy.AddMessage(f"{len(rasters)} Raster in folder")
        # heterogeneous projections?
        projs = {}
        for r in rasters:
            inR = inPath + '/' + r
            info = gdal.Info(inR, wktFormat='WKT1', format='json')
            cs = info['coordinateSystem']['wkt']
            
            if subset:
                sr = arcpy.SpatialReference()
                sr.loadFromString(cs)
                ulr, llr, lrr, url, cr = [P(x, y) for x, y in 
                                          info['cornerCoordinates'].values()]
                extPoly = Polygon(Array([ulr, url, lrr, llr, ulr]), sr)
                disjoint = cutG[0].disjoint(extPoly)
                
                if disjoint:
                    continue
            projcs = cs.rsplit(',\n')[0]
            if 'unknown' in projcs:
                projcs = cs
                
            
            # cc = info['cornerCoordinates']
            # vrtIn = (LL_v < UR_vrt).all()
                # vIn = (LL_vrt < UR_v).all()
                # inter = vrtIn and vIn
            if projcs in projs:
                projs[projcs].append(inR)
                # mUR = np.array(transform.TransformPoint(lrx, uly)[0:2])
                # mLL = np.array(transform.TransformPoint(ulx, lry)[0:2])
            else:
                # arcpy.AddMessage(f"Input projection {projcs}")
                # transform = osr.CoordinateTransformation(tSR,iSR)
                projs[projcs] = [inR]
         
        outR = os.path.join(outPath, R + ext).replace('\\','/')
        # ps = len(projcs)
        # arcpy.AddMessage(f"{outR} with {ps} projection{['s'] * ps}")
        tR = []
        # vrts = []
        
        # Build VRT for each projection found in folder
        t = 0
        rCount = 0

        for pr, rasts in projs.items():
            rCount += len(rasts)
            vrt = f"/vsimem/v{t}.vrt" # os.path.join(outPath, f"vii{t}.vrt").replace('\\','/') # f"/vsimem/v{t}.vrt"
            # vrtT = f"/vsimem/vt{t}.vrt" # os.path.join(outPath, f"vtii{t}.vrt").replace('\\','/') # f"/vsimem/vt{t}.vrt"
            vrti = gdal.BuildVRT(destName=vrt, srcDSOrSrcDSTab=rasts, **vo)
            # vrts.append(vrti)
            # I once thought pre-trimming to extent might save processing time
            # But it ultimately trimmed things short. To work, would need to project cut feat to native SRS
            # if WO['cutlineDSName']: 
            #     # extent of raster set
            #     ulx_vrt, xres_vrt, xskew, uly_vrt, yskew, yres_vrt = \
            #         vrti.GetGeoTransform()
            #     lrx_vrt = ulx_vrt + (vrti.RasterXSize * xres_vrt)
            #     lry_vrt = uly_vrt + (vrti.RasterYSize * yres_vrt)
            #     # arcpy.AddMessage(f"ulx: {ulx_vrt} lrx: {lrx_vrt} xres: {xres_vrt}\n"
            #     #                  f"uly: {uly_vrt} lry: {lry_vrt} yres: {yres_vrt}")
                
            #     # iv = gdal.Info(vrti, format='json')
            #     # arcpy.AddMessage(str(iv['cornerCoordinates']))
            #     # Create feature of raster extent
            #     # srV = arcpy.SpatialReference()
            #     # srV.loadFromString(vrti.GetProjectionRef())
            #     # extPoly = Polygon(Array(
            #     #     [P(ulx_vrt, uly_vrt), P(lrx_vrt, uly_vrt),
            #     #      P(lrx_vrt, lry_vrt), P(ulx_vrt, lry_vrt)]), srV)
                
            #     # arcpy.CopyFeatures_management(extPoly, extF)
            #     # Area of intersect between clip feature and raster extent
            #     # Conduct geoprocessing in clip feature spatial reference
            #     # arcpy.env.outputCoordinateSystem = cutSR
            #     # arcpy.Intersect_analysis([cutline, extF], sub, 'ONLY_FID')
            #     # extS = arcpy.Describe(sub).extent
            #     # win = [extS.XMin, extS.YMax, extS.XMax, extS.YMin]
            #     # arcpy.AddMessage(f"{win}")
            #     # winSRS = WO['outputBoundsSRS']
            #     if unionFlag:
            #         arcpy.Append_management(union, sub)
            #     else:
            #         arcpy.CopyFeatures_management(sub, union)
            #         unionFlag = True
            # elif corners:
            #     winSRS = WO['outputBoundsSRS']
            #     # WO['outputBoundsSRS'] = None
            #     win = corners
            # else:
            #     # win = None
            #     winSRS = None
            
            # if win:
            #     to = {'projWinSRS': winSRS, 'projWin': win}
            #     tR.append(gdal.Translate(vrtT, vrti, **to))
            # else:
            tR.append(vrti)
            
            t += 1
        arcpy.AddMessage(f"{rCount} Rasters used")
        if unionFlag:
            extU = arcpy.Describe(union).extent
            #WO['outputBounds'] = [extU.XMin, extU.YMin, extU.XMax, extU.YMax]
            rExtent = os.path.join(outPath, R + '.shp').replace('\\','/')
            arcpy.PairwiseDissolve_analysis(union, rExtent)
            # WO['outputBoundsSRS'] = None
            # WO['cutlineDSName'] = None
        # arcpy.AddMessage(f"Working on {outR}, with inputs {v}")
        if blocky:
            arcpy.AddMessage(f"{len(rasters)} to {rCount}")
            WO['cutlineDSName'] = None
        arcpy.SetProgressor('step','Performing GDAL Warp')
        try:
            if cutlineDSName:
                outVRT = '/vsimem/out.vrt'
                ow = gdal.Warp(outVRT, tR, **WO)
                WO['cutlineDSName'] = cutlineDSName
                WO['resampleAlg'] = 'near'
                ow = gdal.Warp(outR, outVRT, **WO)
            else:
                ow = gdal.Warp(outR, tR, **WO)
            deltaT = time.time() - start
            gm = time.gmtime(deltaT)
            hrs = int(deltaT // day * 24 + gm.tm_hour)
            milliS = round(deltaT % 1, 3)
            arcpy.AddMessage(f"{hrs}:{gm.tm_min}:{gm.tm_sec + milliS}")
        except:
            arcpy.AddWarning(outR)
            arcpy.AddWarning("Unexpected error on line: " +
                   str(sys.exc_info()[-1].tb_lineno))
            arcpy.AddWarning("\n" + str(sys.exc_info()[0]))
            arcpy.AddWarning("\n" + str(sys.exc_info()[1]))
            pass
        ow = None
        tR = None
        vrti = None
        del vrt
        # del vrtT
        arcpy.Delete_management('in_memory/')
except:
    # arcpy.AddError('split2:' + str(split2))
    arcpy.AddError("Unexpected error on line: " +
                   str(sys.exc_info()[-1].tb_lineno))
    arcpy.AddError("\n" + str(sys.exc_info()[0]))
    arcpy.AddError("\n" + str(sys.exc_info()[1]))

# Prepend 'ESRI::' to the prj file path
    # https://github.com/mapbox/node-srs/issues/1
    # https://lists.osgeo.org/pipermail/gdal-dev/2011-May/028728.html
# Gdal progress
    # https://gis.stackexchange.com/questions/237479/using-callback-with-python-gdal-rasterizelayer
# gdal info coordinate system info
    # https://gis.stackexchange.com/questions/267321/extracting-epsg-from-a-raster-using-gdal-bindings-in-python
# OpenFileGDB
    # https://gis.stackexchange.com/questions/32762/how-to-access-feature-classes-in-file-geodatabases-with-python-and-gdal