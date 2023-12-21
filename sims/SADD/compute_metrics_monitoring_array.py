import numpy as np
import ehtim as eh
import ngehtsim.metrics as cm
import glob

######################################
# 86 GHz performance

filelist = np.sort(glob.glob('./uvfits_individual_bands_monitoring/*86*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
med_bl_sensitivity = list()
bl_sensitivity = list()
long_bl_sensitivity = list()
minimum_RMS = list()
print('Computing 86GHz performance...')
for filehere in filelist[0:30]:
    with eh.parloop.HiddenPrints():
        obs = eh.obsdata.load_uvfits(filehere)
        
        # flag intrasite baselines
        obs = obs.flag_uvdist(uv_min=5.0e6)

    PSS_here = cm.calc_pss(obs)
    PSS.append(PSS_here)

    u = obs.data['u']
    v = obs.data['v']
    rho = np.sqrt(u**2.0 + v**2.0)
    min_bl.append(np.min(rho))
    max_bl.append(np.max(rho))

    med_bl_sensitivity.append(np.median(obs.data['sigma']))
    bl_sensitivity.append(obs.data['sigma'])

    # mean sensitivity of the best 10 baselines on the longest 30% of baselines
    ind = (rho >= (0.7*np.max(rho)))
    sigmas = obs.data['sigma'][ind]
    long_bl_sensitivity.append(np.mean((np.sort(sigmas))[:10]))

    # defined "minimum RMS noise"
    sigmas = obs.data['sigma']
    minimum_RMS.append(np.min(sigmas))

PSS_86 = np.array(PSS)
min_bl_86 = np.array(min_bl)
max_bl_86 = np.array(max_bl)
med_bl_sensitivity_86 = np.array(med_bl_sensitivity)
bl_sensitivity_86 = np.array(bl_sensitivity)
long_bl_sensitivity_86 = np.array(long_bl_sensitivity)
minimum_RMS_86 = np.array(minimum_RMS)

######################################
# 230 GHz performance

filelist = np.sort(glob.glob('./uvfits_individual_bands_monitoring/*230*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
med_bl_sensitivity = list()
bl_sensitivity = list()
long_bl_sensitivity = list()
minimum_RMS = list()
print('Computing 230GHz performance...')
for filehere in filelist[0:30]:
    with eh.parloop.HiddenPrints():
        obs = eh.obsdata.load_uvfits(filehere)
        
        # flag intrasite baselines
        obs = obs.flag_uvdist(uv_min=5.0e6)

    PSS_here = cm.calc_pss(obs)
    PSS.append(PSS_here)

    u = obs.data['u']
    v = obs.data['v']
    rho = np.sqrt(u**2.0 + v**2.0)
    min_bl.append(np.min(rho))
    max_bl.append(np.max(rho))

    med_bl_sensitivity.append(np.median(obs.data['sigma']))
    bl_sensitivity.append(obs.data['sigma'])

    # mean sensitivity of the best 10 baselines on the longest 10% of baselines
    ind = (rho >= (0.7*np.max(rho)))
    sigmas = obs.data['sigma'][ind]
    long_bl_sensitivity.append(np.mean((np.sort(sigmas))[:10]))

    # defined "minimum RMS noise"
    sigmas = obs.data['sigma']
    minimum_RMS.append(np.min(sigmas))

PSS_230 = np.array(PSS)
min_bl_230 = np.array(min_bl)
max_bl_230 = np.array(max_bl)
med_bl_sensitivity_230 = np.array(med_bl_sensitivity)
bl_sensitivity_230 = np.array(bl_sensitivity)
long_bl_sensitivity_230 = np.array(long_bl_sensitivity)
minimum_RMS_230 = np.array(minimum_RMS)

######################################
# 345 GHz performance

filelist = np.sort(glob.glob('./uvfits_individual_bands_monitoring/*345*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
med_bl_sensitivity = list()
bl_sensitivity = list()
long_bl_sensitivity = list()
minimum_RMS = list()
print('Computing 345GHz performance...')
for filehere in filelist[0:30]:
    with eh.parloop.HiddenPrints():
        obs = eh.obsdata.load_uvfits(filehere)
        
        # flag intrasite baselines
        obs = obs.flag_uvdist(uv_min=5.0e6)

    PSS_here = cm.calc_pss(obs)
    PSS.append(PSS_here)

    u = obs.data['u']
    v = obs.data['v']
    rho = np.sqrt(u**2.0 + v**2.0)
    min_bl.append(np.min(rho))
    max_bl.append(np.max(rho))

    med_bl_sensitivity.append(np.median(obs.data['sigma']))
    bl_sensitivity.append(obs.data['sigma'])

    # mean sensitivity of the best 10 baselines on the longest 10% of baselines
    ind = (rho >= (0.7*np.max(rho)))
    sigmas = obs.data['sigma'][ind]
    long_bl_sensitivity.append(np.mean((np.sort(sigmas))[:10]))

    # defined "minimum RMS noise"
    sigmas = obs.data['sigma']
    minimum_RMS.append(np.min(sigmas))

PSS_345 = np.array(PSS)
min_bl_345 = np.array(min_bl)
max_bl_345 = np.array(max_bl)
med_bl_sensitivity_345 = np.array(med_bl_sensitivity)
bl_sensitivity_345 = np.array(bl_sensitivity)
long_bl_sensitivity_345 = np.array(long_bl_sensitivity)
minimum_RMS_345 = np.array(minimum_RMS)

######################################
# report results

print('-----------------------------------')
print('For 86 GHz obs:')
print('PSS: '+str(np.mean(PSS_86)) + ' Jy')
print('FOV: '+str((1.0/np.mean(min_bl_86))/eh.RADPERUAS) + ' uas')
print('Resolution: '+str((1.0/np.mean(max_bl_86))/eh.RADPERUAS) + ' uas')
print('Median baseline sensitivity: '+str(np.mean(med_bl_sensitivity_86))+' Jy')
print('Long baseline sensitivity: '+str(np.median(long_bl_sensitivity_86))+' Jy')
print('Minimum baseline RMS: '+str(np.median(minimum_RMS_86))+' Jy')
print('-----------------------------------')

print('-----------------------------------')
print('For 230 GHz obs:')
print('PSS: '+str(np.mean(PSS_230)) + ' Jy')
print('FOV: '+str((1.0/np.mean(min_bl_230))/eh.RADPERUAS) + ' uas')
print('Resolution: '+str((1.0/np.mean(max_bl_230))/eh.RADPERUAS) + ' uas')
print('Median baseline sensitivity: '+str(np.mean(med_bl_sensitivity_230))+' Jy')
print('Long baseline sensitivity: '+str(np.median(long_bl_sensitivity_230))+' Jy')
print('Minimum baseline RMS: '+str(np.median(minimum_RMS_230))+' Jy')
print('-----------------------------------')

print('-----------------------------------')
print('For 345 GHz obs:')
print('PSS: '+str(np.mean(PSS_345)) + ' Jy')
print('FOV: '+str((1.0/np.mean(min_bl_345))/eh.RADPERUAS) + ' uas')
print('Resolution: '+str((1.0/np.mean(max_bl_345))/eh.RADPERUAS) + ' uas')
print('Median baseline sensitivity: '+str(np.mean(med_bl_sensitivity_345))+' Jy')
print('Long baseline sensitivity: '+str(np.median(long_bl_sensitivity_345))+' Jy')
print('Minimum baseline RMS: '+str(np.median(minimum_RMS_345))+' Jy')
print('-----------------------------------')

