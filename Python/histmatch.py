import os
import subprocess

os.chdir('/var/www/html/samplingbased')
dir = next(os.walk('images_LPN/'))[1]

n = 0
while n < len(dir):
    subprocess.call("./histmatch -c rgb images_LPN/"+str(n+1)+"/SPOT67.jpg images_LPN/"+str(n+1)+"/SPOT67_2017.jpg images_LPN/"+str(n+1)+"/SPOT67_2017.jpg", shell=True)
    subprocess.call("./histmatch -c rgb images_LPN/"+str(n+1)+"/SPOT67.jpg images_LPN/"+str(n+1)+"/SPOT67_2018.jpg images_LPN/"+str(n+1)+"/SPOT67_2018.jpg", shell=True)
	
    n += 1
