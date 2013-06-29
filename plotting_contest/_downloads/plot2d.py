import os

import numpy as np

import tabular as tb

import pylab

from matplotlib.patches import Ellipse

from convexhull import convexHull

import files
import utils

#(z, data)=scatter(fin='../data/words/ingredients-T.tsv', out='../data/scatter/20110907/')
def scatter(fin='../data/original.tsv', out='../data/scatter/20110902/', figname='some', ellipses=False, contours=False, conv_hull=True, conv_thresh=[0.2], xnum=10, ynum=10, norm=None, mew=1, legend=False, special=None, simple=True, typevec=None, colorvec=None):

	print figname

	utils.safe_mkdir(out)
	z = files.filter_hack(tb.tabarray(SVfile=fin))
	
	names = np.array([n for n in z.dtype.names if n not in ['type', 'names', 'name', 'ingredients']])
	
	a = z[names].extract()
	
	if norm == None:
		a = utils.normalize(a)	# normalize data 

	if figname.startswith('some'):
		typevec = ['chocolate-cakes', 'angel-food-cakes', 'brownies', 'sugar-cookies', 'scones', 'loaves', 'pancakes', 'crepes']
		colorvec = ['brown', 'g', 'm', 'b', 'k', 'r', 'y', 'c']
	elif figname.startswith('all'):
		typevec = ['']
		z['type'] = ''
		colorvec = ['g']
	
	ingredientvec = ['white sugar', 'all-purpose flour']
	name_dict = dict(zip(names, range(len(names))))	
	
	idict = {}	
	for i in ['egg', 'flour', 'sugar', 'oil']:
		idict[i] = [n for n in z.dtype.names if i in n]

	idict['liquid'] = ['water']
	idict['liquid'] += [n for n in z.dtype.names if ('milk' in n) and ('powder' not in n) and ('chip' not in n)]
	idict['liquid'] += [n for n in z.dtype.names if ('juice' in n) and ('with' not in n)]
	
	idict['sugar'] += ['corn syrup', 'light corn syrup']

	idict['butter'] = ['butter', 'margarine', 'butter or margarine', 'butter or stick margarine']
	idict['oil'] += [n for n in z.dtype.names if 'shortening' in n]	
	idict['fat'] = idict['butter'] + idict['oil']
	idict.pop('butter')
	idict.pop('oil')
	
	print idict
	
	columns = []
	ingredientvec = idict.keys()
	for i in ingredientvec:
		name_list = np.array([name_dict[j] for j in idict[i]])
		columns += [a[:, name_list].sum(axis=1)]
	data = tb.tabarray(columns=columns, names=ingredientvec)
	print data
	n = len(ingredientvec)
	
	if norm is not None:
		d = data.extract()
		i = list(data.dtype.names).index(norm)
		array = d / np.repeat(d[:,i], d.shape[1]).reshape(d.shape[0], d.shape[1])
		data = tb.tabarray(array=array, names=data.dtype.names)
	
	for j1 in range(n-1):
		i1 = ingredientvec[j1]
		for j2 in range(j1+1, n):
			i2 = ingredientvec[j2]
			k = 0
			pylab.clf()
			for kind in typevec:		
				color = colorvec[k]
		
		
				#p = a[z['type']==kind][:,name_dict[i1]]
				#q = a[z['type']==kind][:,name_dict[i2]]
				p = data[z['type']==kind][i1]
				q = data[z['type']==kind][i2]
				
				if simple:
					pylab.plot(p, q, '+', color=color, markeredgewidth=mew)
					
				if conv_hull:
					
					for ct in conv_thresh:
				
						x = p.mean()
						y = q.mean()
						d = np.sqrt((x - p)**2 + (y - q)**2)
						ind = d.argsort()[:-int(len(p) * ct)]							
						pts = [(p[j], q[j]) for j in ind]
						if pts:
							hull = np.array(convexHull(pts))
							pylab.fill(hull[:,0], hull[:,1], color=color, alpha=0.2)
						#else:
						#	print t		
					
				k += 1

			pylab.xlabel(i1)
			pylab.ylabel(i2)

			if special is not None:
				p = data[z['name']==special][i1]
				q = data[z['name']==special][i2]
				pylab.plot(p, q, '*', color='y', markersize=20, mew=2)
			
			if legend:
				if special is not None:
					pylab.legend(typevec + [special])	
				else:
					pylab.legend(typevec)	
				
			if norm is None:
				pylab.axis([0, 1, 0, 1])
			
			pylab.savefig(out + figname + '_' + i1 + '_' + i2 +'.pdf')

	if special is not None:
		pylab.legend(typevec + [special])	
	else:
		pylab.legend(typevec)	
	pylab.savefig(out + figname + '_legend.pdf')

	data = z[['type', 'name']].colstack(data)
	
	if figname.startswith('some'):
		data.saveSV('../data/words/ingredients-basic.tsv')
		
	return (z, data)

