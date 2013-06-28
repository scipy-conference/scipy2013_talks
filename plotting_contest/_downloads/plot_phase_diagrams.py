import  cdms2
from phase2d import mjo_phase2d, miso_phase2d

# plotting MJO Phase diagrams
f = cdms2.open('mjo_npcs.nc')

# Summer Data Extraction
npc1 = f('norm_pcs1', time=('1979-5-1', '1979-10-31'))
npc1.id = 'Normalized PC1'
npc2 = f('norm_pcs2', time=('1979-5-1', '1979-10-31'))
npc2.id = 'Normalized PC2'
# summer mjo phase plotting
# here sxyphase is 3 for this ('1979-5-1', '1979-10-31') time season only.
# this is just demonstration that we can pass sxyphase purpose only.
x = mjo_phase2d(npc1, npc2, sxyphase=3, pposition1=None, plocation='in',
                                      mintick=0, pdirection='anticlock')

x.ps('mjo_phase2d_summer')

# only single red color plot of summer
x = mjo_phase2d(npc1, npc2, sxyphase=3, colors=['red'], pposition1=None,
                      plocation='in', mintick=0, pdirection='anticlock')

x.ps('mjo_phase2d_summer_red')
# make memory free
del x, npc1, npc2

# Winter Data Extraction
npc1 = f('norm_pcs1', time=('1979-11-1', '1980-4-30'))
npc1.id = 'Normalized PC1'
npc2 = f('norm_pcs2', time=('1979-11-1', '1980-4-30'))
npc2.id = 'Normalized PC2'
# winter mjo phase plotting
# this is generic function call demonstration. For MJO we can make sxyphase 
# as None and using default argument to the pposition1 as 5.
x = mjo_phase2d(npc1, npc2, sxyphase=None, plocation='out', mintick=4)
x.ps('mjo_phase2d_winter')
f.close()

# only single red color plot of winter
x = mjo_phase2d(npc1, npc2, sxyphase=None, colors='red', plocation='out', mintick=4)
x.ps('mjo_phase2d_winter_red')
# make memory free
del x, npc1, npc2


# plotting MISO Phase diagrams
f = cdms2.open('miso_phases.nc')
xdata = f('miso1')
xdata.id = 'MISO1'
ydata = f('miso2')
ydata.id = 'MISO2'

x = miso_phase2d(xdata, ydata, sxyphase=None, plocation='out', mintick=4)
x.ps('miso_phase2d_monsoon')
f.close()
# make memory free
del x, xdata, ydata



