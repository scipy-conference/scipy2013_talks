### @export "import-data"
import csv

csv_file = open("data.csv", "rb")
reader = csv.reader(csv_file)
x = []
y = []
for row in reader:
    x.append(row[0])
    y.append(row[1])
    print row

print x
print y

### @export "setup-pyplot"
import matplotlib
import numpy.random
matplotlib.use("Agg")
import matplotlib.pyplot as pyplot

### @export "graph-data"
pyplot.plot(x, y)

### @export "save-graph"
figfilename = "pyplot-xy-example.png"
figfile = open(figfilename, "wb")
pyplot.savefig(figfile)
figfile.close()

