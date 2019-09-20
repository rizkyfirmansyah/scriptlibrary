# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:42:57 2019

@author: rizky
"""

import os, subprocess, glob, sys, shutil
from tqdm import tqdm
sys.path.append('C:\\Program Files\\QGIS 3.8\\bin')

path = 'D:/DATA/GEOSPATIAL/MINISTRY/MOEF/UPDATED-JULY2019/kws_hutan/geojson/'
shp_path = os.path.join(path, 'shapefile')
os.chdir(path)

geojson_files = [f for f in glob.glob(path + "*.geojson", recursive=True)]

if not os.path.exists(shp_path):
    os.makedirs('shapefile')
    
n = 0
pbar = tqdm(total=len(geojson_files), initial = n)
while n < len(geojson_files):
    subprocess.call('ogr2ogr -f "ESRI Shapefile" shapefile/' + os.path.basename(geojson_files[n]).replace("geojson", "shp") + ' ' + geojson_files[n], shell=True)
    pbar.update(1)
    n += 1
pbar.close()

shp_files = [f for f in glob.glob(shp_path + "*.shp", recursive=True)]

m = 0
pbar = tqdm(total=len(shp_files), initial = m)
while m < len(shp_files):
    subprocess.call('ogr2ogr -f "ESRI Shapefile" -append -update ' + os.path.join(path, 'merged.shp') + ' ' + shp_files[m], shell=True)
    pbar.update(1)
    m += 1
pbar.close()

# delete the folder eventually
shutil.rmtree(shp_path)

"""
References:
    https://gis.stackexchange.com/questions/223183/ogr2ogr-merge-multiple-shapefiles-what-is-the-purpose-of-nln-tag
    https://gis.stackexchange.com/questions/236746/calling-gdal-merge-into-python-script
"""