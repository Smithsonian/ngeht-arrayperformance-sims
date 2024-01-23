#######################################################
# imports

import numpy as np
import ngehtsim.metrics as cm
import ehtim as eh
import glob

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

#######################################################
# compute filling fractions

m_100_M87 = list()
s_100_M87 = list()
m_1000_M87 = list()
s_1000_M87 = list()
m_100_SgrA = list()
s_100_SgrA = list()
m_1000_SgrA = list()
s_1000_SgrA = list()

for idir, outdir in enumerate(outdirs):

    filelist_86_M87 = np.sort(glob.glob(outdir+'/uvfits_M87/*86GHz*uvfits'))
    filelist_230_M87 = np.sort(glob.glob(outdir+'/uvfits_M87/*230GHz*uvfits'))
    filelist_345_M87 = np.sort(glob.glob(outdir+'/uvfits_M87/*345GHz*uvfits'))

    ff100_M87 = np.zeros(len(filelist_86_M87))
    ff1000_M87 = np.zeros(len(filelist_86_M87))
    for i in range(len(filelist_86_M87)):
        with eh.parloop.HiddenPrints():
            obs_86 = eh.obsdata.load_uvfits(filelist_86_M87[i])
            obs_230 = eh.obsdata.load_uvfits(filelist_230_M87[i])
            obs_345 = eh.obsdata.load_uvfits(filelist_345_M87[i])
        obs_230.data['time'] += 0.0001
        obs_345.data['time'] += 0.0002
        obs = eh.obsdata.merge_obs([obs_345,obs_230,obs_86],force_merge=True)
        ff100_M87[i] = cm.calc_ff(obs,fov=100.0,longest_BL=14.66e9)
        ff1000_M87[i] = cm.calc_ff(obs,fov=1000.0,longest_BL=2.06e9)
    ff100mean_M87 = np.mean(ff100_M87)
    ff100std_M87 = np.std(ff100_M87)
    ff1000mean_M87 = np.mean(ff1000_M87)
    ff1000std_M87 = np.std(ff1000_M87)
    m_100_M87.append(ff100mean_M87)
    s_100_M87.append(ff100std_M87)
    m_1000_M87.append(ff1000mean_M87)
    s_1000_M87.append(ff1000std_M87)

    # print
    print('-'*40)
    print('M87 metrics for '+outdir+':')
    print('FF100: '+str(ff100mean_M87)+' +/- '+str(ff100std_M87))
    print('FF1000: '+str(ff1000mean_M87)+' +/- '+str(ff1000std_M87))
    print('-'*40)

    filelist_86_SgrA = np.sort(glob.glob(outdir+'/uvfits_SgrA/*86GHz*uvfits'))
    filelist_230_SgrA = np.sort(glob.glob(outdir+'/uvfits_SgrA/*230GHz*uvfits'))
    filelist_345_SgrA = np.sort(glob.glob(outdir+'/uvfits_SgrA/*345GHz*uvfits'))

    ff100_SgrA = np.zeros(len(filelist_86_SgrA))
    ff1000_SgrA = np.zeros(len(filelist_86_SgrA))
    for i in range(len(filelist_86_SgrA)):
        with eh.parloop.HiddenPrints():
            obs_86 = eh.obsdata.load_uvfits(filelist_86_SgrA[i])
            obs_230 = eh.obsdata.load_uvfits(filelist_230_SgrA[i])
            obs_345 = eh.obsdata.load_uvfits(filelist_345_SgrA[i])
        obs_230.data['time'] += 0.0001
        obs_345.data['time'] += 0.0002
        obs = eh.obsdata.merge_obs([obs_345,obs_230,obs_86],force_merge=True)
        ff100_SgrA[i] = cm.calc_ff(obs,fov=100.0,longest_BL=14.66e9)
        ff1000_SgrA[i] = cm.calc_ff(obs,fov=1000.0,longest_BL=2.06e9)
    ff100mean_SgrA = np.mean(ff100_SgrA)
    ff100std_SgrA = np.std(ff100_SgrA)
    ff1000mean_SgrA = np.mean(ff1000_SgrA)
    ff1000std_SgrA = np.std(ff1000_SgrA)
    m_100_SgrA.append(ff100mean_SgrA)
    s_100_SgrA.append(ff100std_SgrA)
    m_1000_SgrA.append(ff1000mean_SgrA)
    s_1000_SgrA.append(ff1000std_SgrA)

    # print
    print('-'*40)
    print('Sgr A* metrics for '+outdir+':')
    print('FF100: '+str(ff100mean_SgrA)+' +/- '+str(ff100std_SgrA))
    print('FF1000: '+str(ff1000mean_SgrA)+' +/- '+str(ff1000std_SgrA))
    print('-'*40)

#######################################################
# plot things

import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times"],
    "font.size": 10})

#######################################################
# plot M87

base_m_100 = m_100_M87[0]
base_s_100 = s_100_M87[0]
base_m_1000 = m_1000_M87[0]
base_s_1000 = s_1000_M87[0]

m_100 = np.array(m_100_M87[1:])
s_100 = np.array(s_100_M87[1:])
m_1000 = np.array(m_1000_M87[1:])
s_1000 = np.array(s_1000_M87[1:])

