# Import system modules
import arcpy
from arcpy import env


arcpy.env.overWriteOutput = True 
# Set environment settings
env.workspace = "E:/GEORESEARCH/Forest and Deforestation/MoEF/forest_net_stock.gdb"
# list your year
year = ["90", "96", "00", "03", "06", "09", "11", "12", "13", "14", "15", "16", "17"]
# Set variables to be deleted
deleteFeatures = ["PL90_ID", "PL96_ID", "PL00_ID", "PL03_ID", "PL06_ID", "PL09_ID", "PL11_ID", "PL12_ID", "PL13_ID", "PL14_ID", "PL15_ID", "ORIG_FID"]

# arcpy.MakeFeatureLayer_management("pl2015", "lyr")
for i, v in enumerate(year):
	outputFile = "forests_" + v
	# select specific ID which are primary and secondary forests
	arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "PL" + v + "_ID" + " IN (2001, 2002, 2004, 20041, 2005, 20051)")

	arcpy.CopyFeatures_management("lyr", outputFile)

	df = deleteFeatures[:]
	del df[i]
	for d in df:
		try:
			arcpy.DeleteField_management(outputFile, d)
		except:
			print(arcpy.GetMessages(2))