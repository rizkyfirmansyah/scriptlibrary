# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:33:32 2019

@author: Rizky Firmansyah
"""

import os
import geopandas as gp
import rasterio
import numpy
import matplotlib.pyplot as plt
from matplotlib import colors

path = "W:/GEORESEARCH/PTW Illegal Logging/Results/#5 Jan - Mar 2019/planet"
os.chdir(path)

# API Key stored as an env variable
PLANET_API_KEY = '591b3f11a0a5446781a0982f51e18e3b'

filename = '20190330_032153_102e_3B_AnalyticMS.tif'

with rasterio.open(filename) as src:
    band_red = src.read(3)
with rasterio.open(filename) as src:
    band_nir = src.read(4)
    
# Calculating NDVI
    
numpy.seterr(divide='ignore', invalid='ignore')

# NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

print(numpy.nanmin(ndvi))
print(numpy.nanmax(ndvi))

# Save the results to a new single band image
meta = src.meta
print(meta)

# get the dtype of our NDVI array
ndvi_dtype = ndvi.dtype
print(ndvi_dtype)

kwargs = meta

kwargs.update(dtype=ndvi_dtype)

# update the count value since our output will no longer be a 4-band image
kwargs.update(count=1)

with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
    dst.write(ndvi, 1)
    
# NDVI value will range from -1 to 1; Use diverging color scheme to center the colorbar at a defined midpoint
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)
        
    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return numpy.ma.masked_array(numpy.interp(value, x, y), numpy.isnan(value))
    
# Set min/max values from NDVI range for image
min = numpy.nanmin(ndvi)
max = numpy.nanmax(ndvi)

# Set our custom midpoint for most effective NDVI analysis
mid = 0.1

colormap = plt.cm.RdYlGn
norm = MidpointNormalize(vmin=min, vmax=max, midpoint=mid)
fig = plt.figure(figsize=(20,10))

ax = fig.add_subplot(111)

cbar_plot = ax.imshow(ndvi, cmap=colormap, vmin=min, vmax=max, norm=norm)

ax.axis('off')
ax.set_title('Normalized Difference Vegetation Index', fontsize=17, fontweight='bold')

cbar = fig.colorbar(cbar_plot, orientation='horizontal', shrink=0.65)

#fig.savefig("ndvi-image.png", dpi=200, bbox_inches='tight', pad_inches=0.7)

plt.show()


# Generating a histogram of NDVI values

# Define a new figure
fig2 = plt.figure(figsize=(20,10))

ax = fig2.add_subplot(111)

plt.title("NDVI histogram", fontsize=18, fontweight='bold')
plt.xlabel("NDVI values", fontsize=14)
plt.ylabel("Number of pixels", fontsize=14)

# For the x-axis, count every pixel that is not an empty value
x = ndvi[~numpy.isnan(ndvi)]
color = 'b'

# call 'hist' with our x-axis, bins, and color details
ax.hist(x, bins=30, color=color, histtype='bar', ec='black')
#fig2.savefig("ndvi-histogram.png", dpi=200, bbox_inches='tight', pad_inches=0.5)

plt.show()