# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = ""
 
# Set local variables

fieldName1 = "lu_bef"
fieldPrecision = 100
fieldType = "TEXT"

fieldName2 = "lu_aft"

inFeaturesList = ["indoprov_deg_14_15", "indoprov_deg_13_14", "indoprov_deg_12_13", "indoprov_deg_11_12", "indoprov_deg_09_11", "indoprov_deg_06_09", "indoprov_deg_03_06", "indoprov_deg_00_03", "indoprov_deg_96_00", "indoprov_deg_90_96"]


codeblockLU = """def reclass(y):
    if y == 2006:
        return 'Plantation Forest'
    elif y == 2001:
        return 'Primary Dry Land Forest'
    elif y == 2002:
        return 'Secondary Dry Land Forest'
    elif y == 2004:
        return 'Primary Mangrove Forest'
    elif y == 20041:
        return 'Secondary Mangrove Forest'
    elif y == 2005:
        return 'Primary Swamp Forest'
    elif y == 20051:
        return 'Secondary Swamp Forest'
    else:
        return ''
		"""
		
PL_ID = ["PL15_ID", "PL14_ID", "PL13_ID", "PL12_ID","PL11_ID", "PL09_ID","PL06_ID", "PL03_ID","PL00_ID", "PL96_ID", "PL90_ID"]
 
# Execute AddField in looping featureList
for feature in inFeaturesList:
    if feature == "indoprov_deg_14_15":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[1]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[0]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_13_14":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[2]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[1]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_12_13":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[3]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[2]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_11_12":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[4]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[3]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_09_11":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[5]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[4]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_06_09":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[6]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[5]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_03_06":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[7]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[6]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_00_03":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[8]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[7]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_96_00":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[9]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[8]+"!)", "PYTHON_9.3", codeblockLU)
    elif feature == "indoprov_deg_90_96":
        arcpy.CalculateField_management(feature, fieldName1, "reclass(!"+PL_ID[10]+"!)", "PYTHON_9.3", codeblockLU)
        arcpy.CalculateField_management(feature, fieldName2, "reclass(!"+PL_ID[9]+"!)", "PYTHON_9.3", codeblockLU)
