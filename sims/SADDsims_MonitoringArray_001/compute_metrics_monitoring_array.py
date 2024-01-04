import numpy as np
import ehtim as eh
import ngehtsim.metrics as cm
import glob

######################################
# 86 GHz performance

filelist = np.sort(glob.glob('./uvfits/*86*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
min_bl_rms_noise = list()
print('Computing 86GHz performance...')
for filehere in filelist:
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

    min_bl_rms_noise = np.min(obs.data['sigma'])

PSS_86 = np.array(PSS)
min_bl_86 = np.array(min_bl)
max_bl_86 = np.array(max_bl)
min_bl_rms_noise_86 = np.array(min_bl_rms_noise)

######################################
# 230 GHz performance

filelist = np.sort(glob.glob('./uvfits/*230*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
min_bl_rms_noise = list()
print('Computing 230GHz performance...')
for filehere in filelist:
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

    min_bl_rms_noise = np.min(obs.data['sigma'])

PSS_230 = np.array(PSS)
min_bl_230 = np.array(min_bl)
max_bl_230 = np.array(max_bl)
min_bl_rms_noise_230 = np.array(min_bl_rms_noise)

######################################
# 345 GHz performance

filelist = np.sort(glob.glob('./uvfits/*345*.uvfits'))

PSS = list()
min_bl = list()
max_bl = list()
min_bl_rms_noise = list()
print('Computing 345GHz performance...')
for filehere in filelist:
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
    
    min_bl_rms_noise = np.min(obs.data['sigma'])

PSS_345 = np.array(PSS)
min_bl_345 = np.array(min_bl)
max_bl_345 = np.array(max_bl)
min_bl_rms_noise_345 = np.array(min_bl_rms_noise)

######################################
# report results

print('-'*100)
print('For 86 GHz obs:')
print('Minimum baseline RMS noise: ' + str(min_bl_rms_noise_86) + ' Jy')
print('Point source sensitivity: '+str(np.mean(PSS_86)) + ' Jy')
print('Inverse shortest projected non-intrasite baseline: '+str((1.0/np.mean(min_bl_86))/eh.RADPERUAS) + ' uas')
print('Inverse longest projected baseline: '+str((1.0/np.mean(max_bl_86))/eh.RADPERUAS) + ' uas')
print('-'*100)

print('-'*100)
print('For 230 GHz obs:')
print('Minimum baseline RMS noise: ' + str(min_bl_rms_noise_230) + ' Jy')
print('Point source sensitivity: '+str(np.mean(PSS_230)) + ' Jy')
print('Inverse shortest projected non-intrasite baseline: '+str((1.0/np.mean(min_bl_230))/eh.RADPERUAS) + ' uas')
print('Inverse longest projected baseline: '+str((1.0/np.mean(max_bl_230))/eh.RADPERUAS) + ' uas')
print('-'*100)

print('-'*100)
print('For 345 GHz obs:')
print('Minimum baseline RMS noise: ' + str(min_bl_rms_noise_345) + ' Jy')
print('Point source sensitivity: '+str(np.mean(PSS_345)) + ' Jy')
print('Inverse shortest projected non-intrasite baseline: '+str((1.0/np.mean(min_bl_345))/eh.RADPERUAS) + ' uas')
print('Inverse longest projected baseline: '+str((1.0/np.mean(max_bl_345))/eh.RADPERUAS) + ' uas')
print('-'*100)

