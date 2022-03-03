# import required libraries
import h5py as h5
import numpy as np

# Read H5 file
# This file carries a database with spectra for cloud masking applications. It was created during the study described in https://doi.org/10.3390/rs8080666
# It can be downloaded from https://git.gfz-potsdam.de/EnMAP/sentinel2_manual_classification_clouds

f = h5.File("20170412_s2_manual_classification_data.h5", "r")

# Get and print list of datasets within the H5 file
datasetNames = [n for n in f.keys()]
for n in datasetNames:
        print(n)
        
# extract reflectance data from the H5 file

#class_ids 
class_ids=f['class_ids']
class_idsData=class_ids[:]

#class_names
class_names=f['class_names']
print(class_names[:])

#spectra
spectra=f['spectra'] 
spectraData=spectra[:]   

#classes
classes=f['classes'] 
classesData=classes[:]  

# Create array that contains the spectra and the class labels
'''Each row contains 14 collumns: a) 13 collumns for the reflectance values of Sentinel-2 satellite spectra,
#b) one column for the label of the spectra. There are six classes, thus six different
 labels:"10:land", "20:water", "30:shadow", "40:cirrus", "50:opaque cloud", "60:snow".'''
classesData=np.expand_dims(classesData,1)
Array_spectra_labels=np.concatenate((spectraData,classesData), axis=1)

#Save the array with the spectra and the labels
np.savetxt("2017_spectraSOMs.csv", Array_spectra_labels, delimiter=',', header=" #B1,  #B2,  #B3,  #B4, #B5, #B6, #B7, #B8, #B8a, #B9, #B10, #B11, #B12, #label",fmt='%10.4f')
