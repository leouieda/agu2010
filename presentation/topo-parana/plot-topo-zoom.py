import os
import sys

import pylab
import numpy
from mpl_toolkits.basemap import Basemap

xmin, xmax, ymin, ymax = -57.5, -47.4333, -27.5, -17.5

motherdir = '.'
childdirs = os.listdir(motherdir)

shape = (151, 151)

for fname in childdirs:
    
    if  not os.path.isdir(fname) and os.path.splitext(fname)[-1] == '.xyz':

        sys.stderr.write("Plotting zoom topography\n")
        
        prefix = os.path.splitext(fname)[0]
        
        X, Y, Z = pylab.loadtxt(fname, unpack=True, dtype='f')
        
        X = numpy.reshape(X, shape)
        Y = numpy.reshape(Y, shape)
        Z = numpy.reshape(Z, shape)
        
        fig = pylab.figure(figsize=(5,5))
        
        pylab.axis('scaled')
        
        bm = Basemap(projection='merc', \
            llcrnrlon=xmin, llcrnrlat=ymin, \
            urcrnrlon=xmax, urcrnrlat=ymax, \
            lon_0=0.5*(xmax + xmin), lat_0=0.5*(ymax + ymin), \
            resolution='l', area_thresh=10000)
        
        dlon = 2.
        dlat = 2.
        bm.drawmeridians(numpy.arange(xmin, xmax - dlon, dlon), \
            labels=[0,0,0,1], fontsize=13, linewidth=1, rotation=45)#,labelstyle='+/-')
        bm.drawparallels(numpy.arange(ymin + dlat, ymax + dlat, dlat), \
            labels=[1,0,0,0], fontsize=13, linewidth=1)#,labelstyle='+/-')
        bm.drawcoastlines(linewidth=1.5)
        #bm.fillcontinents(color='coral')
        bm.drawmapboundary()
        #bm.bluemarble()
        bm.drawcountries(linewidth=1.5)
        #bm.drawstates(linewidth=1)
        
        X, Y = bm(X, Y)
        
        cf = bm.pcolor(X, Y, Z, cmap=pylab.cm.gist_earth, vmin=-1000, vmax=1000)
        #cf = bm.contourf(X, Y, Z, 25, cmap=pylab.cm.gist_earth, vmin=-1000, vmax=1000)
        
        cb = pylab.colorbar(orientation='vertical', shrink=0.84)
        
        for t in cb.ax.get_yticklabels():
            
            t.set_fontsize(14)
        
        #pylab.savefig(prefix + "-zoom2.pdf", fmt="pdf")
        pylab.savefig(prefix + "-zoom.png", fmt="png", dpi=250)
        pylab.close()