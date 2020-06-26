#Data preprocessing

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the datasets
# The datasets are two .csv files which were created by extracting the spectra from two .h5 files as explained in the file "read_h5file.py". Each row contains 14 collumns: a) 13 collumns for the reflectance values of Sentinel-2 satellite spectra, b) one column for the label of the spectra. There are six classes, thus six different labels:"10:land", "20:water", "30:shadow", "40:cirrus", "50:opaque cloud", "60:snow".  

dataset1 = pd.read_csv('2016_spectraSOMs.csv') #.csv file with spectra extracted from the first .h5 file.
X_train1 = dataset1.iloc[:, 'collumn of 1st band':'collumn of last band'].values
y1=dataset1.iloc[:, "collumn with labels"].values

dataset2 = pd.read_csv('2017_spectraSOMs.csv') #.csv file with spectra extracted from the second .h5 file.
X_train2 = dataset2.iloc[:, 'collumn of 1st band':'collumn of last band'].values
y2=dataset2.iloc[:, "collumn with labels"].values

# Concatenating the spectra of the two datasets in one array
X_traina=np.concatenate((X_train1,X_train2), axis=0) 

# Concatenating the labels of the two datasets in one array
ya=np.concatenate((y1,y2), axis=0)

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X_train = sc.fit_transform(X_traina)








