#######################################################
# imports

import numpy as np
import matplotlib.pyplot as plt
import ngehtsim.obs.obs_generator as og
import ngehtsim.metrics as cm
import ehtim as eh
import ehtim.scattering as so
import os

#######################################################
# looped quantities

outdirs = ['./array_baseline_9m+128Gbps',
           './array_option1_13m+128Gbps',
           './array_option2_13m+64Gbps',
           './array_option3a_13m+128Gbps_noSPM',
           './array_option3b_13m+128Gbps_noLCO',
           './array_option3c_13m+128Gbps_noCNI',
           './array_option3d_13m+128Gbps_noJELM',
           './array_option4a_13m+64Gbps_noSPM',
           './array_option4b_13m+64Gbps_noLCO',
           './array_option4c_13m+64Gbps_noCNI',
           './array_option4d_13m+64Gbps_noJELM',
           './array_option5_13m+128Gbps_noLCO_withLLA']

sitess = [['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['CNI','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','OVRO','SMT','SPT'],
          ['BAJA','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','KP','LAS','OVRO','SMT','SPT'],
          ['CNI','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','OVRO','SMT','SPT'],
          ['BAJA','GLT','HAY','JCMT','JELM','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','KP','LAS','OVRO','SMT','SPT'],
          ['BAJA','CNI','GLT','HAY','JCMT','JELM','KP','LLA','OVRO','SMT','SPT']]

dish_diameters = [9.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0,
                  13.0]

bandwidths = [16.0,
              16.0,
              8.0,
              16.0,
              16.0,
              16.0,
              16.0,
              8.0,
              8.0,
              8.0,
              8.0,
              16.0]

#######################################################
# make source model for M87

F0 = 0.6
f0 = 0.9
f1 = 0.1
alpha = 15.0
alpha2 = 1.5

mod = eh.model.Model()
mod = mod.add_thick_mring(F0=f0*F0,
                          d=42.0*eh.RADPERUAS,
                          alpha=alpha*eh.RADPERUAS,
                          beta_list=[-0.4])
mod = mod.add_thick_mring(F0=f1*F0,
                          d=42.0*eh.RADPERUAS,
                          alpha=alpha2*eh.RADPERUAS,
                          beta_list=[-0.4])

# save as image
im = mod.make_image(500.0*eh.RADPERUAS,npix=512)
im.save_fits('./M87.fits')

#######################################################
# make source model for Sgr A*

F0 = 2.5
f0 = 0.9
d = 52.0
alpha = 20.0
b1a = 0.15
b2a = 0.06
b3a = 0.25
b4a = 0.13
b1p = 0.0
b2p = -2.3
b3p = 0.5
b4p = -1.4

alpha1 = 2.0
f1 = 0.1

beta1 = b1a*np.exp((1j)*(b1p*np.pi))
beta2 = b2a*np.exp((1j)*(b2p*np.pi))
beta3 = b3a*np.exp((1j)*(b3p*np.pi))
beta4 = b4a*np.exp((1j)*(b4p*np.pi))
stretch = 1.2
stretch_PA = (np.pi/2.0) - 0.2

mod = eh.model.Model()
mod = mod.add_stretched_thick_mring(F0=f0*F0,
                                    d=d*eh.RADPERUAS,
                                    alpha=alpha*eh.RADPERUAS,
                                    x0=0.0,
                                    y0=0.0,
                                    beta_list=[beta1,beta2,beta3,beta4],
                                    stretch=stretch,
                                    stretch_PA=stretch_PA)
mod = mod.add_stretched_thick_mring(F0=f1*F0,
                                    d=d*eh.RADPERUAS,
                                    alpha=alpha1*eh.RADPERUAS,
                                    x0=0.0,
                                    y0=0.0,
                                    beta_list=[beta1,beta2,beta3,beta4],
                                    stretch=1.0,
                                    stretch_PA=stretch_PA)


# save as image
im = mod.make_image(1000.0*eh.RADPERUAS,npix=1024)
im.RA = 17.761122
im.DEC = -29.00781
im.source = 'SgrA'

im.rf = 86.0e9
im_scatt = sm.Scatter(im)
im_scatt.save_fits('SgrA_86GHz.fits')

im.rf = 230.0e9
im_scatt = sm.Scatter(im)
im_scatt.save_fits('SgrA_230GHz.fits')

im.rf = 345.0e9
im_scatt = sm.Scatter(im)
im_scatt.save_fits('SgrA_345GHz.fits')

#######################################################
# primary settings

Nweather = 100
SNR_cut = 3.0

freqs = [86.0, 230.0, 345.0]
input_models_M87 = ['./M87.fits', './M87.fits', './M87.fits']
input_models_SgrA = ['./SgrA_86GHz.fits', './SgrA_230GHz.fits', './SgrA_345GHz.fits']

receiver_configuration_overrides = {'ALMA': ['Band7'],
                                    'APEX': ['Band7'],
                                    'BAJA': ['Band3', 'Band6', 'Band7'],
                                    'CNI': ['Band3', 'Band6', 'Band7'],
                                    'GLT': ['Band3', 'Band6', 'Band7'],
                                    'HAY': ['Band3', 'Band6'],
                                    'IRAM': ['Band7'],
                                    'JCMT': ['Band3', 'Band6', 'Band7'],
                                    'JELM': ['Band3', 'Band6', 'Band7'],
                                    'KP': ['Band3', 'Band6'],
                                    'LAS': ['Band3', 'Band6', 'Band7'],
                                    'LMT': ['Band3', 'Band6', 'Band7'],
                                    'NOEMA': ['Band7'],
                                    'OVRO': ['Band3', 'Band6'],
                                    'SMA': ['Band7'],
                                    'SMT': ['Band3', 'Band6', 'Band7'],
                                    'SPT': ['Band3', 'Band6', 'Band7']}

# overrides
T_R_overrides = {'ALMA': {'Band7': 75.0},
                 'APEX': {'Band7': 75.0},
                 'GLT': {'Band7': 75.0},
                 'IRAM': {'Band7': 85.0},
                 'JCMT': {'Band7': 105.0},
                 'LMT': {'Band7': 75.0},
                 'NOEMA': {'Band7': 85.0},
                 'SMA': {'Band7': 130.0},
                 'SMT': {'Band7': 150.0}}

bandwidth_overrides = {'ALMA': {'Band7': 4.0},
                       'APEX': {'Band7': 4.0},
                       'IRAM': {'Band7': 4.0},
                       'NOEMA': {'Band7': 4.0},
                       'SMA': {'Band7': 4.0}}

# specify the DSB stations
sideband_ratio_overrides = {'SMA': {'Band7': 1.0},
                            'SMT': {'Band7': 1.0}}

#######################################################
# run multiple weather instantiations

for idir in range(len(outdirs)):

    # grab current parameters
    outdir = outdirs[idir]
    sites = sitess[idir]
    dish_diameter = dish_diameters[idir]
    bandwidth = bandwidths[idir]

    # make output directory
    os.makedirs(outdir,exist_ok=True)
    os.makedirs(outdir+'/uvfits_M87',exist_ok=True)
    os.makedirs(outdir+'/uvfits_SgrA',exist_ok=True)

    #######################################################
    # M87 simulations

    # update settings and overrides
    settings = {'model_file': input_models_M87[-1],
                'sites': sites,
                'source': 'M87',
                'frequency': freqs[-1],
                'bandwidth': bandwidth,
                'month': 'Apr',
                'day': 15,
                'year': 2021,
                't_start': 0.0,
                'dt': 24.0,
                't_int': 300.0,
                't_rest': 600.0,
                'D_new': dish_diameter,
                'fringe_finder': ['fringegroups', [5., 5.]],
                'weather': 'random'}

    D_overrides = {'BAJA': dish_diameter,
                   'CNI': dish_diameter,
                   'JELM': dish_diameter,
                   'LAS': dish_diameter}

    # run multiple weather instantiations
    obslist_M87 = list()
    fflist = list()
    for i in range(Nweather):
        print(i)

        settings.update({'random_seed': 101 + i})
        obsgen = og.obs_generator(settings,
                              D_overrides=D_overrides,
                              receiver_configuration_overrides=receiver_configuration_overrides,
                              T_R_overrides=T_R_overrides,
                              bandwidth_overrides=bandwidth_overrides,
                              sideband_ratio_overrides=sideband_ratio_overrides)
        obslist_here = obsgen.make_obs_mf(freqs,input_models_M87,addnoise=False,addgains=False)

        if (SNR_cut > 0.0):
            obslist_here[0] = obslist_here[0].flag_low_snr(snr_cut=SNR_cut).copy()
            obslist_here[1] = obslist_here[1].flag_low_snr(snr_cut=SNR_cut).copy()
            obslist_here[2] = obslist_here[2].flag_low_snr(snr_cut=SNR_cut).copy()

        obslist_M87.append(obslist_here)

        ff86 = cm.calc_ff(obslist_here[0],fov=100.0,longest_BL=14.66e9)
        ff230 = cm.calc_ff(obslist_here[1],fov=100.0,longest_BL=14.66e9)
        ff345 = cm.calc_ff(obslist_here[2],fov=100.0,longest_BL=14.66e9)
        fflist.append([ff86,ff230,ff345])

        # save uvfits
        obslist_M87[i][0].save_uvfits(outdir+'/uvfits_M87/obs_86GHz_'+str(i).zfill(4)+'.uvfits')
        obslist_M87[i][1].save_uvfits(outdir+'/uvfits_M87/obs_230GHz_'+str(i).zfill(4)+'.uvfits')
        obslist_M87[i][2].save_uvfits(outdir+'/uvfits_M87/obs_345GHz_'+str(i).zfill(4)+'.uvfits')

    # no noise obs
    settings.update({'frequency': 86.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_86 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_86 = obsgen_nonoise_86.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_86 = obs_nonoise_86.data['u'] / (1.0e9)
    v_nonoise_86 = obs_nonoise_86.data['v'] / (1.0e9)

    settings.update({'frequency': 230.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_230 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_230 = obsgen_nonoise_230.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_230 = obs_nonoise_230.data['u'] / (1.0e9)
    v_nonoise_230 = obs_nonoise_230.data['v'] / (1.0e9)

    settings.update({'frequency': 345.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_345 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_345 = obsgen_nonoise_345.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_345 = obs_nonoise_345.data['u'] / (1.0e9)
    v_nonoise_345 = obs_nonoise_345.data['v'] / (1.0e9)

    #################
    # plot

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    weight_86 = np.zeros_like(u_nonoise_86)
    for j in range(Nweather):
        obshere_86 = obslist_M87[j][0].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_86)):
            if (u_nonoise_86[i] in (obshere_86.data['u'] / (1.0e9))):
                weight_86[i] += 1.0
        obshere_86 = obslist_M87[j][0].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_86)):
            if (u_nonoise_86[i] in (obshere_86.data['u'] / (1.0e9))):
                weight_86[i] += 1.0
    weight_86 /= Nweather

    weight_230 = np.zeros_like(u_nonoise_230)
    for j in range(Nweather):
        obshere_230 = obslist_M87[j][1].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_230)):
            if (u_nonoise_230[i] in (obshere_230.data['u'] / (1.0e9))):
                weight_230[i] += 1.0
        obshere_230 = obslist_M87[j][1].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_230)):
            if (u_nonoise_230[i] in (obshere_230.data['u'] / (1.0e9))):
                weight_230[i] += 1.0
    weight_230 /= Nweather

    weight_345 = np.zeros_like(u_nonoise_345)
    for j in range(Nweather):
        obshere_345 = obslist_M87[j][2].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_345)):
            if (u_nonoise_345[i] in (obshere_345.data['u'] / (1.0e9))):
                weight_345[i] += 1.0
        obshere_345 = obslist_M87[j][2].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_345)):
            if (u_nonoise_345[i] in (obshere_345.data['u'] / (1.0e9))):
                weight_345[i] += 1.0
    weight_345 /= Nweather

    for i in range(len(u_nonoise_345)):
        ax.plot([u_nonoise_345[i]],[v_nonoise_345[i]],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,alpha=weight_345[i])
        ax.plot([-u_nonoise_345[i]],[-v_nonoise_345[i]],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,alpha=weight_345[i])
    for i in range(len(u_nonoise_230)):
        ax.plot([u_nonoise_230[i]],[v_nonoise_230[i]],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,alpha=weight_230[i])
        ax.plot([-u_nonoise_230[i]],[-v_nonoise_230[i]],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,alpha=weight_230[i])
    for i in range(len(u_nonoise_86)):
        ax.plot([u_nonoise_86[i]],[v_nonoise_86[i]],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,alpha=weight_86[i])
        ax.plot([-u_nonoise_86[i]],[-v_nonoise_86[i]],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,alpha=weight_86[i])

    # dummy legend point
    ax.plot([-99],[-99],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,label='345 GHz')
    ax.plot([-99],[-99],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,label='230 GHz')
    ax.plot([-99],[-99],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,label='86 GHz')
    ax.legend(loc='lower left',fontsize=8)

    ax.set_xlim(15,-15)
    ax.set_ylim(-15,15)

    ax.set_xlabel(r'$u$ (G$\lambda$)')
    ax.set_ylabel(r'$v$ (G$\lambda$)')

    ax.grid(linewidth=0.5,color='gray',alpha=0.2,linestyle='--')

    plt.savefig(outdir+'/coverage_M87.png',dpi=300,bbox_inches='tight')
    plt.close()

    #################
    # fill fraction

    ffmeans = np.mean(np.array(fflist),axis=0)
    ffstds = np.std(np.array(fflist),axis=0)

    ff_86 = ffmeans[0]
    ff_230 = ffmeans[1]
    ff_345 = ffmeans[2]

    print('-'*40)
    print('M87 FF at 86 GHz: '+str(ff_86)+' +/- '+str(ffstds[0]))
    print('M87 FF at 230 GHz: '+str(ff_230)+' +/- '+str(ffstds[1]))
    print('M87 FF at 345 GHz: '+str(ff_345)+' +/- '+str(ffstds[2]))
    print('-'*40)

    #######################################################
    # Sgr A* simulations

    # update settings and overrides
    settings = {'model_file': input_models_SgrA[-1],
                'sites': sites,
                'source': 'SgrA',
                'frequency': freqs[-1],
                'bandwidth': bandwidth,
                'month': 'Apr',
                'day': 15,
                'year': 2021,
                't_start': 0.0,
                'dt': 24.0,
                't_int': 300.0,
                't_rest': 600.0,
                'D_new': dish_diameter,
                'fringe_finder': ['fringegroups', [5., 5.]],
                'weather': 'random'}

    D_overrides = {'BAJA': dish_diameter,
                   'CNI': dish_diameter,
                   'JELM': dish_diameter,
                   'LAS': dish_diameter}

    # run multiple weather instantiations
    obslist_M87 = list()
    fflist = list()
    for i in range(Nweather):
        print(i)

        settings.update({'random_seed': 101 + i})
        obsgen = og.obs_generator(settings,
                              D_overrides=D_overrides,
                              receiver_configuration_overrides=receiver_configuration_overrides,
                              T_R_overrides=T_R_overrides,
                              bandwidth_overrides=bandwidth_overrides,
                              sideband_ratio_overrides=sideband_ratio_overrides)
        obslist_here = obsgen.make_obs_mf(freqs,input_models_SgrA,addnoise=False,addgains=False)

        if (SNR_cut > 0.0):
            obslist_here[0] = obslist_here[0].flag_low_snr(snr_cut=SNR_cut).copy()
            obslist_here[1] = obslist_here[1].flag_low_snr(snr_cut=SNR_cut).copy()
            obslist_here[2] = obslist_here[2].flag_low_snr(snr_cut=SNR_cut).copy()

        obslist_M87.append(obslist_here)

        ff86 = cm.calc_ff(obslist_here[0],fov=100.0,longest_BL=14.66e9)
        ff230 = cm.calc_ff(obslist_here[1],fov=100.0,longest_BL=14.66e9)
        ff345 = cm.calc_ff(obslist_here[2],fov=100.0,longest_BL=14.66e9)
        fflist.append([ff86,ff230,ff345])

        # save uvfits
        obslist_M87[i][0].save_uvfits(outdir+'/uvfits_M87/obs_86GHz_'+str(i).zfill(4)+'.uvfits')
        obslist_M87[i][1].save_uvfits(outdir+'/uvfits_M87/obs_230GHz_'+str(i).zfill(4)+'.uvfits')
        obslist_M87[i][2].save_uvfits(outdir+'/uvfits_M87/obs_345GHz_'+str(i).zfill(4)+'.uvfits')

    # no noise obs
    settings.update({'frequency': 86.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_86 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_86 = obsgen_nonoise_86.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_86 = obs_nonoise_86.data['u'] / (1.0e9)
    v_nonoise_86 = obs_nonoise_86.data['v'] / (1.0e9)

    settings.update({'frequency': 230.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_230 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_230 = obsgen_nonoise_230.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_230 = obs_nonoise_230.data['u'] / (1.0e9)
    v_nonoise_230 = obs_nonoise_230.data['v'] / (1.0e9)

    settings.update({'frequency': 345.0,
                     'fringe_finder': ['naive', 0.0]})
    obsgen_nonoise_345 = og.obs_generator(settings,
                                      D_overrides=D_overrides,
                                      receiver_configuration_overrides=receiver_configuration_overrides,
                                      T_R_overrides=T_R_overrides,
                                      bandwidth_overrides=bandwidth_overrides,
                                      sideband_ratio_overrides=sideband_ratio_overrides)
    obs_nonoise_345 = obsgen_nonoise_345.make_obs(addnoise=False,addgains=False,flagwind=False)
    u_nonoise_345 = obs_nonoise_345.data['u'] / (1.0e9)
    v_nonoise_345 = obs_nonoise_345.data['v'] / (1.0e9)

    #################
    # plot

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    weight_86 = np.zeros_like(u_nonoise_86)
    for j in range(Nweather):
        obshere_86 = obslist_M87[j][0].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_86)):
            if (u_nonoise_86[i] in (obshere_86.data['u'] / (1.0e9))):
                weight_86[i] += 1.0
        obshere_86 = obslist_M87[j][0].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_86)):
            if (u_nonoise_86[i] in (obshere_86.data['u'] / (1.0e9))):
                weight_86[i] += 1.0
    weight_86 /= Nweather

    weight_230 = np.zeros_like(u_nonoise_230)
    for j in range(Nweather):
        obshere_230 = obslist_M87[j][1].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_230)):
            if (u_nonoise_230[i] in (obshere_230.data['u'] / (1.0e9))):
                weight_230[i] += 1.0
        obshere_230 = obslist_M87[j][1].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_230)):
            if (u_nonoise_230[i] in (obshere_230.data['u'] / (1.0e9))):
                weight_230[i] += 1.0
    weight_230 /= Nweather

    weight_345 = np.zeros_like(u_nonoise_345)
    for j in range(Nweather):
        obshere_345 = obslist_M87[j][2].flag_sites(['SMA','APEX'])
        for i in range(len(u_nonoise_345)):
            if (u_nonoise_345[i] in (obshere_345.data['u'] / (1.0e9))):
                weight_345[i] += 1.0
        obshere_345 = obslist_M87[j][2].flag_sites(['BAJA','CNI','GLT','HAY','IRAM','JCMT','JELM','KP','LAS','LLA','LMT','NOEMA','OVRO','SMA','SMT','SPT'])
        for i in range(len(u_nonoise_345)):
            if (u_nonoise_345[i] in (obshere_345.data['u'] / (1.0e9))):
                weight_345[i] += 1.0
    weight_345 /= Nweather

    for i in range(len(u_nonoise_345)):
        ax.plot([u_nonoise_345[i]],[v_nonoise_345[i]],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,alpha=weight_345[i])
        ax.plot([-u_nonoise_345[i]],[-v_nonoise_345[i]],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,alpha=weight_345[i])
    for i in range(len(u_nonoise_230)):
        ax.plot([u_nonoise_230[i]],[v_nonoise_230[i]],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,alpha=weight_230[i])
        ax.plot([-u_nonoise_230[i]],[-v_nonoise_230[i]],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,alpha=weight_230[i])
    for i in range(len(u_nonoise_86)):
        ax.plot([u_nonoise_86[i]],[v_nonoise_86[i]],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,alpha=weight_86[i])
        ax.plot([-u_nonoise_86[i]],[-v_nonoise_86[i]],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,alpha=weight_86[i])

    # dummy legend point
    ax.plot([-99],[-99],marker='o',linewidth=0,color='green',markeredgewidth=0,markersize=2,label='345 GHz')
    ax.plot([-99],[-99],marker='o',linewidth=0,color='orange',markeredgewidth=0,markersize=2,label='230 GHz')
    ax.plot([-99],[-99],marker='o',linewidth=0,color='purple',markeredgewidth=0,markersize=2,label='86 GHz')
    ax.legend(loc='lower left',fontsize=8)

    ax.set_xlim(15,-15)
    ax.set_ylim(-15,15)

    ax.set_xlabel(r'$u$ (G$\lambda$)')
    ax.set_ylabel(r'$v$ (G$\lambda$)')

    ax.grid(linewidth=0.5,color='gray',alpha=0.2,linestyle='--')

    plt.savefig(outdir+'/coverage_M87.png',dpi=300,bbox_inches='tight')
    plt.close()

    #################
    # fill fraction

    ffmeans = np.mean(np.array(fflist),axis=0)
    ffstds = np.std(np.array(fflist),axis=0)

    ff_86 = ffmeans[0]
    ff_230 = ffmeans[1]
    ff_345 = ffmeans[2]

    print('-'*40)
    print('Sgr A* FF at 86 GHz: '+str(ff_86)+' +/- '+str(ffstds[0]))
    print('Sgr A* FF at 230 GHz: '+str(ff_230)+' +/- '+str(ffstds[1]))
    print('Sgr A* FF at 345 GHz: '+str(ff_345)+' +/- '+str(ffstds[2]))
    print('-'*40)

