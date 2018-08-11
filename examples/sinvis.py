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
#This example is optimized for the sine transform.
#It also reports time statistics per frame for benchmarking.

import matplotlib.pyplot as plt
import PyFrac as pf
import time


plt.style.use('dark_background')

ax = plt.subplot(111,frameon=False)  #Create a figure and axes for drawing.
ax.axes.get_xaxis().set_visible(False)  #Hide axis
ax.axes.get_yaxis().set_visible(False)
plt.xlim(-1,1)  #This function looks best in the biunit square.
plt.ylim(-1,1)


def quitloop(*args):  #Closes the event loop when no longer needed.
    global run
    run = 0
    return

fig = plt.gcf()  #Get the figure that pyplot spawned.
fig.canvas.mpl_connect('close_event', quitloop)  #If the window is closed, exit loop to free the kernel
fig.canvas.mpl_connect('key_press_event', quitloop)  #If a button is pressed, close everything.

run = 1
framecount = 0

while(run):
    start = time.time()
    framecount += 1
    coeffs = pf.coeffs.rand()  #See the fractcoeffs file for other premade coefficient blocks.

    fractal = pf.engine.fractpoints(coeffs,50000,pf.variations.sin)  #Run the engine to get a figure.
    fractime = time.time()

    plt.clf()
    plt.scatter(fractal['x'],       fractal['y'],  #Get the x,y coordinates for each point
                marker='.',         alpha=1,  #Use small pixel markers with low opacity
                c=fractal['color'], cmap='viridis',  #Map the color row to this colormap.
                s=10,                edgecolor='none'
    )

    end = time.time()
    print("Frame:\t%i\tFractal:\t%f\tPlot:\t%f\tTotal:\t%f" %
    (framecount, fractime - start, end - fractime, end - start))

    plt.pause(1)