import os
import sys

import pylab
import numpy
from mpl_toolkits.basemap import Basemap

motherdir = '.'
childdirs = os.listdir(motherdir)

shape = (151, 152)

for fname in childdirs:

    if not os.path.isdir(fname) and os.path.splitext(fname)[-1] == '.txt':

        sys.stderr.write("Plotting '%s'\n" % (fname))

        prefix = os.path.splitext(fname)[0]

        X, Y, Z = pylab.loadtxt(fname, unpack=True, dtype='f')

        X = numpy.reshape(X, shape)
        Y = numpy.reshape(Y, shape)
        Z = numpy.reshape(Z, shape)

        fig = pylab.figure(figsize=(5,5))
        
        pylab.axis('scaled')

        bm = Basemap(projection='merc', \
            llcrnrlon=X.min(), llcrnrlat=Y.min(), \
            urcrnrlon=X.max(), urcrnrlat=Y.max(), \
            lon_0=0.5*(X.max() + X.min()), lat_0=0.5*(Y.max() + Y.min()), \
            resolution='l', area_thresh=10000)

        dlon = 2.
        dlat = 2.
        bm.drawmeridians(numpy.arange(X.min(), X.max() - dlon, dlon), \
            labels=[0,0,0,1], fontsize=13, linewidth=1, rotation=45)#,labelstyle='+/-')
        bm.drawparallels(numpy.arange(Y.min() + dlat, Y.max() + dlat, dlat), \
            labels=[1,0,0,0], fontsize=13, linewidth=1)#,labelstyle='+/-')
        bm.drawcoastlines(linewidth=1.5)
        #bm.fillcontinents(color='coral')
        bm.drawmapboundary()
        #bm.bluemarble()
        bm.drawcountries(linewidth=1.5)
        #bm.drawstates(linewidth=1)

        X, Y = bm(X, Y)
        
        #cf = bm.pcolor(X, Y, Z, cmap=pylab.cm.jet)
        cf = bm.contourf(X, Y, Z, 30, cmap=pylab.cm.jet)
        #gist_earth

        cb = pylab.colorbar(orientation='vertical', shrink=0.83)

        for t in cb.ax.get_yticklabels():

            t.set_fontsize(14)

        pylab.savefig(prefix + ".pdf", fmt="pdf")

        pylab.close()
