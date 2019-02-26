# Import system modules
import arcpy
 
# Set local variables

fieldName1 = "year"
fieldPrecision = 50
fieldType = "TEXT"

inFeaturesList = ["papua_forests_17_farea_17_class", "papua_forests_15_farea_17_class", "papua_forests_13_farea_17_class", "papua_forests_11_farea_17_class", "papua_forests_09_farea_17_class", "papua_forests_06_farea_17_class", "papua_forests_03_farea_17_class", "papua_forests_00_farea_17_class"]
 
# Execute AddField in looping featureList
for feature in inFeaturesList:
    arcpy.AddField_management(feature, fieldName1, fieldType, fieldPrecision, "", "", "", "")
	
years = ['2017', '2015', '2013', '2011', '2009', '2006', '2003', '2000'] 
	
for idx, feature in enumerate(inFeaturesList):
    try:
        arcpy.CalculateField_management(feature, "year", years[idx], "PYTHON_9.3", "")
    except:
        print(arcpy.GetMessages(2))