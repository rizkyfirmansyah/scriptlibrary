# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:04:20 2019

@author: Rizky Firmansyah
"""

import geopandas as gpd
import os
from sentinelsat.sentinel import SentinelAPI
import matplotlib.pyplot as plt
import zipfile
from time import sleep

# Set working directory
path = "D:/Universe/GEOSPATIAL DATA/OPEN DATA/Sentinel"
os.chdir(path)

# 541 tiles over Indonesia
tileSentinel = gpd.read_file("s2_tile_indo.shp")
queryTileSentinel = tileSentinel[tileSentinel.Name == '52NGG']
all_wkt = [g.wkt for g in tileSentinel['geometry'].values]
query_geom = [g.wkt for g in queryTileSentinel['geometry'].values]

# 493 tiles
tile = gpd.read_file("tile_100km.shp")
geom = [g.wkt for g in tile['geometry'].values]

cre = {'u': 'rizkyfirmansyah', 'p': 'WRIesa2018!'}

## Set your query parameters here
CC = 100
sentinelLevel1 = 'Level-1C'
sentinelLevel2 = 'Level-2A'
a1 = '20180101'
#t2 = '20190516'
a2 = '20181231'

api = SentinelAPI(cre['u'], cre['p'], 'https://scihub.copernicus.eu/dhus')

products1 = ""
products2 = ""

def sentinel_metadata(d, e):
        """
        d for selecting your Sentinel product
        while e for creating a new file containing title, date and cloud coverage
        """
        header = ['filename', 'begin_position', 'cloud_cover', 'size', 'orbit']
        line_count = 0
        for key in d.keys():
            for v in key.split():
                title = d[v]['title']
                date = d[v]['beginposition']
                cc = d[v]['cloudcoverpercentage']
                size = d[v]['size']
                orbit = d[v]['orbitdirection']
                f = None
                try:
                    with open(e, "a") as f:
                        if line_count == 0:
                            print(header[0], header[1], header[2], header[3], header[4], sep=', ', file = f)
                            line_count += 1
                        else:
                            print(title, date, cc, size, orbit, sep=', ', file = f)
                            line_count += 1
                finally:
                    if f is not None:
                        f.close()
            f.close()

def download_metadata(t1, t2, l1 = True, l2 = False):
    """ Download metadata Sentinel 2 either L1A or L2C"""

    global products1
    global products2
    # n starts with 0
    n = 0
    while n < len(geom):
        products1 = api.query(geom[n],
                             date = (t1, t2),
                             platformname = 'Sentinel-2',
                             processinglevel = sentinelLevel1,
                             cloudcoverpercentage = (0, CC))
        
        products2 = api.query(geom[n],
                             date = (t1, t2),
                             platformname = 'Sentinel-2',
                             processinglevel = sentinelLevel2,
                             cloudcoverpercentage = (0, CC))
        try:
            if l1 == True and l2 == True:
                sentinel_metadata(products1, 'Sentinel2_' + sentinelLevel1 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
                sentinel_metadata(products2, 'Sentinel2_' + sentinelLevel2 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
            elif l1 == True:
                sentinel_metadata(products1, 'Sentinel2_' + sentinelLevel1 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
            elif l2 == True:
                sentinel_metadata(products2, 'Sentinel2_' + sentinelLevel2 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
        except:
            sleep(30)

        n += 1

areas = api.to_geodataframe(products1)

def view_aoi():
    """ Return the Sentinel tiles over the area of interest. Choose the products either L1C or L2A"""
    areas.plot(column = 'uuid', cmap=None)
    
    ax = areas.plot(column = 'uuid', cmap=None, figsize=(20,20))
    areas.apply(lambda x: ax.annotate(s=x.uuid, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)

def scene_download():
    """ use geopandas to check which scene to download """
    gdf2 = gpd.read_file(geom)
    f, ax = plt.subplots(1)
    areas.plot(ax=ax, column='uuid', cmap=None)
    gdf2.plot(ax=ax)
    plt.show()

def download_data():
    """ download all the data. Choose the download_all either Level 1C or Level 2A"""
    # n starts with 0
    n = 0
    while n < len(geom):
        try:
            data = api.download_all(products1)
            
            path_tozip = data['path']
            
            zip_ref = zipfile.ZipFile(path_tozip, 'r')
            zip_ref.extractall(r'D:/DATA/GEOSPATIAL/OPEN DATA/Sentinel')
            zip_ref.close()
        except:
            print("There's something wrong with your connection")

