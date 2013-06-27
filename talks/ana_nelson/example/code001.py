### @export "imports"
import matplotlib
import numpy.random

### @export "pyplot"
matplotlib.use("Agg")
import matplotlib.pyplot as pyplot

### @export "hist"
x = numpy.random.randn(10000)
pyplot.hist(x, 100)

### @export "save"
figfilename = "pyplot-hist-example.png"
figfile = open(figfilename, "wb")
pyplot.savefig(figfile)
figfile.close()

