#Creating and plotting the U-matrix

#Importing libraries
import numpy as np
import susi  #The susi package can be found in https://pypi.org/project/susi/
import pickle
import matplotlib.pyplot as plt

#Load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)

#Creating the U-matrix
u_matrix = som.get_u_matrix() #This command creates a U-matrix with shape:39,29,1 when the SOM grid size is 20,15

u_matrix2=np.squeeze(u_matrix) #This command creates a U-matrix with shape:39,29

u_matrix_final=u_matrix2[::2,::2] #This command creates a U-matrix with shape:20,15

u_matrix_log=np.log(u_matrix_final) #This command computes the natural logarithm of U-matrix. It is useful for vizualisation.
    

#Simple way to plot and save the U-matrix
plt.imshow(u_matrix_final, cmap="viridis")
plt.colorbar()
plt.savefig("U_matrix")
plt.show()
plt.close()

#Plot the U-matrix with white grid lines
plt.imshow(u_matrix_final, cmap="viridis")
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

plt.savefig("U_matrix",dpi=300)
plt.show()
plt.close()
