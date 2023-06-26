# Import system modules and
# Set layer to apply symbology
import arcpy
in_layer = arcpy.GetParameterAsText(0)
arcpy.management.ApplySymbologyFromLayer(in_layer, r"C:\GIS_Training\ArcPro_templates\Tennessee_Conservation_Planner_Pro_Template_v1\Layers\Reference_layers\NPAD Points.lyrx", "VALUE_FIELD Practice_Name PracticeNa", "DEFAULT")
