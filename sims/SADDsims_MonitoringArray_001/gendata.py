import numpy as np
import ehtim as eh
import ngehtsim.obs.obs_generator as og
import glob
from astropy.time import Time
import os

#######################################################
# inputs

# specify the frequencies at which to observe
freqs = [86.0, 230.0, 345.0]

# the sites participating in monitoring array observations
sites = ['BAJA','CNI','GLT','HAY','JCMT','JELM','LAS','OVRO','SMT']

# some sites only have access to certain observing bands
receiver_configuration_overrides = {'ALMA': ['Band7'],
                                    'APEX': ['Band7'],
                                    'BAJA': ['Band3', 'Band6', 'Band7'],
                                    'CNI': ['Band3', 'Band6', 'Band7'],
                                    'GAM': ['Band3', 'Band6'],
                                    'GLT': ['Band3', 'Band6', 'Band7'],
                                    'HAY': ['Band3', 'Band6'],
                                    'IRAM': ['Band3', 'Band6'],
                                    'JCMT': ['Band3', 'Band6', 'Band7'],
                                    'JELM': ['Band3', 'Band6', 'Band7'],
                                    'KP': ['Band3', 'Band6'],
                                    'KVNPC': ['Band3', 'Band6'],
                                    'KVNYS': ['Band3', 'Band6'],
                                    'LAS': ['Band3', 'Band6', 'Band7'],
                                    'LLA': ['Band3', 'Band6', 'Band7'],
                                    'LMT': ['Band3', 'Band6', 'Band7'],
                                    'NOEMA': ['Band3', 'Band6'],
                                    'OVRO': ['Band3', 'Band6'],
                                    'SMA': ['Band7'],
                                    'SMT': ['Band3', 'Band6', 'Band7'],
                                    'SPT': ['Band3', 'Band6', 'Band7']}

# specify the diameters for the new dishes
D_overrides = {'BAJA': 9.0,
               'CNI': 9.0,
               'JELM': 9.0,
               'LAS': 9.0}

# some sites record different bandwidths
bandwidth_overrides = {'ALMA': {'Band7': 8.0},
                       'APEX': {'Band7': 8.0},
                       'IRAM': {'Band3': 4.0, 'Band6': 4.0},
                       'NOEMA': {'Band3': 4.0, 'Band6': 4.0}}

# general settings
settings = {'sites': sites,
            'source': 'M87',
            'bandwidth': 16.0,
            'day': 15,
            'month': 'Apr',
            'year': 2025,
            't_start': 0.0,
            'dt': 24.0,
            't_int': 600.0,
            't_rest': 1200.0,
            'weather': 'random'}

#######################################################
# make source model for M87

F0 = 0.6
f0 = 0.9
f1 = 0.1
alpha = 15.0
alpha2 = 1.5

mod = eh.model.Model()
mod = mod.add_thick_mring(F0 = f0*F0,
                          d = 42.0*eh.RADPERUAS,
                          alpha = alpha*eh.RADPERUAS,
                          beta_list=[-0.4])
mod = mod.add_thick_mring(F0 = f1*F0,
                          d = 42.0*eh.RADPERUAS,
                          alpha = alpha2*eh.RADPERUAS,
                          beta_list=[-0.4])

#######################################################
# loop through some weather instantiations

t0 = 58485.0
monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

Nweather = 30

# make directory for storing data files
os.makedirs('./uvfits',exist_ok=True)

for iweather in range(Nweather):

    there = Time(t0 + (3*iweather),format='mjd')
    year = str(there.to_value('datetime').year)
    month = monthlist[there.to_value('datetime').month-1]
    day = str(there.to_value('datetime').day)
    print(there.to_value('datetime'))

    settings.update({'day': day,
                     'month': month,
                     'year': year,
                     'random_seed': 101 + iweather,
                     'weather': 'exact'})

    # specify the model files, assuming monochromatic
    input_models = [mod,mod,mod]

    # initialize the observation generator
    obsgen = og.obs_generator(settings,
                              receiver_configuration_overrides=receiver_configuration_overrides,
                              D_overrides=D_overrides,
                              bandwidth_overrides=bandwidth_overrides)

    # generate the list of observations at each frequency
    obslist = obsgen.make_obs_mf(freqs,input_models)

    # save individual frequency bands
    for iobs, obs in enumerate(obslist):
        obs.save_uvfits('./uvfits/datafile_'+str(iweather).zfill(4)+'_'+str(int(freqs[iobs]))+'GHz'+'.uvfits')
