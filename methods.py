"""This is the file which contains all of the functions and definitions
which I will be using in the main.py file."""

import math
import numpy as np
import numpy.ma as ma  # for masking, gets rid of invalid/null redshifts
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from files import fitsfile

from astropy.table import Table
from astropy import units as u

from astropy.cosmology import LambdaCDM  #for luminosity distance
cosmo = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7) #creates an instance of the LambdaCDM model

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

    def exclude_null_z(self, fitsfile): #removes any nan results from the Z_BEST, but leaves it the same length

        t = Table.read(fitsfile)
        z_arr = t['Z_BEST']
        masked_z_arr = ma.masked_array(z_arr, mask=[~(z>0.0) for z in z_arr])
        print(masked_z_arr)


"""A class that will contain all of the calculations and algebra"""

class Calculating(object):
    def __init__(self):
        null = "null"

    def calc_lum_dist(self, fitsfile):

        t = Table.read(fitsfile)
        z_arr = t['Z_BEST']
        masked_z_arr = ma.masked_array(z_arr, mask=[~(z > 0.0) for z in z_arr])

        #d_L = cosmo.luminosity_distance(z)
        #print(d_L)
        lum_dist_list = []  # will make a list of each D_L(z)
        for zj in masked_z_arr:  # for each redshift, find their luminosity distance
            lum_dist_list.append(cosmo.luminosity_distance(zj))  # each value of D_L for each corresponding z

        #return lum_dist_list

        t['D_L'] = 0.0
        t['D_L']=lum_dist_list
        print(t['D_L'])
        #t['Lum_Dist'] = lum_dist_list #enters the results into the FITS file as a new column

    def calc_Luminosity(self, fitsfile):

        t = Table.read(fitsfile)
        z = t['Z_BEST']
        #t['D_L'] =
        #self.calc_lum_dist(fitsfile) #will make a list of each D_L(z)

        Flux_144MHz = t['Total_flux'] #Total flux observed in the 144MHz radio band
        alpha = -0.7 #slope of the radio spectrum in Lum-freq log-log space

        """for row in t.rows:
        
            Lum_144MHz = row['Flux_144MHz'] * 4*math.pi * row[(d_L)]**2 *(1+z)**(1+alpha)
            Lum_1400MHz = Lum_144MHz * (0.102857)**alpha #the float is equal to 144/1400"""
# trying to do an equation in a single line, with the variables from matching rows  
        t['Lum_1400MHz'] = t['Total_flux'] * 4*math.pi * t['D_L']**2 *(1+t['Z_BEST'])**(1+alpha) # this is a list of luminosity values for each redshift Z_BEST
        print(t['Lum_1400MHz'])


"""Want a class that can plot graphs of Things vs. z, or against other Things"""

class Plotting(object):
    def __init__(self):
        null = "null"

    def plot_Luminosity(self, fitsfile):

        Lum_1400MHz = Calculating.calc_Luminosity(fitsfile)
        z = Reading.exclude_null_z(fitsfile)
        plt.plot(z, Lum_1400MHz)
        plt.title('Luminosity of Radio Sources increasing with redshift')
        plt.ylabel('Luminosity at 1.4GHz (units)')
        plt.xlabel('Redshift z')
        plt.semilogy()
        plt.show()
