


import plot_gen as pg
import numpy as np

# # Some subtraction plots
# # vorticity (da) 
# # levels = np.linspace(-.09,.09,10)
# smax: np.linspace(-.9,.9,10), smean: np.linspace(-.45,.45,10)
# zetamax: np.linspace(-.01,.01,9)
var = {'vort':{'levels':np.linspace(-.0045,.0045,10),'colormap':'RdGy_r','title':r'$\Delta$Max vertical vorticity $(1/s)$'},
	   'tke':{'levels':np.linspace(-.09,.09,10),'colormap':'RdGy_r','title':r'$\Delta$Max TKE ($m^2/s^2$)'},
	   'w':{'levels':np.linspace(-.9,.9,10),'colormap':'RdGy_r','title':r'$\Delta$Max vertical velocity $(m/s)$'},
	   's':{'levels':np.linspace(-.9,.9,10),'colormap':'RdGy_r','title':r'$\Delta$Max horizontal speed $(m/s)$'},
	   'zeta':{'levels':np.linspace(-.0001,.0001,9),'colormap':'RdGy_r','title':r'$\Delta$Mean zeta $(m)$'},
	   'mkpd':{'levels':np.linspace(-.9,.9,10),'colormap':'RdGy_r','title':r'$\Delta$ mean kinetic power density $(kW/m^2)$'},
	   'abi':{'levels':np.linspace(-27,27,10),'colormap':'RdGy_r','title':r'$\Delta$ asymmetry (degrees)'},
	   'stdbi':{'levels':np.linspace(-27,27,10),'colormap':'RdGy_r','title':r'$\Delta$ directional deviation (degrees)'}}

name = 'tke' # when i want to do more do a loop
oper = 'max' # operation (max, mean, metric, min,gradmean)
zoom = 'zmid'
# vlevel = 'hubheight' #'surface'#'hubheight' (depth-averaged)
data = np.load('diff.npz')
diff = data['diff']
x = data['x']
y = data['y']
mask = data['mask']
data.close()

### TEMP
# ind = np.arange(0,50)#15,15+25) # half the cycle

# diff = d.max(axis=0)-dr.max(axis=0)

pg.plt(x/1000.,y/1000.,diff,mask,zoom,
	var[name]['colormap'],var[name]['levels'],
	name + oper + '.pdf',
	var[name]['title'])