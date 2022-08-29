#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:32:31 2022

@author: timjim
"""

import os

path = 'images/test_images/'
print(os.listdir(path)) 

for image in os.listdir(path):  #iterate through each file to perform some action
    print(image)
    
    
import os
print(os.walk("."))  #Nothing to see here as this is just a generator object

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    #print(root)
    path = root.split(os.sep)  #SPlit at separator (/ or \)
    #print(path)  #Gives names of directories for easy location of files
    #print(files)   #Prints all file names in all directories
    
    
#Let us now visualize directories and files within them
    print((len(path) - 1) * '---', os.path.basename(root)) #Add --- based on the path
    for file in files:
        print(len(path) * '---', file)
        
        
#Another way to look at all dirs. and files...  
import os
for root, dirs, files in os.walk("."):
#for path,subdir,files in os.walk("."):
   for name in dirs:
       print (os.path.join(root, name)) # will print path of directories
   for name in files:    
       print (os.path.join(root, name))