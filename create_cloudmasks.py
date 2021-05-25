#Create cloud masks

#Importing libraries
import os, re
import pandas as pd
from os.path import splitext
import numpy as np
import tifffile as tiff
import time

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X_train = sc.fit_transform(X_traina) #"X_traina" was created in "data_preprocessing.py"

directory = os.listdir('path to folder with .csv files containing spectra for the images')
os.chdir('path to folder with .csv files containing spectra for the images')

#Sorting the directory according to the names of the files 
directory2=sorted(directory)

c=0
start_time = time.time()
for file in directory2:
    c=c+1
    print(" The file number is %s" %c) 
    print("--- %s seconds ---" % (time.time() - start_time)) 
    
    #Reading the spectra for an image        
    im=pd.read_csv(file)  
    im2=np.array(im)  
 
    size=len(im)      

    im3= sc.transform(im2) #normalizes the test data based on the statistical parameters of the training data                
      
    #Separating the image spectra into smaller arrays. The size of each image is 1830x1830 pixels thus 3348900 spectra in total    
    X_test1=im3[0:500000,:]
    X_test2=im3[500000:1000000,:]
    X_test3=im3[1000000:1500000,:]
    X_test4=im3[1500000:2000000,:]
    X_test5=im3[2000000:2500000,:]
    X_test6=im3[2500000:3000000,:]
    X_test7=im3[3000000:size,:]
    
    #Detecting the coordinates of the Best Matching Units (BMUs) for each spectral signature. The coordinates are stored in a list data type.
    clusters1 = som.get_clusters(X_test1)    
    clusters2 = som.get_clusters(X_test2)
    print(" Cluster 3" )
    clusters3 = som.get_clusters(X_test3)
    clusters4 = som.get_clusters(X_test4)
    print(" Cluster 5" )
    clusters5 = som.get_clusters(X_test5)
    clusters6 = som.get_clusters(X_test6)    
    clusters7 = som.get_clusters(X_test7)
    print(" Finished clusters" )
    
    #Joining all BMU lists to one
    clusters=clusters1+clusters2+clusters3+clusters4+clusters5+clusters6+clusters7

    #Creating an array data type to store the BMUs
    im_BMUs=np.zeros((size,2))

    for i in range (size):
        im_BMUs[i,:]=clusters[i]

    #Creating an array to store the labels for the spectra of the image
    im_labels=np.zeros((size,1))

    for i in range(size):
        im_labels[i,0]=label2[int(im_BMUs[i,0]),int(im_BMUs[i,1])] #"labels2" was created in "labeling.py"

    #Creating the cloud mask 
    im_labels2=np.uint8(im_labels)      
    reshape=np.reshape(im_labels2,(1830,1830)) 
    file_name = os.path.basename(file)
    new_filename = file_name.split('.')[0]   
    tiff.imsave(new_filename + "mask.tif", reshape)
   




