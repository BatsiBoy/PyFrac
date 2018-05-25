# -*- coding: utf-8 -*-
#Name: Fractal Visualizer
#Author: Sean Pope

#Example use of the fractal engine and coefficients.
#Plots a simple representation of the solution set from the engine.

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import fractcoeffs as fc
import fracteng as fe

fig = plt.figure(facecolor='k')
ax  = fig.add_axes([0,0,1,1],frameon=False)

coeffs = None
def update(frame):
    global coeffs
    if frame == 0:  #Run the engine to get a new figure.
        coeffs = fc.rand(0.5,'q')
        #Return a random coefficient block scaled between -0.5 and 0.5
        #Use quadrature symmetry for output
    del ax.collections[0]
    fractal = fe.fractpoints(coeffs, 1000, fc.horseshoe)
    plt.scatter(fractal['x'],        fractal['y'],    #Get the x,y coordinates for each point
                marker='.',          alpha=0.7,       #Use small pixel markers with low opacity
                c=fractal['color'],  cmap='plasma',   #Map the color row to this colormap.
                s=10,                edgecolor='none'
                )

    return ax.collections



def init():
    global coeffs
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)

    coeffs = fc.rand(0.5,'q')
    for ite in range(15):
        fractal = fe.fractpoints(coeffs, 1000, fc.horseshoe)
        plt.scatter(fractal['x'],         fractal['y'],    #Get the x,y coordinates for each point
                    marker='.',           alpha=0.7,       #Use small pixel markers with low opacity
                    c=fractal['color'],   cmap='plasma',   #Map the color row to this colormap.
                    s=10,                 edgecolor='none'
                    )

    return ax.collections


FuncAnimation(fig,update,frames=30,init_func=init)
plt.show()
