import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

## Input parameters ## 
demo_file = "fes.dat"
x_label = "COM P-loop & Switch-I"
y_label = "COM P-loop & Switch-II"
z_label = r"Potential (kcal/mol)"

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
fig, ax = plt.subplots(1,1)
width = np.linspace(np.min(Z),np.max(Z),500)
cp = ax.contourf(X, Y, Z, levels = width, cmap = cm.jet)
cbar = fig.colorbar(cp)
cbar.set_label(z_label, labelpad=20.0, rotation=270)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
plt.savefig("2D-Energy Plot")
plt.show()

## For 3D Plot ##
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_zlabel(z_label)
plt.show()

## Animation ##
var = str(input("\nDo you want to animate the 3D surface? [y/n]: "))
print(" ")
if var.lower() == "y":
    def init():
        ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)
        return fig,
    def animate(i):
        ax.view_init(elev = 10., azim = i)
        return fig,
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 360, interval = 10, blit = True)
    anim.save('2D-Energy Plot.mp4', fps = 30, extra_args=['-vcodec', 'libx264'], dpi = 250)
else:
    exit()
    
