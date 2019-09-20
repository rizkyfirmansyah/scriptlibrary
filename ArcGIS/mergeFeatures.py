# Import the system modules
import arcpy
import glob
import os
from arcpy import env

path = "D:/DATA/GEOSPATIAL/OPEN_DATA/Burn_Area/Win19/"
env.workspace = path + "burn_area_19_20.gdb"

os.chdir(path)
directory = os.listdir(path)
i = 1

clip_features = "indonesia"

while i < len(directory):
    files = [f for f in glob.glob(path + directory[i] + "/" + "*"+ directory[i] +"*.shp")]
    j = 0
    inFeatures = []
    while j < len(files):
        inFeatures.append(files[j])
        j += 1
    outFeatures = "MCD64_burn_" + directory[i]
    arcpy.Merge_management(inFeatures, outFeatures)
    
    # removing list after successfully merge
    del inFeatures[:]
    
    # clipping merge features within Indonesia
    out_feature_class = "D:/DATA/GEOSPATIAL/OPEN_DATA/Burn_Area/burn_area_idn.gdb/MCD64_burn_idn_" + directory[i]
    arcpy.Clip_analysis(outFeatures, clip_features, out_feature_class)
    
    i += 1