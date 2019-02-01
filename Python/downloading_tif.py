import requests
from tqdm import tqdm
import math
import os

# set your working directory
path = 'C:/Users/GIS/Python Projects'
os.chdir(path)

# collecting some of your desired files to be downloaded in list
idn_grid = ['00N_140E.tif', '00N_130E.tif', '00N_120E.tif', '00N_110E.tif', '00N_100E.tif', '00N_090E.tif',
			'10S_120E.tif', '10S_110E.tif',
			'10N_130E.tif', '10N_120E.tif', '10N_110E.tif', '10N_100E.tif', '10N_090E.tif']


# Write data to files with looping

for i in range(len(idn_grid)):
	url = 'https://glad.umd.edu/Potapov/GFW_2017/drivers_2017/'
	r = requests.get(url + idn_grid[i], stream = True) # create http response object

	# checking total sizes in byte
	total_size = int(r.headers.get('content-length', 0))
	block_size = 1024
	wrote = 0

	with open(idn_grid[i], 'wb') as f:
		for data in tqdm(r.iter_content(block_size), total = math.ceil(total_size / block_size), unit = 'KB', unit_scale = True):
			wrote = wrote + len(data)
			f.write(data)

	if total_size != 0 and wrote != total_size:
		print("ERROR, something went wrong")

"""
References:
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    
"""