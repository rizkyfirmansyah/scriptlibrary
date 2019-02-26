# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:18:06 2019

@author: Rizky Firmansyah
"""

# Adding HTML pages for datasets of simple random sampling based of Landsat

## Libraries Used
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import re

#year = [1985,
#        1986,
#        1987,
#        1988,
#        1989,
#        1990,
#        1991,
#        1992,
#        1993,
#        1994,
#        1995,
#        1996,
#        1997,
#        1998,
#        1999,
#        2000,
#        2001,
#        2002,
#        2003,
#        2004,
#        2005,
#        2006,
#        2007,
#        2008,
#        2009,
#        2010,
#        2011,
#        2012,
#        2013,
#        2014,
#        2015,
#        2016,
#        2017,
#        2018,
#        2019,
#        2020,
#        2021,
#        2022,
#        2023,
#        2024
#        ]

workingpath = "D:/DEVELOPER SPOTS/Indonesia_samples/pages_new/"

# list all files within directory
onlyfiles = [f for f in listdir(workingpath) if isfile(join(workingpath, f))]

## iterating on each file and manipulating its content
for htmlFile in onlyfiles:
    # get the sampling number from its filename
    n = re.findall("\d+", htmlFile)[0]

    with open(workingpath + htmlFile) as fh:
        
        soup = BeautifulSoup(fh, "lxml")
        
        ## adding css custom tag
        css_tag = soup.new_tag("link", rel="stylesheet", href="../custom.css")
        soup.style.insert_after(css_tag)
        
        ## Modifying table Tags
        tableTag = soup.find_all('table')
        for t in tableTag:
            t['class'] = "images"
            
    #    Modifying the image Tags
        imgTag = soup.find_all('img')
        for idx, val in enumerate(imgTag):
            del val['width']
            del val['height']
            val['class'] = "landsat"
            
    #    Modifying Header Links
        aTag = soup.find_all('a')
        for a in aTag:
            a['class'] = "header-link"
            
    #    append KLHK lulc classifcication
        lulcTag = BeautifulSoup('\n'
                                '<a href="../LULC_KLHK/'+n+'/lulc_klhk_2014.txt">Klasifikasi KLHK</a>', "html.parser")
        soup.select('a')[1].insert_after(lulcTag)
        
    # write the results to existing/new file
    with open(workingpath + htmlFile, "w") as file:
        file.write(str(soup))
    
    # deleting specific line
    with open(workingpath + htmlFile, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if i == 55:
                continue
            ## adding more images in this line
            if i == 56:
                f.write('</tr>')
                f.write('\n')
                f.write('<tr>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2017.jpg"/>2017 Pixel Based</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2017_tile.jpg"/>2017 Tile Based</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2017.jpg"/>2018 Pixel Based</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2018_tile.jpg"/>2018 Tile Based</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2019.jpg"/>2019</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2020.jpg"/>2020</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2021.jpg"/>2021</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img class="landsat" src="../images_LPN/'+n+'/2022.jpg"/>2022</p></td>')
                f.write('\n')
                f.write('</tr>')
                f.write('\n')
            if i in range(58, 61):
                continue
            if i == 61:
                f.write('<tr>')
                f.write('\n')
                f.write('<td><p class="bodytext"><a href="../images_LPN/'+n+'/SPOT67.jpg"><img src="../images_LPN/'+n+'/SPOT67.jpg" class="spot"></a></br>SPOT67_2013-2016</p></td>')
                f.write('\n')
                f.write('<td><p class="bodytext"><a href="../images_LPN/'+n+'/SPOT67_2018.jpg"><img src="../images_LPN/'+n+'/SPOT67_2018.jpg" class="spot"></a></br>SPOT67_2013-2018</p></td>')
                f.write('\n')
                f.write('</tr>')
                f.write('\n')
                f.write('</table>')
                f.write('\n')
                f.write('<table class="images">')
                f.write('\n')
                f.write('<tr>')
                f.write('\n')
                f.write('<td><p class="bodytext"><img src="../profiles/'+n+'_plot.png" class="plot"></p></td>')
                f.write('\n')
            if i in range(62, 67):
                continue
            f.write(line)
            
        f.truncate()
        f.close()