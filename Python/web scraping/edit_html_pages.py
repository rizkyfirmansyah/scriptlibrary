# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:18:06 2019

@author: Rizky Firmansyah
"""

# Adding HTML pages for datasets of simple random sampling based of Landsat

## Libraries Used
from os import listdir
from os.path import isfile, join
import re
from tqdm import tqdm

regions_name = ['Irian_Jaya_sample',
                'Jawa_sample',
                'Kalimantan_sample',
                'Maluku_sample',
                'Nusa_Tenggara_sample',
                'Sulawesi_sample',
                'Sumatera_sample'
                ]

idx_regions_name = ['index_Irian_Jaya',
                'index_Jawa',
                'index_Kalimantan',
                'index_Maluku',
                'index_Nusa_Tenggara',
                'index_Sulawesi',
                'index_Sumatera'
                ]

first_page = ['Irian_Jaya_sample1.html',
              'Jawa_sample2173.html',
              'Kalimantan_sample2875.html',
              'Maluku_sample5703.html',
              'Nusa_Tenggara_sample6116.html',
              'Sulawesi_sample6497.html',
              'Sumatera_sample7484.html'
        ]

last_page = ['Irian_Jaya2172.html',
             'Jawa_sample2874.html',
             'Kalimantan_sample5702.html',
             'Maluku_sample6115.html',
             'Nusa_Tenggara_sample6496.html',
             'Sulawesi_sample7483.html',
             'Sumatera_sample10000.html'
        ]

# Irian_Jaya_sample1.html Irian_Jaya2172.html
# Jawa_sample2173.html Jawa_sample2874.html
# Kalimantan_sample2875.html Kalimantan_sample5702.html
# Maluku_sample5703.html Maluku_sample6115.html
# Nusa_Tenggara_sample6116.html Nusa_Tenggara_sample6496.html
# Sulawesi_sample6497.html Sulawesi_sample7483.html
# Sumatera_sample7484.html Sumatera_sample10000.html


workingpath = "D:/Unlocks/WRI/Forest/NFMS/Research/UMD - Random Sampling/Indonesia_samples/pages_new/"
#htmlFile = "D:/Unlocks/WRI/Forest/NFMS/Research/UMD - Random Sampling/Indonesia_samples/pages_new/Irian_Jaya_sample10.html"

# list all files within directory
onlyfiles = [f for f in listdir(workingpath) if isfile(join(workingpath, f))]

# iterating on each file and manipulating its content
for htmlFile in tqdm(onlyfiles):
    # get the sampling number from its filename
    n = re.findall("\d+", htmlFile)[0]
    
#   manipulating html contents here
    with open(workingpath + htmlFile, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if i in range(14, 16):
                continue
            if i == 16:
                if re.match(regions_name[0]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[0]):
                        f.write('\t\t<a class="header-link" href='+regions_name[0] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[0] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Irian Jaya Sample ' + n +'</b></a></a>')
                    f.write('\n')                    
                elif re.match(regions_name[1]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[1]):
                        f.write('\t\t<a class="header-link" href='+regions_name[1] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[1] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Jawa Sample ' + n +'</b></a></a>')
                    f.write('\n')
                elif re.match(regions_name[2]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[2]):
                        f.write('\t\t<a class="header-link" href='+regions_name[2] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[2] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Kalimantan Sample ' + n +'</b></a></a>')
                    f.write('\n')
                elif re.match(regions_name[3]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[3]):
                        f.write('\t\t<a class="header-link" href='+regions_name[3] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[3] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Maluku Sample ' + n +'</b></a></a>')
                    f.write('\n')
                elif re.match(regions_name[4]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[4]):
                        f.write('\t\t<a class="header-link" href='+regions_name[4] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[4] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Nusa Tenggara Sample ' + n +'</b></a></a>')
                    f.write('\n')
                elif re.match(regions_name[5]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[5]):
                        f.write('\t\t<a class="header-link" href='+regions_name[5] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href=../'+ idx_regions_name[5] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Sulawesi Sample ' + n +'</b></a></a>')
                    f.write('\n')
                elif re.match(regions_name[6]+'[0-9]+', htmlFile):
                    if (htmlFile != first_page[6]):
                        f.write('\t\t<a class="header-link" href='+regions_name[6] + str(int(n) - 1) +'.html>Sample <b>'+ str(int(n) - 1) +' >></b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[6] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    f.write('\t\t<a class="active"><b>Sumatera Sample ' + n +'</b></a></a>')    
                    f.write('\n')
            if i in range(18, 20):
                continue
            if i == 20:
                if re.match(regions_name[0]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[0]):
                        f.write('\t\t<a class="header-link" href='+regions_name[0] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[0] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[0] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[1]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[1]):
                        f.write('\t\t<a class="header-link" href='+regions_name[1] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[1] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[1] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[2]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[2]):
                        f.write('\t\t<a class="header-link" href='+regions_name[2] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[2] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[2] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[3]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[3]):
                        f.write('\t\t<a class="header-link" href='+regions_name[3] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[3] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[3] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[4]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[4]):
                        f.write('\t\t<a class="header-link" href='+regions_name[4] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[4] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[4] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[5]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[5]):
                        f.write('\t\t<a class="header-link" href='+regions_name[5] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[5] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[5] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                elif re.match(regions_name[6]+'[0-9]+', htmlFile):
                    if (htmlFile != last_page[6]):
                        f.write('\t\t<a class="header-link" href='+regions_name[6] + str(int(n) + 1) +'.html>Sample <b>'+ str(int(n) + 1) +' >></b></a>')
                        f.write('\n')
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[6] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                    else:
                        f.write('\t\t<a class="header-link" href="../'+ idx_regions_name[6] +'.html"><b>Return to Index</b></a>')
                        f.write('\n')
                        f.write('\t</nav>')
                    
            f.write(line)
            
        f.truncate()
        f.close()