"""
Script to plot molecular dynamics simulation results.

Author:  Elaine Angelino <elaine at eecs dot harvard dot edu>

Copyright 2011

"""

import os

import numpy as np
import tabular as tb

import pylab

	
def normalize(fin, fx, fy, fz):
	"""
	Split the input file into separate files for the three spatial dimensions.
	
	Parameters:
	
		**fin** : str
		
			Name of input file.  There is no header.  Every set of three lines
			corresponds to x-, y-, and z-coordinates for one time point.  Each
			column corresponds to one atom. 
			
		**fx** : str
		
			Name of output file for the x-dimension.  Each record corresponds to
			one time point.  Each column corresponds to one atom.  The columns
			are named in the first line of the file.
			
		**fy** : str
		
			Name of output file for the y-dimension, analogous to ``fx``.	

		**fz** : str
		
			Name of output file for the z-dimension, analogous to ``fx``.				
	
	"""
	
	ncols = len(open(fin, 'rU').readline().strip().split())
	names = [str(i) for i in range(ncols)]
	header = ' '.join(names) + '\n'
	
	f = open(fin, 'rU')
	gx = open(fx, 'w')
	gy = open(fy, 'w')
	gz = open(fz, 'w')	
			
	gx.write(header)
	gy.write(header)
	gz.write(header)
	
	while (1):			
		(x, y, z) = (f.readline(), f.readline(), f.readline())
		if (x.strip() == ''):
			break
		else:
			gx.write(x)
			gy.write(y)
			gz.write(z)
	
	f.close()
	gx.close()
	gy.close()
	gz.close()
	
	
def traces_2d(fx, fy, fz, dout,
		 	  colors=['red', 'orange', 'yellow', 'green', 
		 	  		  'cyan', 'blue', 'purple', 'magenta'], art=False):
	"""
	Parameters:
			
		**fx** : str
		
			Name of input file for the x-dimension.  Each record corresponds to
			one time point.  Each column corresponds to one atom.  The columns
			are named in the first line of the file.
			
		**fy** : str
		
			Name of input file for the y-dimension, analogous to ``fx``.	

		**fz** : str
		
			Name of input file for the z-dimension, analogous to ``fx``.
		
		**colors** : list of strings
		
		**art** : boolean
		
			Default is False; indicates whether or not graphic will be produced
			in ``art'' mode.  If False, the trajectory is plotted on a white
			background with axis ticks, axis labels, and a title.  If True, it 
			is plotted on a gray background without axis ticks, axis labels, or
			a title.
			
	"""

	if not os.path.exists(dout):
		os.mkdir(dout)
		
	names = open(fx, 'rU').readline().strip().split()
		
	recs = []
	
	flist = [fx, fy, fz]

	for i in range(len(flist)-1):
		fi = flist[i]
		di = fi[-1]
		for j in range(i + 1, len(flist)):
			fj = flist[j]
			dj = fj[-1]		
			for n in names[18:]:
				print di, dj, n
				# np1 = str(int(n) + 1)
				if (di == 'x') and (dj == 'y'):
					ii = tb.tabarray(SVfile=fi, usecols=[n]).extract()
					jj = tb.tabarray(SVfile=fj, usecols=[n]).extract()
					ind = np.cast[int](np.linspace(0, len(ii), len(colors) + 1))
					pylab.clf()
					if art:
						pylab.axes(axisbg='gray')					
					for k in range(len(ind) - 1):
						a = ind[k]
						b = ind[k+1]
						pylab.plot(ii[a:b], jj[a:b], colors[k])
					if art:
						pylab.axis('tight')
						pylab.xticks((),())
						pylab.yticks((),())
						pylab.savefig(os.path.join(dout, 
									  '%s-%s-%s-art-gray.png' % (di, dj, n)))
					else:
						pylab.axis((0, 12, 0, 12))
						pylab.title('n = %s' % n)
						pylab.xlabel(di)
						pylab.ylabel(dj)
						pylab.savefig(os.path.join(dout, 
									  '%s-%s-%s.png' % (di, dj, n)))
					pylab.clf()
					break
					

def template(droot, froot, art=False):

	normalize(fin=os.path.join(droot, froot), 
			  fx=os.path.join(droot, froot + '-x'),
			  fy=os.path.join(droot, froot + '-y'),
			  fz=os.path.join(droot, froot + '-z'))

	traces_2d(fx=os.path.join(droot, froot + '-x'),
		 	  fy=os.path.join(droot, froot + '-y'),
		 	  fz=os.path.join(droot, froot + '-z'),
		 	  dout=os.path.join(droot, froot + '-traces-2d'),
		 	  colors=['red', 'orange', 'yellow', 'green', 
		 	  		  'cyan', 'blue', 'purple', 'magenta'], art=art)
		 	  		  
def driver_out11(droot='', froot='out11', art=True):
	template(droot, froot, art)
	
def driver_out12(droot='', froot='out12', art=False):
	template(droot, froot, art)