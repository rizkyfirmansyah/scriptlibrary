import arcpy
from arcpy import env

workspace = "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Papua/Forest Area/"
inFeature = "idn_forests_06"
inFeatureList = " #;idn_forest_area_2017 #"
outFeature = "papua_forests_06_farea_17.shp"


arcpy.Intersect_analysis(in_features = inFeature + inFeatureList, out_feature_class=workspace + outFeature, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")


""" Looping """

inFeatureLoop = ["idn_forests_09", "idn_forests_11", "idn_forests_13", "idn_forests_15", "idn_forests_17"]
outFeatureLoop = ["papua_forests_09_farea_17.shp", "papua_forests_11_farea_17.shp", "papua_forests_13_farea_17.shp", "papua_forests_15_farea_17.shp", "papua_forests_17_farea_17.shp"]

for f in inFeatureLoop:
    for g in outFeatureLoop:
        arcpy.Intersect_analysis(in_features = f + inFeatureList, out_feature_class=workspace + g, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")