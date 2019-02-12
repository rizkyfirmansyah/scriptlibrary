# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = ""
 
# Set local variables

fieldName1 = "lulc"
fieldPrecision = 50
fieldType = "TEXT"

fieldName2 = "lulc_name"
fieldName3 = "foresttype"

fieldName4 = "ha"
fieldType2 = "DOUBLE"

inFeatures = "idn_forests_11"

inFeaturesList = ["idn_forests_11", "idn_forests_13", "idn_forests_15"]
 
# Execute AddField in looping featureList
for feature in inFeaturesList:
    arcpy.AddField_management(feature, fieldName1, fieldType, fieldPrecision, "", "", "", "")
    arcpy.AddField_management(feature, fieldName2, fieldType, fieldPrecision)
    arcpy.AddField_management(feature, fieldName3, fieldType, fieldPrecision)
    arcpy.AddField_management(feature, fieldName4, fieldType2)