def simplex(fin='../data/words/ingredients-basic.tsv', out='../data/simplex/20110920/', figname='some', ellipses=False, contours=False, conv_hull=True, conv_thresh=[0.2], xnum=10, ynum=10, norm=True, linewidth=0.2, text=True, mew=1.5, special=None):

	utils.safe_mkdir(out)
	z = tb.tabarray(SVfile=fin)
	
	names = [n for n in z.dtype.names if n not in ['type', 'names', 'name', 'ingredients']]
	
	n = len(names)

	array = utils.normalize(z[names].extract())
	data = tb.tabarray(array=array, names=names)	

	if figname.startswith('some'):
		typevec = ['chocolate-cakes', 'angel-food-cakes', 'brownies', 'sugar-cookies', 'scones', 'loaves', 'pancakes', 'crepes']
		colorvec = ['brown', 'g', 'm', 'b', 'k', 'r', 'y', 'c']
	elif figname.startswith('all'):
		typevec = ['']
		z['type'] = ''
		colorvec = ['g']
	
	for j1 in range(n):
		i1 = names[j1]
		for j2 in range(n):
			i2 = names[j2]
			for j3 in range(n):
				i3 = names[j3]
				k = 0
				pylab.clf()
				for kind in typevec:		
					color = colorvec[k]
			
					p = data[z['type']==kind][i1] - data[z['type']==kind][i2]
					q = np.sqrt(3) * data[z['type']==kind][i3]

					pylab.plot(p, q, '+', color=color, markeredgewidth=mew)
					
					if conv_hull:
						
						for ct in conv_thresh:
					
							x = p.mean()
							y = q.mean()
							d = np.sqrt((x - p)**2 + (y - q)**2)
							ind = d.argsort()[:-int(len(p) * ct)]							
							pts = [(p[j], q[j]) for j in ind]
							if pts:
								hull = np.array(convexHull(pts))
								pylab.fill(hull[:,0], hull[:,1], color=color, alpha=0.2)
						
					k += 1

				if special is not None:
					p = data[z['name']==special][i1] - data[z['name']==special][i2]
					q = np.sqrt(3) * data[z['name']==special][i3]				
					pylab.plot(p, q, '*', color='y', markersize=20, mew=2)

				pylab.plot([-1, 1], [0, 0], 'k-.', linewidth=linewidth)
				pylab.plot([-1, 0], [0, np.sqrt(3)], 'k-.', linewidth=linewidth)
				pylab.plot([0, 1], [np.sqrt(3), 0], 'k-.', linewidth=linewidth)				
	
				if text:
					pylab.text(1.1, -0.1, i1, fontsize=16)
					pylab.text(-1.1, -0.1, i2, fontsize=16)
					pylab.text(-0.05, 1.8, i3, fontsize=16)
				
				pylab.axis('equal')
				pylab.axis('off')
				
				pylab.savefig(out + figname + '_' + '_'.join([i1, i2, i3]) +'.pdf', transparent=True)

	if special is not None:
		pylab.legend(typevec + [special])	
	else:
		pylab.legend(typevec)		
	pylab.savefig(out + figname + '_legend.pdf', transparent=True)
		
	return (z, data)

def make_contours(x, y, xnum=100, ynum=100, margin=0.1):
	xmin = x.min()
	xmax = x.max()
	ymin = y.min()
	ymax = y.max()
	xm = (xmax - xmin) * margin
	ym = (ymax - ymin) * margin

	xvec = np.linspace(xmin - xm, xmax + xm, xnum)
	yvec = np.linspace(ymin - ym, ymax + ym, ynum)
	xhalf = (xvec[1] - xvec[0]) / 2
	yhalf = (yvec[1] - yvec[0]) / 2
	Z = np.zeros((xnum-1, ynum-1))
	for i in range(xnum-1):
		for j in range(ynum-1):
			z = ((x >= xvec[i]) & (x < xvec[i+1])) & ((y >= yvec[j]) & (y < yvec[j+1]))
			Z[i,j] = z.sum()
	(X, Y) = np.meshgrid(xvec[:-1]+xhalf, yvec[:-1]+yhalf)		
	return (X, Y, Z)	# input to pylab.contour

def plot_contours(x, y, xnum=100, ynum=100, colors=None, margin=0.1):
	(X, Y, Z) = make_contours(x, y, xnum, ynum, margin)
	pylab.contour(X, Y, Z, colors=colors)
	return (X, Y, Z)	

def get_ellipse(x, y):
	a = np.column_stack((x, y))
	a = a - np.repeat(a.mean(axis=0), a.shape[0]).reshape(a.shape[1], a.shape[0]).T	# mean center
	(w, v) = np.linalg.eig(np.cov(a.T))
	i = np.nonzero((-w).argsort()==0)[0][0]		# indices for the top 2 eigenvalues
	j = np.nonzero((-w).argsort()==1)[0][0]	
	xy = (np.mean(x), np.mean(y))
	width = np.sqrt(w[i]) * 2
	height = np.sqrt(w[j]) * 2
	unit = np.array([1, 0])
	vi = v[:,i]
	#vi = vi / norm(vi)		# already normalized
	theta = utils.get_theta(vi, unit)
	angle = utils.rad_to_deg(theta)
	return (xy, width, height, angle)

def plot_ellipse(x, y, ax, color):
	(xy, width, height, angle) = get_ellipse(x, y)
	e = Ellipse(xy, width, height, angle)
	ax.add_artist(e)
	#e.set_clip_box(ax.bbox)
	e.set_alpha(0.2)
	e.set_facecolor(color)
