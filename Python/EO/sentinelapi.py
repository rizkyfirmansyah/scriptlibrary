# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:04:20 2019

@author: Rizky Firmansyah
"""
for name in dir():
    if not name.startswith('_'):
        del globals()[name]

import geopandas as gpd
import os
from sentinelsat.sentinel import SentinelAPI
import matplotlib.pyplot as plt
import zipfile
from time import sleep

# Set working directory
path = "D:/Universe/GEOSPATIAL DATA/OPEN DATA/Sentinel"
os.chdir(path)

# 493 tiles
tile = gpd.read_file("tile_100km.shp")
geom = [g.wkt for g in tile['geometry'].values]

cre = {'u': 'rizkyfirmansyah', 'p': 'WRIesa2018!'}

## Set your query parameters here
CC = 100
sentinelLevel1 = 'Level-1C'
sentinelLevel2 = 'Level-2A'
#a1 = '20180101'
t2 = '20181101'
a2 = '20181231'

api = SentinelAPI(cre['u'], cre['p'], 'https://scihub.copernicus.eu/dhus')

products1 = ""
products2 = ""
sentinel = {}

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

def api_products(t1, t2, n):
    """ API products for Sentinel L1A or L2C"""
    global sentinel
    l1 = api.query(geom[n],
                         date = (t1, t2),
                         platformname = 'Sentinel-2',
                         processinglevel = sentinelLevel1,
                         cloudcoverpercentage = (0, CC))
    
    l2 = api.query(geom[n],
                         date = (t1, t2),
                         platformname = 'Sentinel-2',
                         processinglevel = sentinelLevel2,
                         cloudcoverpercentage = (0, CC))
    
    sentinel = {0: l1, 1: l2}

    return sentinel
        
def download_metadata(t1, t2, l1 = True, l2 = False):
    """ """
    
    # n starts with 0
    n = 0
    while n < len(geom):
        api_products(t1, t2, n)
        try:
            if l1 == True and l2 == True:
                sentinel_metadata(sentinel[0], 'Sentinel2_' + sentinelLevel1 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
                sentinel_metadata(sentinel[1], 'Sentinel2_' + sentinelLevel2 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
            elif l1 == True:
                sentinel_metadata(sentinel[0], 'Sentinel2_' + sentinelLevel1 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
            elif l2 == True:
                sentinel_metadata(sentinel[1], 'Sentinel2_' + sentinelLevel2 + '_' + t1 + '_' + t2 + '_' + 'tile' + str(n+1) + '.csv')
        except:
            sleep(30)
            
        n += 1


def view_aoi(n):
    """ Default to set n = 0 """
    
    n = 0
    areas1 = api.to_geodataframe(sentinel(n)[0])
    areas2 = api.to_geodataframe(sentinel(n)[1])
    """ Return the Sentinel tiles over the area of interest. Choose the products either L1C or L2A"""
    areas1.plot(column = 'uuid', cmap=None)
    areas2.plot(column = 'uuid', cmap=None)
    
    ax = areas1.plot(column = 'uuid', cmap=None, figsize=(20,20))
    areas1.apply(lambda x: ax.annotate(s=x.uuid, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)

def scene_download(n):
    """ use geopandas to check which scene to download """
    
    n = 0
    areas1 = api.to_geodataframe(sentinel(n)[0])
#    areas2 = api.to_geodataframe(sentinel(n)[1])
    
    gdf2 = gpd.read_file(geom)
    f, ax = plt.subplots(1)
    areas1.plot(ax=ax, column='uuid', cmap=None)
    gdf2.plot(ax=ax)
    plt.show()

def download_data(t1, t2, l1 = True, l2 = False):
    """ download all the data. Choose the download_all either Level 1C or Level 2A
        Level 1C - s2 = products1
        Level 2A - s2 = products2
    """
    download_path = 'D:/DATA/GEOSPATIAL/OPEN DATA/Sentinel'
    # n starts with 0
    n = 0
    while n < len(geom):
        api_products(t1, t2, n)
        try:
            # This would be archive two Sentinels into one single zip file
            if l1 == True and l2 == True:
                data = api.download_all(sentinel[0])
                data2 = api.download_all(sentinel[1])
                path_tozip1 = data['path']
                path_tozip2 = data2['path']
                download = list(path_tozip1, path_tozip2)
                try:
                    with zipfile.ZipFile(path_tozip1, 'w') as z:
                        for f in download:
                            z.write(download_path + f)
                except FileNotFoundError:
                    print("An error occured")
                finally:
                    z.close()
            elif l1 == True:
                data = api.download_all(sentinel[0])
                path_tozip = data['path']
                
                zip_ref = zipfile.ZipFile(path_tozip, 'r')
                zip_ref.extractall(download_path)
                zip_ref.close()
            elif l2 == True:
                data = api.download_all(sentinel[1])
                path_tozip = data['path']
                
                zip_ref = zipfile.ZipFile(path_tozip, 'r')
                zip_ref.extractall(download_path)
                zip_ref.close()
                
        except:
            sleep(30)
    
        n += 1
