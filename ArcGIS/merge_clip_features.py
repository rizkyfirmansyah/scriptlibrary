import arcpy
from arcpy import env

path = "D:/DATA/GEOSPATIAL/OPEN_DATA/Burn_Area/Win20/"
env.workspace = path + "burn_area_20.gdb"

os.chdir(path)

clip_features = "indonesia"
for i in range(2000, 2020):
    in_features = []
    out_feature_class = "MCD64_burn_idn_" + i
    in_features.append("MCD64_burn_" + i)
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)