#Detecting the BMUs

#Importing libraries
import numpy as np
import susi #The susi package can be found in https://pypi.org/project/susi/
import pickle

#Load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)

#size: number of rows of the training set
size=len(X_train) #X_train was defined in "data_preprocessing.py"

#Separating the training spectra into smaller arrays 
X_train1=X_train[0:1000000,:]
X_train2=X_train[1000000:2000000,:]
X_train3=X_train[2000000:3000000,:]
X_train4=X_train[3000000:4000000,:]
X_train5=X_train[4000000:5000000,:]
X_train6=X_train[5000000:6000000,:]
X_train7=X_train[6000000:7000000,:]
X_train8=X_train[7000000:8000000,:]
X_train9=X_train[8000000:size,:]

#Detecting the coordinates of the Best Matching Units (BMUs) for each spectral signature of the training set. The coordinates are stored in a list data type.
print(" Cluster 1" )
clusters1 = som.get_clusters(X_train1)
print(" Cluster 2" )
clusters2 = som.get_clusters(X_train2)
print(" Cluster 3" )
clusters3 = som.get_clusters(X_train3)
print(" Cluster 4" )
clusters4 = som.get_clusters(X_train4)
print(" Cluster 5" )
clusters5 = som.get_clusters(X_train5)
print(" Cluster 6" )
clusters6 = som.get_clusters(X_train6)
print(" Cluster 7" )
clusters7 = som.get_clusters(X_train7)
print(" Cluster 8" )
clusters8 = som.get_clusters(X_train8)
print(" Cluster 9" )
clusters9 = som.get_clusters(X_train9)

#Joining all BMU lists to one
clusters=clusters1+clusters2+clusters3+clusters4+clusters5+clusters6+clusters7+clusters8+clusters9

#Creating an array data type to store the BMUs
BMUs=np.zeros((size,2))

for i in range (size):
    BMUs[i,:]=clusters[i]

#Saving the BMUs in a .csv file
np.savetxt('BMUs.csv', BMUs, delimiter=',', header="position1, #position2", fmt='%10.0f')







