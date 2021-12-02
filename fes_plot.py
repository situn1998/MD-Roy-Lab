import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

## Imput parameters ## 
demo_file = "bck.0.fes.dat"
x_label = "RMSD Switch-I"
y_label = "COM Distance"

## Reading the file ##
data = open(demo_file,"r")
demolines = []
for line in data:
    line_split = line.split()
    demolines.append(line_split)

## Extracting the X coordinates ##
x = []
for i in demolines:
    if i != []:
        if i[0] != "#!":
            x.append(float(i[0]))
    else:
        break
x = np.array(x)

## Extracting the Y coordinates ##
y = []
for j in demolines:
    if j != []:
        if j[0] != "#!":
            y.append(float(j[1]))
y = np.unique(y)

## Extracting the Z coordinates ##
Z = np.zeros([len(y),len(x)])
temp = []
a = 0
for k in demolines:
    if k != []:
        if k[0] != "#!":
                temp.append(float(k[2]))
    else:
        temp = []
        a = a+1
    if len(temp) == len(x):
        Z[a,:] = temp

X,Y = np.meshgrid(x,y)

## For 2D Plot ##
fig, ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp, ax=ax)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
plt.savefig("2D-Energy Plot")
plt.show()

## For 3D Plot ##
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_zlabel('Potential')
plt.show()