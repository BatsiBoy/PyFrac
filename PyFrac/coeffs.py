# -*- coding: utf-8 -*-

import numpy as np


""" Known patterns. """

sierp = np.array([  #The classic Sierpinski triangle
# weight,  a1,     b1,     c1,     a2,     b2,     c2
    (1,    0.5,    0.,     0.,     0.,     0.5,    0.   ),
    (1,    0.5,    0.,     0.5,    0.,     0.5,    0.   ),
    (1,    0.5,    0.,     0.25,   0.,     0.5,    0.5  )
])

fern = np.array([  #Converges to a self-similar fern leaf
# weight,  a1,     b1,     c1,     a2,     b2,     c2
    (1,    0.,     0.,     0.,     0.16,   0.,     0.   ),
    (7,    0.2,   -0.26,   0.,     0.23,   0.22,   1.6  ),
    (7,   -0.15,   0.28,   0.,     0.26,   0.24,   0.44 ),
    (85,   0.85,   0.04,   0.,    -0.04,   0.85,   1.6  ),
])

""" Debug blocks. """

ones = np.array([  #All ones
# weight,  a1,     b1,     c1,     a2,     b2,     c2
    (1,    1.,     1.,     1.,     1.,     1.,     1.   )
])

passthrough = np.array([  #Returns input
# weight,  a1,     b1,     c1,     a2,     b2,     c2
    (1,    1.,     0.,     0.,     0.,     1.,     0.   )
])

null = np.array([  #All zeroes
# weight,  a1,     b1,     c1,     a2,     b2,     c2
    (1,    0.,     0.,     0.,     0.,     0.,     0.   ),
])


""" Procedural random coefficient functions. """


def rand(scale=1,minf=0.05,sym=None):
    """
    Produce a random coefficient array for variable outputs.

    Produces 1 to 5 rows of random weights and affine factors scaled between -1 and 1.
    Also implements several symmetries.

    Scale: Multiplies all coefficients before adding to the arroy, good for forcing contraction.

    minf: Minimum allowable coefficient magnitude, excluding symmetry rows.

    sym: Accepts a keyword to create symmetry rows for the output matrix.
    'x': Reflects about the X axis.
    'y': Reflects about the y axis.
    't': 3-fold symmetry oriented toward positive y.
    'q': 4-fold symmetry about the axes.
    """
    randrows = int(np.ceil(np.random.random() * 4)) + 1  #Between 1 and 5 rows
    randarray = []  #Empty return list

    for _ in range(randrows):
        workrow = []
        workrow.append(int(np.ceil((np.random.random() * 10))))  #Add random weight from (1,10)
        for _ in range(6):
            newcoeff = (np.cos(np.random.random()*np.pi)) * scale  #cos(x) for [0,pi]
            if newcoeff < minf and newcoeff > -0.05:  #within minimum magnitude
                newcoeff == np.clip(newcoeff,-minf,minf)  #Enforce minimum factor rule
            workrow.append(newcoeff)
        randarray.append(tuple(workrow))  #Push the new row into the array

    rand = np.array(randarray)
    if sym:
        symprob = sum(rand[:,0])  #Get the sum of all probabilities in the existing set.
        if sym == 'x':
            symrow = (symprob,  -1.,   0.,    0.,  0.,   1.,    0.)
            symarr = np.array(symrow)
        if sym == 'y':
            symrow = (symprob,   1.,   0.,    0.,  0.,  -1.,    0.)
            symarr = np.array(symrow)
        if sym == 't':
            symrow  = (symprob, -0.5, -0.866, 0.,   0.866,   -0.5,   0.)
            symrow2 = (symprob, -0.5,  0.866, 0.,  -0.866,   -0.5,   0.)
            symarr = np.array([symrow,symrow2])
        if sym == 'q':
            symrow  = (symprob,  -1.,   0.,    0.,  0.,   1.,    0.)
            symrow2 = (symprob,   1.,   0.,    0.,  0.,  -1.,    0.)
            symarr = np.array([symrow,symrow2])
        rand = np.vstack((rand,symarr))  #Push the symmetry rows into the main list.

    return rand


