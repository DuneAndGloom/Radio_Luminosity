"""This is the file which contains all of the functions and definitions
which I will be using in the main.py file."""

import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from files import fitsfile

from astropy.table import Table
from astropy.cosmology import WMAP9 as cosmo #for luminosity distance

"""A class that will house functions that read out various columns from the FITS file"""

class Reading(object):
    def __init__(self):
        null = 'null'

    def read_headers(self, fitsfile):

        t = Table.read(fitsfile)
        print(t[0])

    def read_RA_and_Dec(self, fitsfile):

        t = Table.read(fitsfile)
        print(t['RA','DEC'])

    def read_z(self, fitsfile):

        t = Table.read(fitsfile)
        print(t['Z_BEST'])


"""A class that will contain all of the calculations and algebra"""

class Calculating(object):
    def __init__(self):
        null = "null"

    def calc_lum_dist(self, fitsfile):

        t = Table.read(fitsfile)
        z = t['Z_BEST']
        d_L = cosmo.luminosity_distance(z)
        print(d_L)

    def calc_Luminosity(self, fitsfile):

        t = Table.read(fitsfile)
        z = t['Z_BEST']
        d_L = cosmo.luminosity_distance(z)
        Flux_144MHz = t['Total_flux'] #Total flux observed in the 144MHz radio band
        alpha = -0.7 #slope of the radio spectrum in Lum-freq log-log space

        Lum_144MHz = Flux_144MHz * 4*math.pi * (d_L)**2 *(1+z)**(1+alpha)
        Lum_1400MHz = Lum_144MHz * (0.102857)**alpha #the float is equal to 144/1400

        return Lum_1400MHz

"""Want a class that can plot graphs of Things vs. z"""

class Plotting(object):
    def __init__(self):
        null = "null"

    def plot_Luminosity(self, z, fitsfile):

        Lum_1400MHz = Calculating.calc_Luminosity(fitsfile)
        z = np.linspace(0.01,7.01,100)
        plt.plot(z, Lum_1400MHz)
        plt.title('Luminosity of Radio Sources increasing with redshift')
        plt.ylabel('Luminosity at 1.4GHz (units)')
        plt.xlabel('Redshift z')
        plt.semilogy()
        plt.show()
