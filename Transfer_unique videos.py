# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:29:22 2020

@author: Sima
"""


# import all the data 

import os,shutil
dest = r'..\Unique Videos'

# read all the excel files containing the patients data,
# this is for now just for PKMAS but it can be extended
path = r'..\Original Videos'
#subdirectory = ['PKMAS']
filelist =[]

for root,dirs,files in os.walk(path):
    for dir in dirs:    
        source = os.path.join(root,dir)
        for file in os.listdir(source):
            if (file.endswith('.MPG') or (file.endswith('.vsmeta'))or file.endswith('.asf')or file.endswith('.WMV')):
                if not os.path.exists(dest+'\\'+file):
                    #os.mkdir(dest+'\\'+file)
                    shutil.copy(source+"\\"+file ,dest +'\\'+ file)





# Read the data from the excel file


# Rename the file's names based on the info on excel sheet

# import os
# os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')


# add a column with the new names of the files


