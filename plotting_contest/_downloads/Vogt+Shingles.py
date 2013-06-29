

from enthought.tvtk.api import tvtk
from enthought.mayavi import mlab
from enthought.mayavi import modules
import pyfits
import numpy as np
import pickle

# Some constants ...
size_x = 142
size_y = 162
astopc = 0.286040071 # " to pc

# Forground stars position ... chopped them off, 
# and replace the by black spheres
stars = np.array([[30,30,5],[50,43,5],[40,52,5],[119,43,5],[67,120,4],
                  [122,42,5],[67,142,5],[110,80,7],[138,98,5],[136,67,6],[97,90,5]])

# Load the data ... a tad big, but it's a real IFU observation after all ...
fn = './data.pkl'
file = open(fn,'r')
print 'De-pickling data ...'
[x,y,z,x_b,y_b,z_b,
 scidata_cleana,scidata_cleana_noplane,scidata_cleanb] = pickle.load(file)
file.close()

print 'Plotting it ...'
# Start plotting ... make it an interactive 3D map !
fig1 = mlab.figure(bgcolor=(1.0,1.0,1.0),fgcolor=(0.0,0.0,0.0), size=(1200,900))

surf2 = mlab.contour3d(x,y,z,scidata_cleana,contours=[10],\
                opacity=0.5, colormap='RdYlBu', name='[O III]-1')
mlab.outline()
surf3 = mlab.contour3d(x,y,z,scidata_cleana,contours=[40],\
                opacity=1, colormap='Blues', name='[O III]-2')

surf5 = mlab.contour3d(x_b,y_b,z_b,scidata_cleanb,contours=[10],\
                           opacity=0.1,colormap='autumn', name='Hbeta')

surf6 =  mlab.points3d((stars[:,0]-size_x/2)*0.5*astopc,(stars[:,1]-size_y/2.)*0.5*astopc,stars[:,0]*0.0,stars[:,2]*0.5*astopc*2,color=(0,0,0), scale_factor=1, name = 'Stars')

# Now to make it look decent ...
ax = mlab.axes(extent=[-10,10,-12,12,-7,7],nb_labels=5)
ax.axes.fly_mode = 'outer_edges'
ax.title_text_property.font_size = 10
ax.title_text_property.font_family = 'courier'
ax.label_text_property.font_family = 'courier'

# And a bit of references if anyone is interested ...
mlab.text(0.05,0.95,'Oxygen-rich ejecta in SNR N132D. Vogt & Dopita, Ap&SS, 311, 521 (2011); Vogt & Shingles, Ap&SS (2013), submitted.',width=0.75)
mlab.text(0.05,0.05,'fvogt@mso.anu.edu.au',width=0.25)

# Label the axes ...
ax.axes.x_label = 'X (Dec.) [pc]'
ax.axes.y_label = 'Y (R.A.) [pc]'
ax.axes.z_label = 'Z [pc]'
mlab.show()
# Define the view point - useful to make a movie (not build here) ...
mlab.view(90,0,60) 

# Save it all ...
#mlab.savefig('Vogt+Shingles_test.wrl')
#mlab.savefig('Vogt+Shingles_test.eps')
#mlab.savefig('Vogt+Shingles_test.png')

print 'All done !'
# End of the World as we know it ...
