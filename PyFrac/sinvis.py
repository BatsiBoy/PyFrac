# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:47:01 2018

@author: J73072
"""

# -*- coding: utf-8 -*-
#Name: Fractal Visualizer
#Author: Sean Pope

#Example use of the fractal engine and coefficients.
#Plots a simple representation of the solution set from the engine.

import matplotlib.pyplot as plt
import fractcoeffs as fc
import fracteng as fe
import time


plt.style.use('dark_background')
framecount = 0

while(1):
    start = time.time()
    framecount += 1
    coeffs = fc.rand()  #See the fractcoeffs file for other premade coefficient blocks.

    fractal = fe.fractpoints(coeffs,500,fc.sin)  #Run the engine to get a figure.
    fractime = time.time()

    plt.clf()
    plt.scatter(fractal['x'],       fractal['y'],  #Get the x,y coordinates for each point
                marker='.',         alpha=1,  #Use small pixel markers with low opacity
                c=fractal['color'], cmap='viridis',  #Map the color row to this colormap.
                s=10,                edgecolor='none'
    )
    ax = plt.gca()
    ax.axes.get_xaxis().set_visible(True)
    ax.axes.get_yaxis().set_visible(True)
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    end = time.time()
    print("Frame:\t%i\tFractal:\t%f\tPlot:\t%f\tTotal:\t%f" %
    (framecount, fractime - start, end - fractime, end - start))

    plt.pause(.01)