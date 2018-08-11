# -*- coding: utf-8 -*-
#Name: Fractal Example - Exponential Curves
#Author: Sean Pope

#Example use of the fractal engine and coefficient block.
#Creates random coefficient blocks and draws frames to create a simple animation.
#This one is optimized for the exponential variation.

import matplotlib.pyplot as plt
import PyFrac as pf

plt.style.use('seaborn-notebook')

ax = plt.subplot(111, frameon=False)  #Create a figure and axes for drawing.
ax.axes.get_xaxis().set_visible(False)  #Hide axis
ax.axes.get_yaxis().set_visible(False)
plt.xlim(-5,5)  #This function looks best thinner

#Uncomment below for fullscreen
#mng = plt.get_current_fig_manager()  #Grab the figure window
#mng.full_screen_toggle()  #Maximize the image to fill the screen.

""" Runtime variables """

run = 1  #Set to continue drawing frames, unset to terminate
framecount = 0  #Used to set frames drawn per coefficient block
frameclear = 0  #Starts deleting frames when set

""" Runtime functions. """

def quitloop(*args):  #Closes the event loop when no longer needed.
    global run
    run = 0
    return

fig = plt.gcf()  #Get the figure that pyplot spawned.
fig.canvas.mpl_connect('close_event', quitloop)  #If the window is closed, exit loop to free the kernel
fig.canvas.mpl_connect('key_press_event', quitloop)  #If a button is pressed, close everything.

coeffs = pf.coeffs.fern

""" Main event loop. """



while(run):  #Check if the event loop has not been interrupted
    framecount += 1
    if framecount == 600:  #Draws a new coefficient set when the frame limit is reached.
       frameclear = 1  #Set the deletion flag        
       framecount -= 600  #Reset frame counter.

    fractal = pf.engine.fractpoints(coeffs, 100)  #Run the engine to get a figure.
    plt.scatter(fractal['x'],        fractal['y'],   #Get the x,y coordinates for each point
                marker='.',          alpha=0.8,         #Use small pixel markers with low opacity
                c=fractal['color'],  cmap='viridis',  #Map the color row to this colormap.
                s=15,                edgecolor='k'
                )
    if frameclear:
        del ax.collections[0]  #Remove the oldest frame.

    plt.pause(.01)  #This pause draws the frame before looping.


plt.close(fig)