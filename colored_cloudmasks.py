#Producing cloud masks with different colours for TP,TN,FN,FP

#Importing libraries
import os
import numpy as np
import tifffile as tiff
from os.path import splitext
from sklearn.metrics import confusion_matrix
import time

directory1= os.listdir('path to the folder with the ground truth cloud masks')
directory2= os.listdir('path to the folder with the cloud masks produced by the SOM')

directory1a= 'path to the folder with the ground truth cloud masks'
directory2a= 'path to the folder with the cloud masks produced by the SOM'

directory1b=sorted(directory1)
directory2b=sorted(directory2)

start_time = time.time()

number_files="total number of files"
for i in range(number_files): 
  
    print(" The repetition number is %s" %i)  
    print("--- %s seconds ---" % (time.time() - start_time))  
    
    #Read the first ground truth cloud mask
    os.chdir(directory1a)
    gt_mask= tiff.imread(directory1b[i])
    size=1830*1830    

    #Read first SOM cloud mask
    os.chdir(directory2a)
    SOM_mask=tiff.imread(directory2b[i])     
    file_name = os.path.basename(directory2b[i])
    
    #Creating four arrays with zeros to store True Positive (TP), False Positive (FP), False Negative (FN) and True Negative (TN) pixels
    TP=np.zeros((1830,1830))
    TN=np.zeros((1830,1830))
    FN=np.zeros((1830,1830))
    FP=np.zeros((1830,1830))    
       
    for i in range (1830):
        for j in range (1830):
            if gt_mask[i,j]==255 and SOM_mask[i,j]==255:
                TP[i,j]=1
            elif gt_mask[i,j]==0 and SOM_mask[i,j]==0:
                TN[i,j]=2
            elif gt_mask[i,j]==255 and SOM_mask[i,j]==0:
                FN[i,j]=3
            elif gt_mask[i,j]==0 and SOM_mask[i,j]==255:
                FP[i,j]=4
                
    
    #Adding colour to the arrays
    clas_im=TP+TN+FN+FP                  
    final_class=np.zeros((3,1830,1830))
    for i in range (1830):
        for j in range (1830):
            if clas_im[i,j]==1:
                final_class[0,i,j]=0
                final_class[1,i,j]=102
                final_class[2,i,j]=102
            elif clas_im[i,j]==2:  
                final_class[0,i,j]=0
                final_class[1,i,j]=102
                final_class[2,i,j]=204
            elif clas_im[i,j]==3:  
                final_class[0,i,j]=255
                final_class[1,i,j]=102
                final_class[2,i,j]=102
            elif clas_im[i,j]==4:  
                final_class[0,i,j]=153
                final_class[1,i,j]=0
                final_class[2,i,j]=0  
               
    final_class2=np.uint8(final_class)     
    new_filename = file_name.split('.')[0]   
    tiff.imsave(new_filename + "_class.tif", final_class2)


    
    
   
    
    
    
   
    

        
