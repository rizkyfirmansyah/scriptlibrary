#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %load sentinel.py
"""
Created on Wed May 22 16:48:01 2019

@author: Rizky Firmansyah
"""

import geopandas as gpd
import os
import pandas as pd
import numpy as np
import folium as f


# In[2]:
path = r'D:\Universe\GEOSPATIAL DATA\OPEN DATA\Sentinel'
os.chdir(path)

s1 = pd.read_csv('Sentinel2_Level-1C_2015_2019.csv', skipinitialspace=True)
s2 = pd.read_csv('Sentinel2_Level-2A_2018_2019.csv', skipinitialspace=True)

## Create a row index
s1['rowid'] = np.arange(len(s1))
s2['rowid'] = np.arange(len(s2))

## Rename column name in order to join the table
s1.columns = ['filename', 'begin_position', 'cloud_cover', 'size', 'orbit', 'Id', 'year', 'rowid']
s2.columns = ['filename', 'begin_position', 'cloud_cover', 'size', 'orbit', 'Id', 'year', 'rowid']

# removing MB in the size column and converting to numeric
s1['size'] = pd.to_numeric(s1['size'].apply(lambda x: x[:-3]))
s2['size'] = pd.to_numeric(s2['size'].apply(lambda x: x[:-3]))


# In[3]:


# Finding the duplicate
duplicateS1 = s1[s1.duplicated(['filename', 'size', 'year', 'cloud_cover'])]
duplicateS2 = s2[s2.duplicated(['filename', 'size', 'year', 'cloud_cover'])]


## How many clean scenes over Indonesia
s1_clean = s1[~s1['rowid'].isin(duplicateS1['rowid'])]
s2_clean = s2[~s2['rowid'].isin(duplicateS1['rowid'])]


# In[4]:


def aggregate(g = 'Id', c = 'size', v = 'sum'):
    """ Aggregation group by and returning the sum/max/min function in dictionary
        You can modify the g = year
        c = cloud_cover
        v = min/sum/max
    """
    
    s = {}
    
    s1 = s1_clean.groupby(g)[c].agg(v)
    s2 = s2_clean.groupby(g)[c].agg(v)
    s1['GB'] = s1_clean.groupby(g)[c].agg(v) / 1000
    s2['GB'] = s2_clean.groupby(g)[c].agg(v) / 1000
    s = {'sentinel2L1C': s1, 'sentinel2L2A': s2}
    
    return s


# In[5]:


## Aggregate by Cloud Filter Function

def aggregate_by_cloud(cc1 = 0, cc2 = 100, g = 'Id', c = 'size', v = 'sum'):
    """ Aggregation group by filtering the cloud cover threshold first then returning the sum/max/min function in dictionary
        By default: Minimum Cloud Cover (cc1) = 0 and Maximum Cloud Cover (cc2) = 100
        You can modify the g = year
        c = cloud_cover
        v = min/sum/max
    """
    s = {}
    
    s1 = s1_clean[(s1_clean['cloud_cover'] >= cc1) & (s1_clean['cloud_cover'] <= cc2)].groupby(g)[c].agg(v)
    s2 = s2_clean[(s2_clean['cloud_cover'] >= cc1) & (s2_clean['cloud_cover'] <= cc2)].groupby(g)[c].agg(v)
    s1['GB'] = s1_clean[(s1_clean['cloud_cover'] >= cc1) & (s1_clean['cloud_cover'] <= cc2)].groupby(g)[c].agg(v) / 1000
    s2['GB'] = s2_clean[(s2_clean['cloud_cover'] >= cc1) & (s2_clean['cloud_cover'] <= cc2)].groupby(g)[c].agg(v) / 1000
    s = {'sentinel2L1C': s1, 'sentinel2L2A': s2}
    
    return s


# In[6]:


## How much the total size (GB) of Sentinel 2 Level 1-C on each Tile ID
aggregate().get('sentinel2L1C')['GB']


# In[7]:


## How much the total size (GB) of Sentinel 2 Level 1-C by Tile ID
aggregate().get('sentinel2L1C')['GB'][2]


# In[8]:


## How much the total size (GB) of Sentinel 2 Level 1-C in a total from 2015-06 to 2019-05-18?
aggregate().get('sentinel2L1C')['GB'].sum()


# In[9]:


## How much the total size (GB) of Sentinel 2 Level 2-A on each Tile ID
aggregate().get('sentinel2L2A')['GB']


# In[10]:


## How much the total size (GB) of Sentinel 2 Level 2-A in a total from 2018-11 to 2019-05-18?
aggregate().get('sentinel2L2A')['GB'].sum()


# In[11]:


## What about the total size (GB) on each year in Sentinel 2 Level 1-C?

aggregate(g = 'year').get('sentinel2L1C')['GB']


