# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:56:50 2019

@author: Rizky Firmansyah
"""


import os
from os import listdir
from os.path import isfile, join
import pandas as pd

path = 'D:/Universe/GEOSPATIAL DATA/OPEN DATA/Sentinel/L1C'
os.chdir(path)

all_files = []
sentinel2l1_data = pd.DataFrame()
tileID = list()
dataframes = pd.DataFrame()
yearID = list()

def read_csv():
    global all_files
    """ read all files over csv files """
    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    
def populate_tile():
    global tileID
    global dataframes
    global yearID
    # read tile ID from filename
    tile = [i[41:-4] for i in all_files]
    year = [i[19:23] for i in all_files]
    
    # combined all files into one
    dataframes = [pd.read_csv(f, header=0) for f in all_files]
    length_df = [i.shape[0] for i in dataframes]
    
    tileID = list(zip(length_df, tile))
    yearID = list(zip(length_df, year))
    

def populate_data():
    global sentinel2l1_data
    sentinel2l1_data = pd.concat(dataframes)
    
    data = []
    year_data = []

    for i, v in enumerate(tileID):
        n = 0
        while n < v[0]:
            data.append(v[1])
            n += 1
    
    for i, v in enumerate(yearID):
        m = 0
        while m < v[0]:
            year_data.append(v[1])
            m += 1
            
    sentinel2l1_data['tile']  = data
    sentinel2l1_data['year']  = year_data

read_csv()
populate_tile()
populate_data()

sentinel2l1_data.to_csv('Sentinel2_Level-1C_2015_2019.csv')