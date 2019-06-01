#!/usr/bin/env python
# coding: utf-8

# ## Created on Wed May 22 16:48:01 2019
# ### @author: Rizky Firmansyah
# 

# In[1]:


import geopandas as gpd
import os
import pandas as pd
import numpy as np
import folium as f
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


s1 = pd.read_csv('Sentinel2_Level-1C_2015_2019.csv', skipinitialspace=True)
s2 = pd.read_csv('Sentinel2_Level-2A_2018_2019.csv', skipinitialspace=True)


# ### Data Cleaning
# Create a row index

# In[4]:


s1['rowid'] = np.arange(len(s1))
s2['rowid'] = np.arange(len(s2))


# In[5]:


s1.columns = ['filename', 'begin_position', 'cloud_cover', 'size', 'orbit', 'Id', 'year', 'rowid']
s2.columns = ['filename', 'begin_position', 'cloud_cover', 'size', 'orbit', 'Id', 'year', 'rowid']


# In[6]:


s1['size'] = pd.to_numeric(s1['size'].apply(lambda x: x[:-3]))
s2['size'] = pd.to_numeric(s2['size'].apply(lambda x: x[:-3]))


s1['gb'] = s1['size'].divide(other=1000)
s2['gb'] = s2['size'].divide(other=1000)


# #### Finding the duplicate

# In[7]:


duplicateS1 = s1[s1.duplicated(['filename', 'year'])]
duplicateS2 = s2[s2.duplicated(['filename', 'year'])]


# #### How many scenes over Indonesia

# In[8]:


s1_clean = s1[~s1['rowid'].isin(duplicateS1['rowid'])]
s2_clean = s2[~s2['rowid'].isin(duplicateS1['rowid'])]


# In[9]:


def aggregate(data, g = 'year', c = 'gb', v = 'sum'):
    """ Aggregation group by and returning the sum/max/min function in dictionary
        You can modify the g = year
        c = cloud_cover
        v = min/sum/max
    """
    s = data.groupby(g)[c].agg(v)
    return s


# #### Aggregate by Cloud Filter Function

# In[10]:


def aggregate_by_cloud(data, cc1 = 0, cc2 = 100, g = 'year', c = 'gb', v = 'sum'):
    """ Aggregation group by filtering the cloud cover threshold first then returning the sum/max/min function in dictionary
        By default: Minimum Cloud Cover (cc1) = 0 and Maximum Cloud Cover (cc2) = 100
        You can modify the g = Id
        c = cloud_cover
        v = min/sum/max
    """
    s = data[(data['cloud_cover'] >= cc1) & (data['cloud_cover'] <= cc2)].groupby(g)[c].agg(v)    
    return s


# In[11]:


tile = gpd.read_file("tile_100km.shp")

# Converting object type to int64
tile['Id'] = pd.to_numeric(tile['Id'])

# Attribute Join
tile_name1 = aggregate(s1_clean, g='Id')
tile_name2 = aggregate(s2_clean, g='Id')

## Converting into int64
tile_name1['Id'] = pd.to_numeric(np.arange(len(tile_name1) + 1))
tile_name2['Id'] = pd.to_numeric(np.arange(len(tile_name2) + 1))

sentinel2_L1C = tile.merge(tile_name1, on='Id')
sentinel2_L2A = tile.merge(tile_name2, on='Id')


# # Sentinel 2 Level 1-C Metadata

# In[12]:


def func(x, pos):  # formatter function takes tick label and tick position
   s = '{:0,d}'.format(int(x))
   return s

def aggregate_plot(df, title, xpos=0.25, ypos=1000, g='year', c='filename', v='count'):
    y_format = tkr.FuncFormatter(func)  # make formatter

    fig, ax = plt.subplots(figsize=(8,6))

    # data = df.groupby('year')[c].agg(ag)
    data = df
    data.plot(kind='bar', x='year', y='filename', legend=False, ax=ax)
    ax.set_xlabel('Year', fontsize=15, fontweight='black', color='#333F4B')
    ax.set_ylabel('')
    ax.yaxis.set_major_formatter(y_format)  # set formatter to needed axis

    # Change font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'

    # add an horizontal label for the y axis
    fig.text(-0.23, 0.96, title, fontsize=15, fontweight='black', color="#333F4B")

    # set axis
    ax.tick_params(axis='both', which='major', labelsize=12)

    # change the axis spines's style
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    # set the spines position
    ax.spines['bottom'].set_position(('axes', -0.04))
    ax.spines['left'].set_position(('axes', 0.015))

    # add a datalabel for each bar
    for i, v in enumerate(data):
        if (data.dtypes == 'int64'):
            plt.text(x=i-xpos, y=v+ypos, s='{:0,d}'.format(v) , fontdict=dict(fontsize=14))
        else:
            plt.text(x=i-xpos, y=v+ypos, s='{0:,.0f}'.format(v) , fontdict=dict(fontsize=14))


# In[13]:


aggregate_plot(aggregate(s1_clean, c='filename', v='count'), 'A total file of Sentinel 2 Level 1-C per Year')


# ## How much the total size (GB) of Sentinel 2 Level 1-C per year from 2015-06 to 2019-05-18?

# In[14]:


aggregate_plot(aggregate(s1_clean, v='sum'), 'A total size (GB) of Sentinel 2 Level 1-C per Year', 0.25)


# #### How much the total size (GB) of Sentinel 2 Level 1-C on each Tile ID

# In[15]:


from branca.colormap import linear

s2c_colormap = linear.YlOrRd_09.scale(
    sentinel2_L1C.gb.min(),
    sentinel2_L1C.gb.max())

