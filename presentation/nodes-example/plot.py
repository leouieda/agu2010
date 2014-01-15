import os

import pylab
import numpy

from fatiando.math import glq

w, e, s, n = pylab.loadtxt("model.txt", usecols=(0,1,2,3), unpack=True)
model_contourx = [w, e, e, w, w]
model_contoury = [n, n, s, s, n]
nodes = glq.nodes(2)
xnodes = glq.scale(w, e, nodes)
ynodes = glq.scale(s, n, nodes)

motherdir = '.'
childdirs = os.listdir(motherdir)

shape = (101, 101)

for fname in childdirs:

    if not os.path.isdir(fname) and os.path.splitext(fname)[-1] == '.dat':
		
        print "Ploting ", fname

        prefix = os.path.splitext(fname)[0]

        X, Y, Z = pylab.loadtxt(fname, unpack=True, dtype='f')

        X = numpy.reshape(X, shape)
        Y = numpy.reshape(Y, shape)
        Z = numpy.reshape(Z, shape)

        pylab.figure(figsize=(3,3))

        pylab.axis('scaled')

        pylab.contourf(X, Y, Z, 20, cmap=pylab.cm.jet, model_contourx=True)

        pylab.colorbar(orientation='vertical', shrink=0.78)

        pylab.plot(model_contourx, model_contoury, '-k', linewidth=2)

        for y in ynodes:
            for x in xnodes:

                pylab.plot(x, y, 'ow', markersize=6)

        pylab.xlim(X.min(), X.max())
        pylab.ylim(Y.min(), Y.max())

        pylab.savefig(prefix + ".pdf", fmt="pdf", transparent=True)

        pylab.close()

		
