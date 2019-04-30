# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:04:20 2019

@author: Rizky Firmansyah
"""

import geopandas as gpd
import os
from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
import matplotlib.pyplot as plt
import zipfile

# Set working directory
path = "D:/DATA/GEOSPATIAL/OPEN DATA/Sentinel"
os.chdir(path)

aoi = r'tes.geojson'
tileSentinel = gpd.read_file("s2_tile_indo.shp")
#shapefile = tileSentinel[tileSentinel.Name == '49NGA']
all_wkt = [g.wkt for g in tileSentinel['geometry'].values]

user = 'rizkyfirmansyah'
password = 'WRIesa2018!'

## Set your query parameters here
CC = 100
sentinelLevel2 = 'Level-2A'
sentinelLevel1 = 'Level-1C'
t1 = '20180101'
t2 = '20181231'

api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
footprint = geojson_to_wkt(read_geojson(aoi))

# 541 tiles over Indonesia

products1 = api.query(all_wkt[247],
                     date = (t1, t2),
                     platformname = 'Sentinel-2',
                     processinglevel = sentinelLevel1,
                     cloudcoverpercentage = (0, CC))

products2 = api.query(all_wkt[247],
                     date = (t1, t2),
                     platformname = 'Sentinel-2',
                     processinglevel = sentinelLevel2,
                     cloudcoverpercentage = (0, CC))

#print(len(products))

def sentinel_metadata(d, e):
    for key in d.keys():
        with open(e, "a") as f:
            for v in key.split():
                title = d[v]['title']
                date = d[v]['ingestiondate']
                cc = d[v]['cloudcoverpercentage']
                print(title, date, cc, sep=', ', file = f)
                
    f.close()


#areas = api.to_geodataframe(products)
#
#areas.plot(column = 'uuid', cmap=None)
#
#ax = areas.plot(column = 'uuid', cmap=None, figsize=(20,20))
#areas.apply(lambda x: ax.annotate(s=x.uuid, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)
#
## use geopandas to check which scene to download
#gdf2 = gpd.read_file(aoi)
#f, ax = plt.subplots(1)
#areas.plot(ax=ax, column='uuid', cmap=None)
#gdf2.plot(ax=ax)
#plt.show()
#
## download all the data
#data = api.download_all(products)
#
#path_tozip = data['path']
#
#zip_ref = zipfile.ZipFile(path_tozip, 'r')
#zip_ref.extractall(r'D:/DATA/GEOSPATIAL/OPEN DATA/Sentinel')
#zip_ref.close()