# -*- coding: utf-8 -*-
#Name: Fractal Engine
#Author: Sean Pope

#Backend functions to implement the iterated function system.
#Used to output an array of points that result from the supplied coefficients.

import numpy as np

dims = {  #May eventually provide support for higher dimensions.
    'dtype': [('x',np.float16),('y',np.float16),('color',np.float16)]
}


def bound(x,y,*args):
    return np.clip([x,y],-1e4,1e4)


def ifs(inpoint,flist,weightlist,variation,alpha):
    """ Select a coefficient set and apply the transform. """
    fselectindex = np.random.random() * (len(weightlist))  #Get a random coeff index
    fchoice = weightlist[int(np.floor(fselectindex))]
    fselect = flist[fchoice]  #Grab the coefficients for this iteration

    weight, a1, b1, c1, a2, b2, c2 = fselect  #Unpack variables for clarity
    xi,yi,ci = inpoint['x'], inpoint['y'], inpoint['color']  #Unpack point
    xn,yn = (((a1 * xi) + (b1 * yi) + c1),
             ((a2 * xi) + (b2 * yi) + c2)
    )  #Generic IFS function

    if callable(variation):  #If a variation function is supplied, apply it
        xn, yn = variation(xn,yn,a1,b1,c1,a2,b2,c2)

    cn =  (ci * (1.-alpha)) + (fchoice * alpha)   #Blends the old color and new function color.

    outarr = np.array((xn,yn,cn),**dims)

    return outarr



def fractpoints(coeffs,     iters=10000,    variation=bound,
                alpha=0.5,  startpos=None,  cutin=20
                ):
    """
    Generate a structured array of x,y points for the given fractal IFS coefficients.

    ---

    Coeffs (numpy array, nx7: An array with one row for each IFS function to implement.
    Each row expects values with the following schema:

    weight,  a1,     b1,     c1,     a2,     b2,     c2
    And implements the generic IFS function:

    F{x_new, y_new} = { (a1*xi) + (b1*yi) + c1, (a2*xi) + (b2*yi) + c2) }

    iters: How many points to create.

    startpos: Expects an (x,y) tuple to start the figure.
    If one isn't supplied, a random point in the unit square is chosen.

    alpha: Scales the color blending function severity.

    cutin: How many iterations are discarded before points are reported.
    """

    weightlist = []  #precompute the weight table to get a weighted random
    for findex in range(coeffs.shape[0]):  #For each coefficient list,
        for fweight in np.arange(coeffs[findex][0]):  #Append the index (weight) times
            weightlist.append(findex)

    if startpos:  #If a starting location is supplied, initalize from it.
        point = np.array(startpos,**dims)
    else:  #Otherwise, start randomly in the unit square.
        point = np.random.random(2)
        point = np.array((point[0],point[1],0),**dims)

    fractal = np.zeros(iters+1-cutin,**dims)
    fractal[0] = point
    for iteration in range(iters):
        point = ifs(point,coeffs,weightlist,variation,alpha)
        if iteration > cutin:
            fractal[iteration-cutin] = point

    return fractal

