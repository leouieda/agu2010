import os
import sys

import pylab
import numpy
from mpl_toolkits.basemap import Basemap

xmin, xmax, ymin, ymax = -57.5, -47.4333, -27.5, -17.5

zoom_x = [xmin, xmax, xmax, xmin, xmin]
zoom_y = [ymax, ymax, ymin, ymin, ymax]

motherdir = '.'
childdirs = os.listdir(motherdir)

shape = (151, 151)

for fname in childdirs:

    if  not os.path.isdir(fname) and os.path.splitext(fname)[-1] == '.xyz':

        sys.stderr.write("Plotting full topography\n")

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

        dlon = 5.
        dlat = 5.
        bm.drawmeridians(numpy.arange(X.min(), X.max(), dlon), \
        labels=[0,0,0,1], fontsize=12, linewidth=1, rotation=45)#,labelstyle='+/-')
        bm.drawparallels(numpy.arange(Y.min() + dlat, Y.max() + dlat, dlat), \
        labels=[1,0,0,0], fontsize=12, linewidth=1)#,labelstyle='+/-')
        bm.drawcoastlines(linewidth=1.5)
        #bm.fillcontinents(color='coral')
        bm.drawmapboundary()
        #bm.bluemarble()
        bm.drawcountries(linewidth=1.5)
        #bm.drawstates(linewidth=1)

        X, Y = bm(X, Y)

        cf = bm.pcolor(X, Y, Z, cmap=pylab.cm.gist_earth, vmin=-1000, vmax=1000)

        cb = pylab.colorbar(orientation='vertical', shrink=0.84)

        for t in cb.ax.get_yticklabels():

            t.set_fontsize(14)

        zoom_x, zoom_y = bm(zoom_x, zoom_y)

        bm.plot(zoom_x, zoom_y, '-r', linewidth=3)

        pylab.savefig(prefix + ".png", fmt="png")

        pylab.close()
