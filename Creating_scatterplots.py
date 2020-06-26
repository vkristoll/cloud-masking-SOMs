#Creating scatterplots

#Importing libraries
import numpy as np
import susi #The susi package can be found in https://pypi.org/project/susi/
import pickle
import matplotlib.pyplot as plt

#load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)

#Defining six counters for the spectra of the six classes of the data in order to find the total number of spectra for each class
#ya: the data labels ("ya" is created in "data_preprocessing.py")
#size: number of rows of the training set (size=len(X_train))

c10=0
c20=0
c30=0
c40=0
c50=0
c60=0

for i in range(size):
    if ya[i]==10:
        c10=c10+1
    elif ya[i]==20:
        c20=c20+1
    elif ya[i]==30:
        c30=c30+1 
    elif ya[i]==40:
        c40=c40+1
    elif ya[i]==50:
        c50=c50+1
    elif ya[i]==60:
        c60=c60+1 

#Load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)

#Command that creates an array of size 20,15,13 (i.e. number of SOM grid rows, number of SOM grid columns,number of Sentinel-2 bands) which contains the weights of the trained SOM

weights=som.unsuper_som_

#Create an array which contains the SOM weights that correspond to the misclassified bright non-cloud spectra (18 in number)       
 
bright_non_cloud=np.zeros((18,13))

bright_non_cloud[0,:]=weights["row in the SOM grid for first point","column in the SOM grid for first point",:] 
bright_non_cloud[1,:]=weights["row in the SOM grid for second point","column in the SOM grid for second point",:]
...
...
bright_non_cloud[17,:]=weights["row in the SOM grid for last point","column in the SOM grid for last point",:]

#Create two arrays for each of the six classes to store the spectra for two chosen bands which will be used for the scatterplot

X10=np.zeros((c10,1)) # array that stores the spectra for "land" class (first chosen band)
X10b=np.zeros((c10,1)) # array that stores the spectra for "land" class (second chosen band)
X20=np.zeros((c20,1)) # array that stores the spectra for "water" class (first chosen band)
X20b=np.zeros((c20,1)) # array that stores the spectra for "water" class (second chosen band)
X30=np.zeros((c30,1)) # array that stores the spectra for "shadow" class (first chosen band)
X30b=np.zeros((c30,1)) # array that stores the spectra for "shadow" class (second chosen band)
X40=np.zeros((c40,1)) # array that stores the spectra for "cirrus" class (first chosen band)
X40b=np.zeros((c40,1)) # array that stores the spectra for "cirrus" class (second chosen band)
X50=np.zeros((c50,1)) # array that stores the spectra for "opaque cloud" class (first chosen band)
X50b=np.zeros((c50,1)) # array that stores the spectra for "opaque cloud" class (second chosen band)
X60=np.zeros((c60,1)) # array that stores the spectra for "snow" class (first chosen band)
X60b=np.zeros((c60,1))  # array that stores the spectra for "snow" class (second chosen band)

#Defining six counters for the spectra of the six classes of the data
count10=0
count20=0
count30=0
count40=0
count50=0
count60=0

#size: number of rows of the training set (size=len(X_train))
for i in range (size):
    if ya[i]==10:
        count10=count10+1
        X10[count10-1,0]=X_train[i,7] #X_train was defined in "data_preprocessing.py"
        X10b[count10-1,0]=X_train[i,11]
    elif ya[i]==20:
        count20=count20+1
        X20[count20-1,0]=X_train[i,7]
        X20b[count20-1,0]=X_train[i,11]
    elif ya[i]==30:
        count30=count30+1
        X30[count30-1,0]=X_train[i,7] 
        X30b[count30-1,0]=X_train[i,11] 
    elif ya[i]==40:
        count40=count40+1
        X40[count40-1,0]=X_train[i,7]    
        X40b[count40-1,0]=X_train[i,11] 
    elif ya[i]==50:
        count50=count50+1
        X50[count50-1,0]=X_train[i,7]   
        X50b[count50-1,0]=X_train[i,11] 
    elif ya[i]==60:
        count60=count60+1
        X60[count60-1,0]=X_train[i,7]  
        X60b[count60-1,0]=X_train[i,11] 

#Create an array with shape 300,13 to store the weights (15x20=300)

weights2=np.zeros((300,13))
c=0

for i in range (20):
    for j in range (15):
        weights2[c,:]=weights[i,j,:]
        c=c+1

#Creating separate scatterplots for each class. Each scatterplot contains: a) spectral values of the training data for two bands (e.g. X10,X10b), b) the SOM weights for the two bands (w1,w2) and c) the SOM weights for the two bands that correspond to the bright non-cloud spectra (bright1, bright2)

w1=weights2[:,7]
w2=weights2[:,11]

bright1=bright_non_cloud[:,7]
bright2=bright_non_cloud[:,11]

#Creating and saving the scatterplot for the "land" class    
plt.scatter(X10,X10b,s=2,marker='p',c="#0066CC")            
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1)
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)    
plt.savefig("scatterplot_land_b7_b11",dpi=300)
plt.show()
plt.close()

#Creating and saving the scatterplot for the "water" class           
plt.scatter(X20,X20b,s=2,marker='p',c="#305496")    
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1)  
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)   
plt.savefig("scatterplot_water_b7_b11",dpi=300)
plt.show()
plt.close()  

#Creating and saving the scatterplot for the "shadow" class        
plt.scatter(X30,X30b,s=2,marker='p',c="#5B9BD5") 
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1)  
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)    
plt.savefig("scatterplot_shadow_b7_b11",dpi=300)
plt.show()
plt.close()  

#Creating and saving the scatterplot for the "cirrus" class 
plt.scatter(X40,X40b,s=2,marker='p',c="#009999") 
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1) 
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)   
plt.savefig("scatterplot_cirrus_b7_b11",dpi=300)
plt.show()
plt.close()  

#Creating and saving the scatterplot for the "opaque cloud" class         
plt.scatter(X50,X50b,s=2,marker='p',c="#006666") 
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1) 
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)   
plt.savefig("scatterplot_opaque_cloud_b7_b11",dpi=300)
plt.show()
plt.close() 

#Creating and saving the scatterplot for the "snow" class           
plt.scatter(X60,X60b,s=2,marker='p',c="#9BC2E6")
plt.plot(w1,w2,linewidth=0.5,c='y',marker='p',markerfacecolor='black',markeredgecolor='black',markersize=1) 
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)   
plt.savefig("scatterplot_opaque_cloud_b7_b11",dpi=300)
plt.show()
plt.close() 

# Create a scatterplot that contains all classes
plt.scatter(X60,X60b,s=2,marker='p',c="#9BC2E6") 
plt.scatter(X50,X50b,s=2,marker='p',c="#006666")
plt.scatter(X40,X40b,s=2,marker='p',c="#009999")
plt.scatter(X10,X10b,s=2,marker='p',c="#0066CC")
plt.scatter(X30,X30b,s=2,marker='p',c="#5B9BD5") 
plt.scatter(X20,X20b,s=2,marker='p',c="#305496") 
plt.plot(w1,w2, linewidth=0.5, c='y',marker='p',markerfacecolor='black', markeredgecolor='black',markersize=1) 
plt.plot(bright1,bright2,markersize=1,marker='p',c="r",linewidth=0)  
plt.savefig("scatterplot_all_b7_b11",dpi=300)              
plt.show()
plt.close()

