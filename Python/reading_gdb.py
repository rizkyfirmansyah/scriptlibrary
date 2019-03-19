import geopandas as gpd
import fiona
import os

path = "/cosmos/ftp/RBI_BIG_2016/"

# select your geodatabase file
file = "RBI50K_SUMATERA.gdb"
os.chdir(path)

# changes your filename here
fname = "RBI50K_SUMATERA.txt"

#create a list of layers with in a file geodatabase 
layerlist = fiona.listlayers(path+file)

f = open(fname, "w")
for i in sorted(layerlist):
    f.write(i + "\n")

f.close()