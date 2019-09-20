
# Import system modules
import arcpy
 
# Set local variables

fieldName1 = "year"
fieldPrecision = 50
fieldType = "SHORT"

del_field = "year"

inFeaturesList = ["MCD64_burn_idn_2013", "MCD64_burn_idn_2012", "MCD64_burn_idn_2011", "MCD64_burn_idn_2010", "MCD64_burn_idn_2009", "MCD64_burn_idn_2008", "MCD64_burn_idn_2007", "MCD64_burn_idn_2006", "MCD64_burn_idn_2005", "MCD64_burn_idn_2004", "MCD64_burn_idn_2003", "MCD64_burn_idn_2002", "MCD64_burn_idn_2001"]
years = [2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001] 
 
# Execute AddField in looping featureList
for idx, feature in enumerate(inFeaturesList):
    try:
        arcpy.AddField_management(feature, fieldName1, fieldType, fieldPrecision, "", "", "", "")
        arcpy.CalculateField_management(feature, "year", years[idx], "PYTHON_9.3", "")
    except:
        print(arcpy.GetMessages(2))