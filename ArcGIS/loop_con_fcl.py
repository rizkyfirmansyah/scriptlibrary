import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "W:/GEORESEARCH/West Borneo Deforestation and Peat Fires/Result/bs_peat.gdb/"
dir = "W:/GEORESEARCH/West Borneo Deforestation and Peat Fires/Result/bs_peat.gdb/"

for i in range(1,18,1):
	if i < 10:
		arcpy.gp.Con_sa("burnt_scar_peat_200" + str(i) + ".tif", "burnt_scar_peat_200" + str(i) + ".tif", dir + "bs_200" + str(i), "", '"Value" > 0')
	else:
		arcpy.gp.Con_sa("burnt_scar_peat_20" + str(i) + ".tif", "burnt_scar_peat_20" + str(i) + ".tif", dir + "bs_20" + str(i), "", '"Value" > 0')
		
		

		
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "W:/GEORESEARCH/West Borneo Deforestation and Peat Fires/Result/bs_peat.gdb/"
dir = "W:/GEORESEARCH/West Borneo Deforestation and Peat Fires/Result/bs_peat.gdb/"

for i in range(1,11,1):
	if i < 10:
		arcpy.AddField_management(in_table="bs_201" + str(i), field_name="Year", field_type="SHORT", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")

		arcpy.CalculateField_management(in_table="bs_201" + str(i), field="Year", expression="201" + str(i), expression_type="PYTHON_9.3", code_block="")
	else:
		arcpy.AddField_management(in_table="bs_20" + str(i), field_name="Year", field_type="SHORT", field_precision="", field_scale="", field_length="", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")


		arcpy.CalculateField_management(in_table="bs_20" + str(i), field="Year", expression="20" + str(i), expression_type="PYTHON_9.3", code_block="")