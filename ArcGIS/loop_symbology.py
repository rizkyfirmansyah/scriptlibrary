import arcpy
arcpy.ApplySymbologyFromLayer_management("in_layer", "in_symbology_layer")


import arcpy
from arcpy import env

# Set the current workspace
env.workspace = "W:/GEORESEARCH/West Borneo Deforestation and Peat Fires/Result/bs_peat.gdb/"

# Set layer to apply symbology to
inputLayers = ["in_layer_first.lyr","in_layer_second.lyr","in_layer_third.lyr"]

# Set layer that output symbology will be based on
symbologyLayer = "in_symbology_layer.lyr"

# Apply the symbology from the symbology layer to the input layer
for layer in inputLayers:
	arcpy.ApplySymbologyFromLayer_management (layer, symbologyLayer)
	

# Import arcpy module
import arcpy

for i in range(2000,2018,1):
	arcpy.ApplySymbologyFromLayer_management(in_layer="bs_" + str(i), in_symbology_layer="bs_2016")