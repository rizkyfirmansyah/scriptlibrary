import requests
from requests import ConnectionError
from tqdm import tqdm
import math
import os
import time

# set your working directory
path = 'E:/DEM'
os.chdir(path)

# specify your file path containing list of filename to be downloaded
file = 'list_papua.txt'

connection_timeout = 30 # in seconds
# read every line within file
with open(file) as f:
    content = f.readlines()
# removing newline characters in end of every lines
content = [x.strip() for x in content]

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
start_time = time.time()

i = 0
while i < len(content):
    try:
        # Write data to files with looping
        url = 'http://tides.big.go.id/DEMNAS/download.php?download_file=DEMNAS_'
        r = requests.get(url + content[i] + '_v1.0.tif', stream = True, headers= headers) # create http response object
            
        # checking total sizes in byte
        total_size = int(r.headers.get('content-length', 0))
        # limit the total size of downloading by setting the parameters block size. The less number the more packet you get
        block_size = 64
        wrote = 0
        url_file = url + content[i] + '_v1.0.tif'
        
        if r.status_code != 404 and not os.path.exists(os.path.join(path, content[i])):
            with open(content[i], 'wb') as f:
                for data in tqdm(r.iter_content(block_size), total = math.ceil(total_size / block_size), unit = 'KB', unit_scale = True):
                    wrote = wrote + len(data)
                    f.write(data)
                    
            if total_size != 0 and wrote != total_size:
                time.sleep(30)
                print(r.headers)
                    
            i += 1
            continue
        else:
            if r.status_code == 404:
                print("Your file requests were not found. Please check your url.")
                i += 1
                continue
            else:
                print("Please check again your server requests.")
                break
    except ConnectionError:
        if time.time() > start_time + connection_timeout:
            raise Exception('Unable to get request after {} seconds of ConnectionErrors'.format(connection_timeout))
        else:
            time.sleep(30) # attempting once every 30 seconds
    else:
        break