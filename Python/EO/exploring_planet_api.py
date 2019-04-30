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
import geojsonio
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
print(search_request)
# Quick searches are meant to be more fleeting, and are not guaranteed to be available on the API after they are executed.

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


# Calculate Coverage
def get_overlap_shapes_utm(items, aoi_shape):
#    Determine overlap between item footprint and AOI in UTM
    proj_fcn = get_
    
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