# In[12]:


## What about the total size (GB) on each year in Sentinel 2 Level 2-A?

aggregate(g = 'year').get('sentinel2L2A')['GB']


# In[13]:

# How much a total size (GB) filtered by cloud CC >= 0 and CC <= 30 in Sentinel 2 Level 1-C?
# You can filter manually the Cloud Cover threshold by changing the cc1 and cc2

aggregate_by_cloud(cc1 = 0, cc2 = 30).get('sentinel2L1C')['GB']

# In[14]:


# How much a total size (GB) filtered by cloud CC >= 0 and CC <= 30 in Sentinel 2 Level 2-A?

aggregate_by_cloud(cc1 = 0, cc2 = 30).get('sentinel2L2A')['GB']


# In[15]:


tile = gpd.read_file("tile_100km.shp")

# Converting object type to int64
tile['Id'] = pd.to_numeric(tile['Id'])

# Attribute Join
tile_name1 = aggregate().get('sentinel2L1C')
tile_name2 = aggregate().get('sentinel2L2A')

## Converting into int64
tile_name1['Id'] = pd.to_numeric(np.arange(len(tile_name1) + 1))
tile_name2['Id'] = pd.to_numeric(np.arange(len(tile_name2) + 1))

sentinel2_L1C = tile.merge(tile_name1, on='Id')
sentinel2_L2A = tile.merge(tile_name2, on='Id')

# Convert MB to GB
sentinel2_L1C['GB'] = sentinel2_L1C['size'] / 1000
sentinel2_L2A['GB'] = sentinel2_L2A['size'] / 1000

# Change into two decimal format
sentinel2_L1C['GB'] = pd.to_numeric(sentinel2_L1C['GB']).round(2)
sentinel2_L2A['GB'] = pd.to_numeric(sentinel2_L2A['GB']).round(2)


# In[16]:


m = f.Map(
    location=[-2.27, 118.27],
    zoom_start=5,
    tiles='mapboxbright'
)


# In[17]:


sentinel2_L1C_json = sentinel2_L1C.to_json()
sentinel2_L2A_json = sentinel2_L2A.to_json()

f.GeoJson(data=sentinel2_L1C_json,
                  name='Sentinel 2 Level 1-C',smooth_factor=2,
                  style_function=lambda x: {'color':'black','fillColor':'transparent','weight':2},
                  tooltip=f.GeoJsonTooltip(fields=['GB'],
                                              labels=False,
                                              sticky=False),
               highlight_function=lambda x: {'weight':3,'fillColor':'grey'}
              ).add_to(m)




# In[18]:


f.GeoJson(data=sentinel2_L2A_json,
                  name='Sentinel 2 Level 2-A',smooth_factor=2,
                  style_function=lambda x: {'color':'blue','fillColor':'transparent','weight':2},
                  tooltip= f.GeoJsonTooltip(fields=['GB'],
                                              labels=False,
                                              sticky=False),
                  highlight_function=lambda x: {'weight':3,'fillColor':'grey'}
              ).add_to(m)

f.LayerControl(autoZIndex=True).add_to(m)


# In[19]:


f.LayerControl().add_to(m)
m


# In[20]: Deprecated function

# Add the color for the chloropleth:
m.choropleth(
 geo_data=sentinel2_L1C_json,
 name='choropleth',
 data=aggregate().get('sentinel2L2A')['GB'],
 columns=['Id', 'GB'],
 key_on='feature.Id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Sentinel 2 Level 2-A Size (GB)'
)
f.LayerControl().add_to(m)


# In[21]:
m.choropleth(
 geo_data=sentinel2_L1C_json,
 name='choropleth',
 data=aggregate().get('sentinel2L2A')['GB'],
 columns=['Id', 'GB'],
 key_on='feature.Id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Sentinel 2 Level 2-A Size (GB)'
)

m
# In[22]:

from branca.colormap import linear

colormap_s2 = linear.YlGn_09.scale(
        aggregate().get('sentinel2L2A')['GB'].min(),
        aggregate().get('sentinel2L2A')['GB'].max())

colormap_s1 = linear.YlGn_09.scale(
        aggregate().get('sentinel2L1C')['GB'].min(),
        aggregate().get('sentinel2L1C')['GB'].max())

# In[23]:
agg_s2_dict = pd.DataFrame(aggregate().get('sentinel2L2A')).set_index('Id')['GB']
agg_s1_dict = pd.DataFrame(aggregate().get('sentinel2L1C')).set_index('Id')['GB']

# In[24]:

f.GeoJson(
    tile,
    name='Sentinel 2 Level 1-C (GB)',
    style_function=lambda feature: {
        'fillColor': colormap_s1(agg_s1_dict[feature['id']]),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.9,
    }
).add_to(m)

f.LayerControl().add_to(m)

m