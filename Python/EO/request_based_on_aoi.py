# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:49:46 2019

@author: Rizky Firmansyah
"""

import os
import requests
import json
import geopandas as gp
import datetime
import time

import rasterio
from rasterio import features as rfeatures
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

from IPython.display import display, Image
from functools import partial
from tqdm import tqdm
from planet import api
from planet.api import filters
import pyproj
from shapely import geometry as sgeom
import shapely.ops

path = "W:/GEORESEARCH/PTW Illegal Logging/Results/#5 Jan - Mar 2019"
os.chdir(path)

# API Key stored as an env variable
PLANET_API_KEY = '591b3f11a0a5446781a0982f51e18e3b'
#PLANET_API_KEY = os.getenv('PLANET_API_KEY')


# this notebook uses rasterio Shapes for processing, so lets convert that geojson to a shape
aoi_json = gp.read_file("loc_1.shp").to_json()
data = json.loads(aoi_json)
aoi = sgeom.shape(data['features'][0]['geometry'])

start_date = "2019-01-01T00:00:00.000Z"
end_date = "2019-03-31T00:00:00.000Z"
y1 = 2019
m1 = 1
d1 = 1

y2 = 2019
m2 = 1
d2 = 31

cc = 5

#geometry_filter = {
#    "type": "GeometryFilter",
#    "field_name": "geometry",
#    "config": aoi        
#}
#
#date_range_filter = {
#    "type": "DateRangeFilter",
#    "field_name": "acquired",
#    "config": {
#        "gte": start_date,
#        "lte": end_date
#    }        
#}
#    
## only get image which have <% cloud coverage    
#cloud_cover_filter = {
#    "type": "RangeFilter",
#    "field_name": "cloud_cover",
#    "config": {
#        "lte": cc
#    }        
#}
#
## combine our geo, date, cloud filters
#combined_filters = {
#    "type": "AndFilter",
#    "config": [geometry_filter, date_range_filter, cloud_cover_filter]
#}
#
## API request object
#search_request = {
#    "interval": "day",
#    "item_types": [item_type],
#    "filter": combined_filters
#}

def build_request(aoi_shape):
    old = datetime.datetime(year=y1,month=m1,day=d1)
    new = datetime.datetime(year=y2,month=m2,day=d2)
    
    query = filters.and_filter(
        filters.geom_filter(sgeom.mapping(aoi_shape)),      
        filters.range_filter('cloud_cover', lt=cc),
        filters.date_range('acquired', gt=old),
        filters.date_range('acquired', lt=new)
    )
    
    item_types = ["PSScene4Band"]
    return filters.build_search_request(query, item_types)
        
search_request = build_request(aoi)

# Quick searches are meant to be more fleeting, and are not guaranteed to be available on the API after they are executed.

# Utility functions: projecting a feature to the appropriate UTM zone

def get_utm_projection_fcn(shape):
    # define projection
    proj_fcn = partial(
        pyproj.transform,
        pyproj.Proj(init='epsg:4326'), #wgs84
        _get_utm_projection(shape))
    return proj_fcn

def _get_utm_zone(shape):
    centroid = shape.centroid
    lon = centroid.x
    lat = centroid.y
    
    if lat > 84 or lat < -80:
        raise Exception('UTM Zones only valid within [-80, 84] latitude')
        
    zone = int((lon + 180) / 6 + 1)
    
    hemisphere = 'north' if lat > 0 else 'south'
    
    return (zone, hemisphere)

def _get_utm_projection(shape):
    zone, hemisphere = _get_utm_zone(shape)
    proj_str = "+proj=utm +zone={zone}, +{hemi} +ellps=WGS84 +datum=WGS84 +units=m +no_defs".format(
            zone=zone, hemi=hemisphere)
    return pyproj.Proj(proj_str)

proj_fcn = get_utm_projection_fcn(aoi)
aoi_shape_utm = shapely.ops.transform(proj_fcn, aoi)


def get_coverage_dimensions(aoi_shape_utm):
    '''Checks that aoi is big enough and calculates the dimensions for coverage grid.'''
    minx, miny, maxx, maxy = aoi_shape_utm.bounds
    width = maxx - minx
    height = maxy - miny
    
    min_cell_size = 9 # in meters, approx 3x ground sampling distance
    min_number_of_cells = 3
    max_number_of_cells = 3000
    
    
    min_dim = min_cell_size * min_number_of_cells
    if height < min_dim:
        raise Exception('AOI height too small, should be {}m.'.format(min_dim))

    if width < min_dim:
        raise Exception('AOI width too small, should be {}m.'.format(min_dim))
    
    def _dim(length):
        return min(int(length / min_cell_size), max_number_of_cells)

    return [_dim(l) for l in (height, width)]


dimensions = get_coverage_dimensions(aoi_shape_utm)

# Search Planet API
def create_client():
    return api.ClientV1(api_key=PLANET_API_KEY)

def search_pl_api(request, limit=500):
    client = create_client()
    result = client.quick_search(request)
    
    return result.items_iter(limit=limit)

def get_overlap_shapes_utm(items, aoi_shape):
    
    proj_fcn = get_utm_projection_fcn(aoi_shape)
    aoi_shape_utm = shapely.ops.transform(proj_fcn, aoi_shape)
    
    def _calculate_overlap(item):
        footprint_shape = sgeom.shape(item['geometry'])
        footprint_shape_utm = shapely.ops.transform(proj_fcn, footprint_shape)
        return aoi_shape_utm.intersection(footprint_shape_utm)
    
    for i in items:
        yield _calculate_overlap(i)
        
items = search_pl_api(search_request)

# cache the overlaps as a list so we don't have to refetch items
overlaps = list(get_overlap_shapes_utm(items, aoi))
print(len(overlaps))

# What do overlaps look like?
display(overlaps[0])

def calculate_coverage(overlaps, dimensions, bounds):
    
    # get dimensions of coverage raster
    mminx, mminy, mmaxx, mmaxy = bounds

    y_count, x_count = dimensions
    
    # determine pixel width and height for transform
    width = (mmaxx - mminx) / x_count
    height = (mminy - mmaxy) / y_count # should be negative

    # Affine(a, b, c, d, e, f) where:
    # a = width of a pixel
    # b = row rotation (typically zero)
    # c = x-coordinate of the upper-left corner of the upper-left pixel
    # d = column rotation (typically zero)
    # e = height of a pixel (typically negative)
    # f = y-coordinate of the of the upper-left corner of the upper-left pixel
    # ref: http://www.perrygeo.com/python-affine-transforms.html
    transform = rasterio.Affine(width, 0, mminx, 0, height, mmaxy)
    
    coverage = np.zeros(dimensions, dtype=np.uint16)
    for overlap in overlaps:
        if not overlap.is_empty:
            # rasterize overlap vector, transforming to coverage raster
            # pixels inside overlap have a value of 1, others have a value of 0
            overlap_raster = rfeatures.rasterize(
                    [sgeom.mapping(overlap)],
                    fill=0,
                    default_value=1,
                    out_shape=dimensions,
                    transform=transform)
            
            # add overlap raster to coverage raster
            coverage += overlap_raster
    return coverage


# what is a low-resolution look at the coverage grid?
display(calculate_coverage(overlaps, (6,3), aoi_shape_utm.bounds))

def plot_coverage(coverage):
    fig, ax = plt.subplots()
    cax = ax.imshow(coverage, interpolation='nearest', cmap=cm.viridis)
    ax.set_title('Coverage\n(median: {})'.format(int(np.median(coverage))))
    ax.axis('off')
    
    ticks_min = coverage.min()
    ticks_max = coverage.max()
    cbar = fig.colorbar(cax,ticks=[ticks_min, ticks_max])


plot_coverage(calculate_coverage(overlaps, dimensions, aoi_shape_utm.bounds))
    

# Setup Planet Data API base URL
URL = "https://api.planet.com/data/v1"

## Setup the session
session = requests.Session()

## Authenticate
session.auth = (PLANET_API_KEY, "")

quick_url = "{}/quick-search".format(URL)

res = session.post(quick_url, json=search_request)
geojson = res.json()

#url = geojsonio.display(res.text)

features = geojson["features"]
for f in features:
    # Print the ID for each feature
    print(f["id"])
  
#next_url = geojson["_links"]["_next"]
#res = session.get(next_url)

features = geojson["features"]
# Get the first result's feature
feature = features[0]

# get the assets link for the item
assets_url = feature["_links"]["assets"]

asset_activated = False
while asset_activated == False:
    res = session.get(assets_url)
    assets = res.json()
    
    analytic = assets["analytic"]
    asset_status = analytic["status"]
    
    if asset_status == 'active':
        asset_activated = True
        print("Asset is active and ready to download")
        
    # Still activating. Wait and check again.
    else:
        print("...Still waiting for asset activation...")
        time.sleep(3)
        
location_url = analytic["location"]

# Create a function to download asset files
def pl_download(url, filename=None):
    # Send a GET request to the provided location url
    res = requests.get(url, stream=True, auth=(PLANET_API_KEY, ""))
    
    if not filename:
        # Construct a filename from the API response
        if "content-disposition" in res.headers:
            filename = res.headers["content-disposition"].split("filename=")[-1].strip("'\"")
        # Construct a filename from the location url
        else:
            filename = url.split("=")[1][:10]
    
    # Save the file
    with open(path + '/planet/' + filename, "wb") as f:
        for chunk in tqdm(res.iter_content(chunk_size=1024)):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        
    return filename

# Download the file from an activated asset's location url
#pl_download(location_url)