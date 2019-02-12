# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = ""
 
# Set local variables
deleteFeatures = ["FID_idn_fo", "FID_idn__1", "objectid_1", "provinsi_1" "island_1", "province_1", "lulc"]

inFeaturesList = ["papua_forests_09_farea_17.shp", "papua_forests_11_farea_17.shp", "papua_forests_13_farea_17.shp", "papua_forests_15_farea_17.shp", "papua_forests_17_farea_17.shp"]

# Execute delete Fields in looping featureList

for feature in inFeaturesList:
    for d in deleteFeatures:
	    try:
		    arcpy.DeleteField_management(feature, d)
	    except:
		    print(arcpy.GetMessages(2))