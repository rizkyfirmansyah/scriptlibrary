# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:50:29 2018

@author: GIS
"""
"""
import os

path = "W:/DEM/Warp"

files = os.listdir(path)

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, "DEMNAS_" + file))
    
"""

# list all files with a given string
import os

path = "W:/DEM"

files = []

for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)) and 'DEMNAS_' in i:
        files.append(i)