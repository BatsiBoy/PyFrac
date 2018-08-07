# -*- coding: utf-8 -*-
#Name: Fractal Variations
#Author: Sean Pope

#A small collection of common variation functions.
#When passed to the fractal engine, these take effect after the IFS algorithm.

""" Functions to make variations simpler to implement. """

import numpy as np

def r(x,y):
    return np.sqrt(np.square(x) + np.square(y))

def theta(x,y):
    return np.arctan(x/y)

def phi(x,y):
    return np.arctan(y/x)

def bound(x,y):
    return np.clip([x,y],-10,10)


""" Popular variation functions. """


def sin(x,y,*args):
    """ Constrains output to biunit square, favors arcs. """
    return np.sin(x),np.sin(y)



def spherical(x,y,*args):
    """ Rounds figures, produces many small spirals. """
    ri = r(x,y)
    rn = 1 / np.square(ri)
    return rn * x, rn * y


def swirl(x,y,*args):
    """ Pulls figures rotationally (counter-clockwise). """
    x,y = bound(x,y)
    ri = r(x,y)
    xn = (x * np.sin(np.square(ri))) - (y * np.cos(np.square(ri)))
    yn = (x * np.cos(np.square(ri))) + (y * np.sin(np.square(ri)))
    return xn, yn



def horseshoe(x,y,*args):
    """ Enlongates figures horizontally with elliptical figures. """
    ri = r(x,y)
    xn = (x-y)*(x+y)
    yn = 2 * x * y
    return xn / ri, yn / ri



def polar(x,y,*args):
    """ Forms vertical arcs, similar to arctan. """
    ri = r(x,y)
    thi = theta(x,y)
    return thi / np.pi, ri - 1



def handkerchief(x,y,*args):
    """ Creates diagonal diamond shapes about the origin. """
    ri = r(x,y)
    thi = theta(x,y)
    xn = np.sin(thi + ri)
    yn = np.cos(thi - ri)
    return xn, yn



def heart(x,y,*args):
    """ Cardiod heart shapes. """
    ri = r(x,y)
    thi = theta(x,y)
    xn = np.sin(thi * ri)
    yn = -1. * np.cos(thi * ri)
    return ri * xn, ri * yn



def disc(x,y,*args):
    """ Counter-clockwise rotation with internal peaking. """
    ri = r(x,y)
    thi = theta(x,y) / np.pi
    return thi * np.sin(np.pi * ri), thi * np.cos(np.pi * ri)



def spiral(x,y,*args):
    """ Chaotic clockwise pull toward the origin. """
    ri = r(x,y)
    thi = theta(x,y)
    xn = np.cos(thi) + np.sin(ri)
    yn = np.sin(thi) - np.cos(ri)
    return xn / ri, yn / ri



def hyperbolic(x,y,*args):
    """ Asymptotic curves about x and y. """
    ri = r(x,y)
    thi = theta(x,y)
    xn = np.sin(thi) / ri
    yn = ri * np.cos(thi)
    return xn, yn



def diamond(x,y,*args):
    """ Angled square forms about the axes. """
    ri = r(x,y)
    thi = theta(x,y)
    xn = np.sin(thi) * np.cos(ri)
    yn = np.cos(thi) * np.sin(ri)
    return xn, yn



def ex(x,y,*args):
    """ Strong diagonal pull with sheets about origin. """
    ri = r(x,y)
    thi = theta(x,y)
    p = np.sin(thi + ri)
    q = np.cos(thi - ri)
    xn = (p ** 3) + (q ** 3)
    yn = (p ** 3) - (q ** 3)
    return ri * xn, ri * yn



def julia(x,y,*args):
    """ Blooming fractal shapes with natural symmetries. """
    ris = np.sqrt(r(x,y))
    thi = theta(x,y)
    omega = np.random.randint(0,2)
    xn = np.cos(thi/2 + omega)
    yn = np.sin(thi/2 + omega)
    return ris * xn, ris * yn



def bent(x,y,*args):
    """ Smashes points into negative xy. """
    if x >= 0:
        if y >= 0:
            return x, y
        else:
            return x, y/2
    else:
        if y >= 0:
            return 2*x, y
        else:
            return 2*x, y/2
    return



def waves(x,y,a,b,c,d,e,f):
    """ Strong sinusoidal patterns at all angles. """
    if c:
        xn = b * np.sin(y/c**2)
    else:
        xn = 0
    if f:
        yn = e * np.sin(x/f**2)
    else:
        yn = 0
    return x + xn, y + yn



def fisheye(x,y,*args):
    """ Bulge figures out around the origin. """
    rif = 2 / (r(x,y) + 1)
    return rif * y, rif * x



def popcorn(x,y,a,b,c,d,e,f):
    """ Wavey jitters, like smeared paint. """
    xn = c * np.sin(np.tan(3 * y))
    yn = f * np.sin(np.tan(3 * x))
    return x + xn, y + yn



def exponential(x,y,*args):
    """ Expanding radial patterns. """
    expf = np.exp(x - 1)
    return expf * np.cos(np.pi * y), expf * np.sin(np.pi * y)



def power(x,y,*args):
    """ Forms elliptical gaps and arches. """
    thi = theta(x,y)
    rif = r(x,y) ** np.sin(thi)
    return rif * np.cos(thi), rif * np.sin(thi)



def cosine(x,y,*args):
    """  Bulging ellipse about the x axis. """
    xn = np.cos(np.pi * x) * np.cosh(y)
    yn = -1*np.sin(np.pi * x) * np.sinh(y)
    return xn, yn