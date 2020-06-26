#Creating and plotting hit rate maps

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

#Creating the hit rate map for all classes
Hit_all=Hit1+Hit2+Hit3+Hit4+Hit5+Hit6

#Simple way to plot and save the hit rate map
plt.imshow(Hit_all, cmap="viridis")
plt.colorbar()
plt.savefig("Hit_all")
plt.show()
plt.close()

#Plot the hit rate map with white grid lines
plt.imshow(Hit_all, cmap="viridis")
ax=plt.gca()
plt.colorbar()

#Major ticks
ax.set_xticks([0,4,9,14])
ax.set_yticks([0,4,9,14,19])

#Minor ticks
ax.set_xticks(np.arange(-0.5, 15, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)

#Labels for major ticks
x_label_list = ['1', '5', '10', '15']
y_label_list = ['1', '5', '10', '15', '20']

ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)

#Gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.savefig("Hit_all",dpi=300)
plt.show()
plt.close()

