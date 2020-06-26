#Labeling of SOM neurons through majority voting

#Importing libraries
import numpy as np
import pandas as pd

#Reading the .csv file that contains the coordinates of the Best Matching Units (BMUs) for each spectral signature of the training set.

BMUs = pd.read_csv('BMUs.csv') #The "BMUs.csv" file was created in "BMUs_detection.py"         
BMUs2=np.array(BMUs)

#Creating an array of zeros which is of equal size to the SOM grid for each of the six classes
Hit1=np.zeros((20,15))
Hit2=np.zeros((20,15))
Hit3=np.zeros((20,15))
Hit4=np.zeros((20,15))
Hit5=np.zeros((20,15))
Hit6=np.zeros((20,15))

#Creating the hit rate map for each class
#ya: the data labels ("ya" is created in "data_preprocessing.py")
for i in range (size):
    if (ya[i]==10):
        Hit1[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit1[int(BMUs2[i,0]),int(BMUs2[i,1])]+1
    elif (ya[i]==20):
        Hit2[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit2[int(BMUs2[i,0]),int(BMUs2[i,1])]+1         
    elif (ya[i]==40):
        Hit3[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit3[int(BMUs2[i,0]),int(BMUs2[i,1])]+1        
    elif(ya[i]==50):
        Hit4[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit4[int(BMUs2[i,0]),int(BMUs2[i,1])]+1 
    elif(ya[i]==60):
        Hit5[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit5[int(BMUs2[i,0]),int(BMUs2[i,1])]+1    
    elif(ya[i]==30):
        Hit6[int(BMUs2[i,0]),int(BMUs2[i,1])]=Hit6[int(BMUs2[i,0]),int(BMUs2[i,1])]+1        

#Labeling of SOM neurons

#Creating an array of zeros which is of equal size to the SOM grid and store the majority voting output
labels= np.zeros((20,15))
for i in range (20):
    for j in range (15):
        if (Hit1[i,j]>Hit2[i,j] and Hit1[i,j]>Hit3[i,j] and Hit1[i,j]>Hit4[i,j] and Hit1[i,j]>Hit5[i,j] and Hit1[i,j]>Hit6[i,j]):
           labels[i,j]=10
        elif (Hit2[i,j]>Hit1[i,j] and Hit2[i,j]>Hit3[i,j] and Hit2[i,j]>Hit4[i,j] and Hit2[i,j]>Hit5[i,j] and Hit2[i,j]>Hit6[i,j]):
           labels[i,j]=20
        elif (Hit3[i,j]>Hit1[i,j] and Hit3[i,j]>Hit2[i,j] and Hit3[i,j]>Hit4[i,j] and Hit3[i,j]>Hit5[i,j] and Hit3[i,j]>Hit6[i,j]):
           labels[i,j]=40           
        elif (Hit4[i,j]>Hit1[i,j] and Hit4[i,j]>Hit2[i,j] and Hit4[i,j]>Hit3[i,j] and Hit4[i,j]>Hit5[i,j] and Hit4[i,j]>Hit6[i,j]):
           labels[i,j]=50    
        elif (Hit5[i,j]>Hit1[i,j] and Hit5[i,j]>Hit2[i,j] and Hit5[i,j]>Hit3[i,j] and Hit5[i,j]>Hit4[i,j] and Hit5[i,j]>Hit6[i,j]):
           labels[i,j]=60  
        elif (Hit6[i,j]>Hit1[i,j] and Hit6[i,j]>Hit2[i,j] and Hit6[i,j]>Hit3[i,j] and Hit6[i,j]>Hit4[i,j] and Hit6[i,j]>Hit5[i,j]):
           label[i,j]=30 

#Conversion of the six classes to two (cloud:"40,50", non-cloud:"10,20,30,60")
labels2=np.zeros((20,15))

for i in range(20):
    for j in range(15):
        if labels[i,j]==40 or labels[i,j]==50:
            labels2[i,j]=255





