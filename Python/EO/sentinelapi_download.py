#!/usr/bin/env python
# coding: utf-8

# In[1]:


# @author: Rizky Firmansyah


# In[2]:


import geopandas as gpd
import os
from sentinelsat.sentinel import SentinelAPI
import matplotlib.pyplot as plt
import zipfile
import folium
from time import sleep


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


path = 'download'
os.chdir(path)


# ### There are 493 tiles within shapefile

# In[5]:


tile = gpd.read_file(r"../tile_100km.shp")
geom = [g.wkt for g in tile['geometry'].values]


# In[6]:


cre = {'u': '', 'p': ''}


# ### Set your query parameters here

# In[7]:


CC = 100
sentinelLevel1 = 'Level-1C'
sentinelLevel2 = 'Level-2A'
t1 = '20190101'
t2 = '20190131'


# In[8]:


api = SentinelAPI(cre['u'], cre['p'], 'https://scihub.copernicus.eu/dhus')


# In[9]:


products1 = ""
products2 = ""
sentinel = {}


# #### Run along the function sentinel_metadata if you would like to obtain its metadata

# In[10]:


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


# #### Run api_products function before generating download query

# In[11]:


def api_products(t1, t2, n):
    """ API products for Sentinel L1A or L2C. t1 refers to earlier date and t2 is the latest."""
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


# In[12]:


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


# In[ ]:


# You can view the Sentinel-2 intersects with your shapefile with view_aoi function below


# In[13]:


def view_aoi(t1, t2, n=0, s=0):
    """ Default to set n = 0 and s = 0.
        s = 0 means Level 1-C and s = 1 means Level 2-A
    """
    
    api_products(t1, t2, n)
    areas = api.to_geodataframe(sentinel.get(s))
    """ Return the Sentinel tiles over the area of interest. Choose the products either L1C or L2A"""
    areas.plot(column = 'uuid', cmap=None)
    
    ax = areas.plot(column = 'uuid', cmap=None, figsize=(20,20))
    areas.apply(lambda x: ax.annotate(s=x.uuid, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)


# In[14]:


view_aoi(t1, t2, 190)


# In[15]:


def scene_download(t1, t2, n=0, s=0):
    """ use geopandas to check which scene to download.
        Default to set n = 0 and s = 0.
        s = 0 means Level 1-C and s = 1 means Level 2-A
    """
    
    api_products(t1, t2, n)
    
    areas = api.to_geodataframe(sentinel.get(s))
    tile_center = tile[tile.Id == str(n+1)].geometry.centroid[0]
    
    tile_location = [tile_center.y, tile_center.x]
    
    #f, ax = plt.subplots(1)
    #areas.plot(ax=ax, column='uuid', cmap=None)
    #tile[tile.Id == str(n+1)].plot(ax=ax)
    
    m = folium.Map(location = tile_location, zoom_start = 8)
    folium.GeoJson(tile[tile.Id == str(n+1)].geometry.to_json(),
                  name='Filtered Tile',
                  smooth_factor=2,
                  style_function=lambda x: {'color':'black','fillColor':'transparent','weight':2}).add_to(m)
    
    cols = ['title', 'filename', 'size', 'geometry', 'cloudcoverpercentage']
    scene = areas.loc[:, cols]
    folium.GeoJson(scene.to_json(),
                  name="Downloaded Scene",
                  smooth_factor=2,
                  style_function=lambda x: {'color':'red','fillColor':'transparent','weight':2, 'opacity': 0.7},
                    tooltip=folium.GeoJsonTooltip(fields=['title', 'size'],
                             aliases=['Title', 'Size (MB)'],
                             labels=True,
                             sticky=True,
                             localize=True)).add_to(m)
    folium.LayerControl(autoZIndex=False).add_to(m)
    return m


# In[16]:


scene_download(t1, t2, 190)


# In[17]:


def download_data(t1, t2, l1 = True, l2 = False):
    
    """ download all the data. Choose the download_all either Level 1C or Level 2A
        Level 1C - s2 = products1
        Level 2A - s2 = products2
    """
    
    download_path = ''
    # n starts with 0
    n = 0
    
    # AOI = geom file; iterating through each tile attributes
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

                with zipfile.ZipFile(path_tozip, 'w') as z:
                    z.write(download_path + path_tozip, zipfile.ZIP_DEFLATED)
                zip_ref.close()
            elif l2 == True:
                data = api.download_all(sentinel[1])
                path_tozip = data['path']
                
                with zipfile.ZipFile(path_tozip, 'w') as z:
                    z.write(download_path + path_tozip, zipfile.ZIP_DEFLATED)
                zip_ref.close()
                
        except:
            sleep(30)
    
        n += 1


# #### Run the function download_data to start downloading Sentinel. Specify the earlier and later date. Sentinel Level 1-C is a default option to be downloaded, otherwise specify l1 = False and l2=True if you wish to download only Level 2-A

# In[18]:


# download_data('20190501', '20190505')


# In[19]:


"""
References:
https://sentinelsat.readthedocs.io/en/v0.12/api.html
http://www.acgeospatial.co.uk/sentinelsat_demo/
"""

