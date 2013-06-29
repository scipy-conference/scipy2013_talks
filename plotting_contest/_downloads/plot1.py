"""
Script for the SciPy John Hunter Excellence in Plotting Contest.

Contestant: Rodrigo Nemmen (http://goo.gl/FRbxw)
E-mail: rsnemmen@gmail.com
Title: A Universal Scaling for the Energetics of Relativistic Jets from 
  Black Hole Systems
Type of plot: 2d scatter plot with linear regressions, uses Numpy and 
  Matplotlib

Scientific result:
The plot demonstrates that the relativistic outflows produced by supermassive 
black holes in the centers of active galaxies (displayed as BL Lacs and FSRQs 
in the plot) and stellar mass black holes in gamma-ray bursts (GRBs in the plot) 
follow the same universal scaling for their energetics. Hence, the result showed 
in this plot implies that the efficiency of energy dissipation in jets produced 
in black hole systems is similar over 10 orders of magnitude in jet power.

Description of the plot:
Relation between the collimation-corrected gamma-ray luminosity L = fb*Liso and 
the kinetic power Pjet for AGNs and GRBs. The shaded regions display the 2sigma 
confidence band of the fits. The blazar and GRB best-fit models (dashed and dotted 
lines, respectively) follow correlations that are consistent, within the uncertainties, 
with the best-fit model obtained from the joint data set (solid line). The best-fit 
parameters obtained from the combined data set are A = 0.98 ± 0.02 and B = 1.6 ± 0.9, 
where logPjet = AlogL + B. The scatter about the best-fit is 0.64 dex. The yellow data 
points correspond to XRF 020903 and GRB 090423, which we do not take into account 
in the statistics.

Reference: 
Nemmen, R., et al. Science, 2012, 338, 1445 (cf. Figure 3).
http://www.sciencemag.org/content/338/6113/1445

The Science article above can be retrieved for free at the address 
http://goo.gl/lnQEm (click the Science cover image in the web page) or 
at http://arxiv.org/abs/1212.3343 (arXiv article repository).
"""

import numpy, pylab

# Imports data
# =============
grb=numpy.load('grb.npz')
blazar=numpy.load('blazar.npz')
all=numpy.load('all.npz')
fgrb=numpy.load('fgrb.npz')
sgrb=numpy.load('sgrb.npz')
psgrb=numpy.load('psgrb.npz')




# Plots: data
# ===============
pylab.clf()

# Blazars
bl=blazar['bl']
q=blazar['q']

# Error bars
pylab.errorbar(psgrb['x'],psgrb['y'],yerr=psgrb['erry'],xerr=psgrb['errx'],fmt=None,ecolor='DodgerBlue',label='_nolegend_')
pylab.errorbar(sgrb['x'],sgrb['y'],yerr=sgrb['erry'],xerr=sgrb['errx'],fmt=None,ecolor='MediumSeaGreen',label='_nolegend_')
pylab.errorbar(fgrb['x'],fgrb['y'],yerr=fgrb['erry'],xerr=fgrb['errx'],fmt=None,ecolor='Tomato',label='_nolegend_')
pylab.errorbar(blazar['xdata'][bl],blazar['ydata'][bl],yerr=blazar['erry'][bl],xerr=blazar['errx'][bl],fmt=None,ecolor='DarkCyan',label='_nolegend_')
pylab.errorbar(blazar['xdata'][q],blazar['ydata'][q],yerr=blazar['erry'][q],xerr=blazar['errx'][q],fmt=None,ecolor='MediumOrchid',label='_nolegend_')	

# GRBs
pylab.plot(psgrb['x'], psgrb['y'],'ob',label='Pre-Swift GRBs')
pylab.plot(sgrb['x'], sgrb['y'],'og',label='Swift GRBs')
pylab.plot(fgrb['x'], fgrb['y'], 'or',label='Fermi GRBs')

# Blazars
pylab.plot(blazar['xdata'][bl], blazar['ydata'][bl],'sc',label='BL Lacs')
pylab.plot(blazar['xdata'][q], blazar['ydata'][q], '*m',label='FSRQs')

# LLGRBs
pylab.plot(grb['xdata'][33], grb['ydata'][33],'og',markersize=8)
pylab.plot(grb['xdata'][15], grb['ydata'][15],'ob',markersize=8)


# Only limits
# XRF 020903 (theta unknown)
xrflg,xrfkp=48.14, 49.7
pylab.plot(xrflg, xrfkp, 'oy',zorder=11)
pylab.quiver(xrflg, xrfkp,-0.9,-0.9,color='k',scale=30,width=0.004,zorder=10)
# 090423 (theta>4deg)
xrflg,xrfkp=51.3, 51.9
pylab.plot(xrflg, xrfkp, 'oy',zorder=11)
pylab.quiver(xrflg, xrfkp,+0.9,+0.9,color='k',scale=30,width=0.004,zorder=10)





# Plots: Fits
# ============
def plotfit(x,y,lcb,ucb,linestyle='',confcolor='gray',front=False,**args):
	# Line
	pylab.plot(x,y,linestyle,**args)

	# Plots confidence band
	if front==True:
		zorder=10
	else:
		zorder=None
	pylab.fill_between(x, lcb, ucb, alpha=0.3, facecolor=confcolor, zorder=zorder)


## GRB BCES
plotfit(grb['x'],grb['y'],grb['lcb'],grb['ucb'],linestyle='k:',confcolor='green',linewidth=1.5)

## Blazar BCES
plotfit(blazar['x'],blazar['y'],blazar['lcb'],blazar['ucb'],linestyle='k--',confcolor='blue',linewidth=1.5,front=True)

## All BCES
plotfit(all['x'],all['y'],all['lcb'],all['ucb'],linestyle='k',confcolor='gray',front=True)






pylab.xlim(41,52)
pylab.ylim(41,54)
pylab.ylabel('$\log P_{\\rm jet}$ (erg s$^{-1}$)')
pylab.xlabel('$\log L$ (erg s$^{-1}$)')
pylab.minorticks_on()
import matplotlib.font_manager	# need to import this in order to change the size of the fonts in the legend
pylab.legend(loc='best', numpoints=1, frameon=False, prop=matplotlib.font_manager.FontProperties(size='small'))
pylab.axes().set_aspect('equal')
pylab.show()
pylab.draw()