s2c_colormap


# In[16]:


m = f.Map(
    location=[-2.27, 118.27],
    zoom_start=5,
    tiles='mapboxbright'
)
sentinel2_L1C_json = sentinel2_L1C.to_json()

f.GeoJson(sentinel2_L1C_json,
                  name='Sentinel 2 Level 1-C',
                  smooth_factor=2,
                  style_function=lambda x: {'color':'black','fillColor':s2c_colormap(x['properties']['gb']),'weight':2},
                  tooltip=f.GeoJsonTooltip(fields=['gb', 'Id'],
                                             aliases=['Size (GB)', 'Tile ID'],
                                             labels=True,
                                             sticky=True,
                                             localize=True),
               highlight_function=lambda x: {'weight':3,'fillColor':'grey'}
              ).add_to(m)

s2c_colormap.caption = 'Total Size in GB'
s2c_colormap.add_to(m)
f.LayerControl(autoZIndex=False).add_to(m)
m


# #### How much the total size (GB) of Sentinel 2 Level 1-C in a total from 2015-06 to 2019-05-18?

# In[17]:


aggregate(s1_clean).sum()


# #### How much a total size (GB) filtered by cloud CC >= 0 and CC <= 30 in Sentinel 2 Level 1-C?
# #### You can filter manually the Cloud Cover threshold by changing the cc1 and cc2

# In[18]:


aggregate_plot(aggregate_by_cloud(s1_clean, cc1 = 0, cc2 = 30), 'A total size (GB) of Sentinel 2 Level 1-C filtered by Cloud (CC >=0 and CC <= 30) per Year', 0.25, 200)


# # Sentinel 2 Level 2-A Metadata

# In[19]:


aggregate_plot(aggregate(s2_clean, v='count'), 'A total file of Sentinel 2 Level 2-A per Year', 0.1)


# In[20]:


aggregate_plot(aggregate(s2_clean, v='sum'), 'A total size (GB) of Sentinel 2 Level 2-A per Year', 0.1)


# #### How much the total size (GB) of Sentinel 2 Level 2-A on each Tile ID

# In[21]:


from branca.colormap import linear

s2a_colormap = linear.YlGnBu_09.scale(
    sentinel2_L2A.gb.min(),
    sentinel2_L2A.gb.max())

s2a_colormap


# In[22]:


n = f.Map(
    location=[-2.27, 118.27],
    zoom_start=5,
    tiles='mapboxbright'
)
sentinel2_L2A_json = sentinel2_L2A.to_json()
f.GeoJson(sentinel2_L2A_json,
          name='Sentinel 2 Level 2-A',
          smooth_factor=2,
          style_function=lambda x: {'color':'black','fillColor':s2a_colormap(x['properties']['gb']),'weight':2},
          tooltip=f.GeoJsonTooltip(fields=['gb', 'Id'],
                                     aliases=['Size (GB)', 'Tile ID'],
                                     labels=True,
                                     sticky=True,
                                     localize=True),
           highlight_function=lambda x: {'weight':3,'fillColor':'blue'}
              ).add_to(n)

s2a_colormap.caption = 'Total Size in GB'
s2a_colormap.add_to(n)
f.LayerControl(autoZIndex=False).add_to(n)
n


# ## How much the total size (GB) of Sentinel 2 Level 2-A in a total from 2018-11 to 2019-05-18?

# In[23]:


aggregate(s2_clean).sum()


# ### How much a total size (GB) filtered by cloud CC >= 0 and CC <= 30 in Sentinel 2 Level 2-A per Year?

# In[24]:


aggregate_plot(aggregate_by_cloud(s2_clean, cc1 = 0, cc2 = 30), 'A total size (GB) of Sentinel 2 Level 2-A filtered by Cloud (CC >=0 and CC <= 30) per Year', 0.12, 200)


# In[26]:


s2a_cc = aggregate_by_cloud(s2_clean, cc1 = 0, cc2 = 30, g='Id').to_frame()
s2a_cc.reset_index(inplace=True)

sentinel2_L2A_cc = pd.merge(tile, s2a_cc, on='Id')

sentinel2_L2A_cc.head(5)


# In[27]:


from branca.colormap import linear

s2acc_colormap = linear.YlGnBu_09.scale(
    sentinel2_L2A_cc.gb.min(),
    sentinel2_L2A_cc.gb.max())

s2acc_colormap


# In[29]:


o = f.Map(
    location=[-2.27, 118.27],
    zoom_start=5,
    tiles='mapboxbright'
)
sentinel2_L2A_cc_json = sentinel2_L2A_cc.to_json()
f.GeoJson(sentinel2_L2A_cc_json,
          name='Sentinel 2 Level 2-A (CC Filtered)',
          smooth_factor=2,
          style_function=lambda x: {'color':'black','fillColor':s2acc_colormap(x['properties']['gb']),'weight':2},
          tooltip=f.GeoJsonTooltip(fields=['gb', 'Id'],
                                     aliases=['Size (GB)', 'Tile ID'],
                                     labels=True,
                                     sticky=True,
                                     localize=True),
           highlight_function=lambda x: {'weight':3,'fillColor':'blue'}
              ).add_to(o)

s2acc_colormap.caption = 'Total Size in GB'
s2acc_colormap.add_to(o)
f.LayerControl(autoZIndex=False).add_to(o)
o


# In[ ]:


""" 
References:
https://scentellegher.github.io/visualization/2018/10/10/beautiful-bar-plots-matplotlib.html
https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
https://python-visualization.github.io/folium/quickstart.html

Folium Geojson with a colormap style
https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb?flush_cache=true
"""

