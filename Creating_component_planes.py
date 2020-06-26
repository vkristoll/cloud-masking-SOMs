# Creating and plotting the component planes

#Importing libraries
import numpy as np
import susi  #The susi package can be found in https://pypi.org/project/susi/
import pickle
import matplotlib.pyplot as plt

#Load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)

#Command that creates an array of size 20,15,13 (i.e. number of SOM grid rows, number of SOM grid columns,number of Sentinel-2 bands) which contains the weights of the trained SOM

weights=som.unsuper_som_

#Create an array with shape 300,13 to store the weights (15x20=300)

weights2=np.zeros((300,13))
c=0

for i in range (20):
    for j in range (15):
        weights2[c,:]=weights[i,j,:]
        c=c+1

#Simple way to plot and save the component planes for the 13 Sentinel-2 bands
for i in range (13):
    component=weights2[:,i]
    componentb=np.reshape(component,(20,15))
    plt.imshow(componentb, cmap="viridis")
    plt.colorbar() 
    plt.savefig("component" +str(i) +"png")   
    plt.show()
    plt.close()

#Plot the component planes with white grid lines  
for i in range (13):
    component=weights2[:,i]
    componentb=np.reshape(component,(20,15))
    plt.imshow(componentb, cmap="viridis")       
    ax=plt.gca()
    plt.colorbar()

    # Major ticks
    ax.set_xticks([0,4,9,14])
    ax.set_yticks([0,4,9,14,19])

    # Minor ticks
    ax.set_xticks(np.arange(-0.5, 15, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)

    # Labels for major ticks
    x_label_list = ['1', '5', '10', '15']
    y_label_list = ['1', '5', '10', '15', '20']

    ax.set_xticklabels(x_label_list)
    ax.set_yticklabels(y_label_list)
      
    # Gridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

    plt.savefig("component" +str(i) ,dpi=300)
    plt.show()
    plt.close()    
    

    

 
    
    
    
    


