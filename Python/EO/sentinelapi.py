# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:04:20 2019

@author: Rizky Firmansyah
"""

import geopandas as gpd
from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
import matplotlib.pyplot as plt
import zipfile

aoi = r'D:\Universe\GEOSPATIAL DATA\OPEN DATA\Sentinel\tes.geojson'

user = 'rizkyfirmansyah'
password = 'WRIesa2018!'


api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

footprint = geojson_to_wkt(read_geojson(aoi))

products = api.query(footprint,
                     date = ('20190225', '20190227'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0, 80))

#print(len(products))

areas = api.to_geodataframe(products)

areas.plot(column = 'uuid', cmap=None)

ax = areas.plot(column = 'uuid', cmap=None, figsize=(20,20))
areas.apply(lambda x: ax.annotate(s=x.uuid, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)

# use geopandas to check which scene to download
gdf2 = gpd.read_file(aoi)
f, ax = plt.subplots(1)
areas.plot(ax=ax, column='uuid', cmap=None)
gdf2.plot(ax=ax)
plt.show()

data = api.download('1b1c9990-7c77-4619-a2fe-0af13d2791f5')

path_tozip = data['path']

zip_ref = zipfile.ZipFile(path_tozip, 'r')
zip_ref.extractall(r'D:\Universe\GEOSPATIAL DATA\OPEN DATA\Sentinel')
zip_ref.close()