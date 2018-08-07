# -*- coding: utf-8 -*-
#Name: Fractal Visualizer
#Author: Sean Pope

#Example use of the fractal engine and coefficients.
#Plots a simple representation of the solution set from the engine.

import matplotlib.pyplot as plt
import fractcoeffs as fc
import fracteng as fe
import fractvars as fv

plt.style.use('dark_background')
framecount = 0

ax = plt.subplot(111,frameon=False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.frameon=False
plt.xlim(-1,1)
plt.ylim(-1,1)


coeffs = fv.rand(0.8)
for x in range(40):
    fractal = fe.fractpoints(coeffs, 200, fc.exponential)  #Run the engine to get a figure.
    plt.scatter(fractal['x'],        fractal['y'],        #Get the x,y coordinates for each point
                marker='.',          alpha=0.8,           #Use small pixel markers with low opacity
                c=fractal['color'],  cmap='plasma',       #Map the color row to this colormap.
                s=25,                edgecolor='none'
                )

    plt.pause(.01)

while(1):

    if framecount == 39:
        coeffs = fv.rand(0.8)
        framecount -= 40
    framecount += 1

    fractal = fe.fractpoints(coeffs, 200, fc.exponential)  #Run the engine to get a figure.
    plt.scatter(fractal['x'],        fractal['y'],   #Get the x,y coordinates for each point
                marker='.',          alpha=0.8,         #Use small pixel markers with low opacity
                c=fractal['color'],  cmap='plasma',  #Map the color row to this colormap.
                s=25,                edgecolor='none'
                )

    del ax.collections[0]


    plt.pause(.01)