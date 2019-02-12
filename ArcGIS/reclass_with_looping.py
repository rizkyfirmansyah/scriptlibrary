# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = ""
 
inFeaturesList = ["idn_forests_00", "idn_forests_03", "idn_forests_06", "idn_forests_09", "idn_forests_11", "idn_forests_13", "idn_forests_15", "idn_forests_17"]

# Define land use land cover class
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
    elif y == 2007:
        return 'Bush / Shrub'
    elif y == 2010:
        return 'Estate Crop Plantation'
    elif y == 2012:
        return 'Settlement Area'
    elif y == 2014:
        return 'Bare Land'
    elif y == 2500:
        return 'Cloud'
    elif y == 3000:
        return 'Savannah'
    elif y == 5001:
        return 'Bodies of Water'
    elif y == 20071:
        return 'Swamp Shrub'
    elif y == 20091:
        return 'Dryland Agriculture'
    elif y == 20092:
        return 'Shrub-Mixed Dryland Farm'
    elif y == 20093:
        return 'Rice Field'
    elif y == 20094:
        return 'Fish Pond'
    elif y == 20121:
        return 'Airport	/ Harbour'
    elif y == 20122:
        return 'Transmigration Area'
    elif y == 20141:
        return 'Open-pit Mining'
    elif y == 50011:
        return 'Swamp'
    else:
        return ''"""
		
codeblockForestType = """def reclass(y):
    if y == 2006:
        return 'Non Forest'
    elif y == 2001:
        return 'Primary Forests'
    elif y == 2002:
        return 'Secondary Forests'
    elif y == 2004:
        return 'Primary Forests'
    elif y == 20041:
        return 'Secondary Forests'
    elif y == 2005:
        return 'Primary Forests'
    elif y == 20051:
        return 'Secondary Forests'
    elif y == 2007:
        return 'Non Forest'
    elif y == 2010:
        return 'Non Forest'
    elif y == 2012:
        return 'Non Forest'
    elif y == 2014:
        return 'Non Forest'
    elif y == 2500:
        return 'Non Forest'
    elif y == 3000:
        return 'Non Forest'
    elif y == 5001:
        return 'Non Forest'
    elif y == 20071:
        return 'Non Forest'
    elif y == 20091:
        return 'Non Forest'
    elif y == 20092:
        return 'Non Forest'
    elif y == 20093:
        return 'Non Forest'
    elif y == 20094:
        return 'Non Forest'
    elif y == 20121:
        return 'Non Forest'
    elif y == 20122:
        return 'Non Forest'
    elif y == 20141:
        return 'Non Forest'
    elif y == 50011:
        return 'Non Forest'
    else:
        return ''"""

fieldName1 = "lulc_name"
fieldName2 = "foresttype"
inField1 = "lc_code"
expression = "reclass(!lc_code!)"

# arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON_9.3", codeblock)
 
# Execute AddField in looping featureList
"""
for feature in inFeaturesList:
    try:
        arcpy.CalculateField_management(feature, fieldName1, expression, "PYTHON_9.3", codeblockLU)
    except:
        print(arcpy.GetMessages(2))
"""
for feature in inFeaturesList:
    try:
        arcpy.CalculateField_management(feature, fieldName2, expression, "PYTHON_9.3", codeblockForestType)
    except:
        print(arcpy.GetMessages(2))