m_100_frac = 100.0*((m_100 - base_m_100)/base_m_100)
s_100_frac = 100.0*(s_100/base_m_100)
m_1000_frac = 100.0*((m_1000 - base_m_1000)/base_m_1000)
s_1000_frac = 100.0*(s_1000/base_m_1000)

s_100_frac_base = 100.0*(base_s_100 / base_m_100)
s_1000_frac_base = 100.0*(base_s_1000 / base_m_1000)

fig = plt.figure(figsize=(8,2))
ax1 = fig.add_axes([0.1,0.1,0.8,0.4])
ax2 = fig.add_axes([0.1,0.5,0.8,0.4])

x = np.linspace(1.0,len(m_100),len(m_100))

ax2.fill_between([0,20],[-s_100_frac_base,-s_100_frac_base],[s_100_frac_base,s_100_frac_base],color='gray',alpha=0.3,linewidth=0)
ax2.plot([0,20],[0.0,0.0],'k--')
ax2.errorbar(x,m_100_frac,yerr=s_100_frac,fmt='bo',markersize=4)

ax1.fill_between([0,20],[-s_1000_frac_base,-s_1000_frac_base],[s_1000_frac_base,s_1000_frac_base],color='gray',alpha=0.3,linewidth=0)
ax1.plot([0,20],[0.0,0.0],'k--')
ax1.errorbar(x,m_1000_frac,yerr=s_1000_frac,fmt='bo',markersize=4)

ax1.set_xlim(0,len(m_100)+1)
ax1.set_ylim(-11,11)
ax2.set_xlim(0,len(m_100)+1)
ax2.set_ylim(-30,30)

ax1.set_ylabel(r'$\Delta$FF1000 (\%)')
ax2.set_ylabel(r'$\Delta$FF100 (\%)')

ax1.set_xticks(x)
ax2.set_xticks(x)
ax1.set_xticklabels(['Option 1', 'Option 2', 'Option 3a\n(no SPM)', 'Option 3b\n(no LCO)', 'Option 3c\n(no CNI)', 'Option 3d\n(no JELM)', 'Option 4a\n(no SPM)', 'Option 4b\n(no LCO)', 'Option 4c\n(no CNI)', 'Option 4d\n(no JELM)', 'Option 5'],rotation=60,ha='center')
ax2.set_xticklabels([])

plt.savefig('comparison_M87.png',dpi=300,bbox_inches='tight')
plt.close()

#######################################################
# plot SgrA

base_m_100 = m_100_SgrA[0]
base_s_100 = s_100_SgrA[0]
base_m_1000 = m_1000_SgrA[0]
base_s_1000 = s_1000_SgrA[0]

m_100 = np.array(m_100_SgrA[1:])
s_100 = np.array(s_100_SgrA[1:])
m_1000 = np.array(m_1000_SgrA[1:])
s_1000 = np.array(s_1000_SgrA[1:])

m_100_frac = 100.0*((m_100 - base_m_100)/base_m_100)
s_100_frac = 100.0*(s_100/base_m_100)
m_1000_frac = 100.0*((m_1000 - base_m_1000)/base_m_1000)
s_1000_frac = 100.0*(s_1000/base_m_1000)

s_100_frac_base = 100.0*(base_s_100 / base_m_100)
s_1000_frac_base = 100.0*(base_s_1000 / base_m_1000)

fig = plt.figure(figsize=(8,2))
ax1 = fig.add_axes([0.1,0.1,0.8,0.4])
ax2 = fig.add_axes([0.1,0.5,0.8,0.4])

x = np.linspace(1.0,len(m_100),len(m_100))

ax2.fill_between([0,20],[-s_100_frac_base,-s_100_frac_base],[s_100_frac_base,s_100_frac_base],color='gray',alpha=0.3,linewidth=0)
ax2.plot([0,20],[0.0,0.0],'k--')
ax2.errorbar(x,m_100_frac,yerr=s_100_frac,fmt='bo',markersize=4)

ax1.fill_between([0,20],[-s_1000_frac_base,-s_1000_frac_base],[s_1000_frac_base,s_1000_frac_base],color='gray',alpha=0.3,linewidth=0)
ax1.plot([0,20],[0.0,0.0],'k--')
ax1.errorbar(x,m_1000_frac,yerr=s_1000_frac,fmt='bo',markersize=4)

ax1.set_xlim(0,len(m_100)+1)
ax1.set_ylim(-30,30)
ax2.set_xlim(0,len(m_100)+1)
ax2.set_ylim(-15,15)

ax1.set_ylabel(r'$\Delta$FF1000 (\%)')
ax2.set_ylabel(r'$\Delta$FF100 (\%)')

ax1.set_xticks(x)
ax2.set_xticks(x)
ax1.set_xticklabels(['Option 1', 'Option 2', 'Option 3a\n(no SPM)', 'Option 3b\n(no LCO)', 'Option 3c\n(no CNI)', 'Option 3d\n(no JELM)', 'Option 4a\n(no SPM)', 'Option 4b\n(no LCO)', 'Option 4c\n(no CNI)', 'Option 4d\n(no JELM)', 'Option 5'],rotation=60,ha='center')
ax2.set_xticklabels([])

plt.savefig('comparison_SgrA.png',dpi=300,bbox_inches='tight')
plt.close()

