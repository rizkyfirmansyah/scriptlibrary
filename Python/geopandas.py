# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:58:14 2019

@author: Rizky Firmansyah
"""

import geopandas as gp
import os
import matplotlib.pyplot as plt

path = "D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Dataviz/Hotspot VIIRS"
os.chdir(path)

hotspot = gp.read_file("Karhutla_Riau_2013_12mar.shp")
riau = gp.read_file("D:/DATA/GEOSPATIAL/MINISTRY/BIG/Administrative/indonesia_provinsi_2013_edited.shp")
peat = gp.read_file("D:/DATA/GEOSPATIAL/GFW/Indonesia_peat_lands/idnprov_peat_lands.shp")

riau_f = riau[riau.province == 'Riau']
peat_f = peat[peat.province == 'Riau']

hotspots = []

def hotspotList(x, y):
    return hotspots.append(hotspot[(hotspot.ACQ_DATE < x) & (hotspot.ACQ_DATE >= y)])

# filtered your data here
#hotspotList('2013-04-01', '2013-01-01')
#hotspotList('2013-07-01', '2013-04-01')
#hotspotList('2013-10-01', '2013-07-01')
#hotspotList('2014-01-01', '2013-10-01')
#hotspotList('2014-04-01', '2014-01-01')
#hotspotList('2014-07-01', '2014-04-01')
#hotspotList('2014-10-01', '2014-07-01')
#hotspotList('2015-01-01', '2014-10-01')
hotspotList('2015-04-01', '2015-01-01')
hotspotList('2015-07-01', '2015-04-01')
hotspotList('2015-10-01', '2015-07-01')
hotspotList('2016-01-01', '2015-10-01')
hotspotList('2016-04-01', '2016-01-01')
hotspotList('2016-07-01', '2016-04-01')
hotspotList('2016-10-01', '2016-07-01')
hotspotList('2017-01-01', '2016-10-01')
hotspotList('2017-04-01', '2017-01-01')
hotspotList('2017-07-01', '2017-04-01')
hotspotList('2017-10-01', '2017-07-01')
hotspotList('2018-01-01', '2017-10-01')
hotspotList('2018-04-01', '2018-01-01')
hotspotList('2018-07-01', '2018-04-01')
hotspotList('2018-10-01', '2018-07-01')
hotspotList('2019-01-01', '2018-10-01')
hotspotList('2019-04-01', '2019-01-01')

hotspotLabel = [
#        'Januari - Maret 2013',
#        'April - Juni 2013',
#        'Juli - September 2013',
#        'Oktober - Desember 2013',
#        'Januari - Maret 2014',
#        'April - Juni 2014',
#        'Juli - September 2014',
#        'Oktober - Desember 2014',
		'Januari - Maret 2015',
        'April - Juni 2015',
        'Juli - September 2015',
        'Oktober - Desember 2015',
		'Januari - Maret 2016',
        'April - Juni 2016',
        'Juli - September 2016',
        'Oktober - Desember 2016',
        'Januari - Maret 2017',
        'April - Juni 2017',
        'Juli - September 2017',
        'Oktober - Desember 2017',
		'Januari - Maret 2018',
        'April - Juni 2018',
        'Juli - September 2018',
        'Oktober - Desember 2018',
        'Januari - Maret 2019'
        ]

graphTitle = 'Titik Panas Riau periode 2015 - 12 Maret 2019'

        
# save the figures

#for idx, val in enumerate(hotspots):
#    fig = plt.figure(figsize=(10, 10))
#    ax = fig.add_subplot(111)
#    
#    rf = riau_f.plot(ax=ax, color='white', edgecolor='k')
#    peat_f.plot(ax=ax, color='black')
#    hotspots[idx].plot(ax=ax, color='#f16521', edgecolor='#ff4f1e')
#                
#    #    white peat
##    rf = riau_f.plot(ax=ax, color='#3a3d42', edgecolor='k')
##    peat_f.plot(ax=ax, color='#ffffff')
##    hotspots[0].plot(ax=ax, color='#f16521', edgecolor='#ff4f1e')
#    
#    rf.set_axis_off()
#    
#    ax.annotate(hotspotLabel[idx], xy=(0.16, .21),
#        xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=14, color='#161616', fontname='Whitney')
#    plt.title(graphTitle, fontname='Whitney', fontsize=16, loc='center', pad=-10)
#
#    plt.savefig('frame'+str(idx)+'.png', dpi=600, bbox_inches='tight')
#    fig.tight_layout()
#    
#    fig.clf()
#    plt.close()

im = 'D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Dataviz/Hotspot VIIRS/pg_logo.png'
img = plt.imread(im)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

rf = riau_f.plot(ax=ax, color='white', edgecolor='k')
peat_f.plot(ax=ax, color='black')
hotspots[0].plot(ax=ax, color='#f16521', edgecolor='#ff4f1e')
            
rf.set_axis_off()

ax.annotate(hotspotLabel[0], xy=(0.16, .21),
    xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=14, color='#161616', fontname='Whitney')
plt.title(graphTitle, fontname='Whitney', fontsize=16, loc='center', pad=-10)

ax.imshow()
plt.savefig('tes.png', dpi=600, bbox_inches='tight')
fig.tight_layout()

#fig.clf()
#plt.close()