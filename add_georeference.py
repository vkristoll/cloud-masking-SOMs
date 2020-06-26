#Adding georeference to the cloud masks produced in the file "create_cloudmasks.py"
    
import os
import pandas as pd
from osgeo import gdal
from os.path import splitext
import numpy as np
import time

directory1 = os.listdir('path to the folder with the cloud masks') 
directory2 = os.listdir('path to the folder with Sentinel-2 bands') 

directory1a=sorted(directory1)
directory2a=sorted(directory2)

directory1b='path to the folder with the cloud masks'
directory2b='path to the folder with Sentinel-2 bands'

number_files="total number of files"

start_time = time.time()
for i in range (number_files): 

    print(" The repetition number is %s" %i)  
    print("--- %s seconds ---" % (time.time() - start_time)) 
    
    #Read the first cloud mask file
    os.chdir(directory1b)     
    ds1=gdal.Open(directory1a[i])    
    file_name1 = os.path.basename(directory1a[i])
    new_filename1 = file_name1.split('.')[0] 
    
    #Store the cloud mask in an array
    array = np.array(ds1.ReadAsArray())
    sizerows=len(array)
    sizecol=len(array[0])
    
    #Read the first Sentinel-2 image
    os.chdir(directory2b)
    ds2=gdal.Open(directory2a[i])
    
    #Import georeference information from the Sentinel-2 image                
    geotransform= ds2.GetGeoTransform()
    projection=ds2.GetProjection()     
    
    #Create a layer to store the georeferenced cloud mask 
    target_layer1= new_filename1 + "georeferenced.tif"   

    xSize=sizecol
    ySize=sizerows

    driver= gdal.GetDriverByName('GTiff')
    target_ds1 = driver.Create(target_layer1, xSize, ySize, bands=1, eType=gdal.GDT_Byte)    
    target_ds1.SetGeoTransform(geotransform)
    target_ds1.SetProjection(projection)  
    
    #Write the cloud mask to the layer
    outBand1 = target_ds1.GetRasterBand(1)
    outBand1.WriteArray(array)   
    
    #Close raster file
    target_ds1= None  
   
          
          
