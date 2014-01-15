import os
import sys

import pylab
import numpy
from mpl_toolkits.basemap import Basemap

xmin, xmax, ymin, ymax = -65.0, -40.0, -35.0, -10.0

zoom_x = [xmin, xmax, xmax, xmin, xmin]
zoom_y = [ymax, ymax, ymin, ymin, ymax]

xmin, xmax, ymin, ymax = -75.0, -30.0, -45.0, 0.0

sys.stderr.write("Plotting bigger map\n")

fig = pylab.figure(figsize=(5,5))

#pylab.axis('scaled')

bm = Basemap(projection='merc', \
    llcrnrlon=xmin, llcrnrlat=ymin, \
    urcrnrlon=xmax, urcrnrlat=ymax, \
    lon_0=0.5*(xmax + xmin), lat_0=0.5*(ymax + ymin), \
    resolution='i', area_thresh=10000)

dlon = 5.
dlat = 5.
bm.drawmeridians(numpy.arange(xmin, xmax, dlon), \
    labels=[0,0,0,1], fontsize=12, linewidth=1, rotation=45)#,labelstyle='+/-')
bm.drawparallels(numpy.arange(ymin + dlat, ymax + dlat, dlat), \
    labels=[1,0,0,0], fontsize=12, linewidth=1)#,labelstyle='+/-')
    
bm.drawcoastlines(linewidth=1.5)
bm.fillcontinents(color='green')
bm.drawmapboundary()
#bm.bluemarble()
bm.drawcountries(linewidth=1.5)
#bm.drawstates(linewidth=1)

zoom_x, zoom_y = bm(zoom_x, zoom_y)

bm.plot(zoom_x, zoom_y, '-r', linewidth=3)

pylab.savefig("map.pdf", fmt="pdf")

pylab.close()