#-*-coding:utf-8-*-
'''
Visualizing geolocated friendships within a social network in a map.

The input-file must be a dict, which the elements are:

{ ((latO,longO),(latD,longD)): qtd, ...}

(latO,longO) are the latitude and longitude of the origin location. Both are float values.
(latD,longD) ate the latitude and longitude of the destiny location. Both are float values.

qtd: An integer that represents the number of connections between both coordinates (cities).

'''

__author__ = 'caraciol@gmail.com'
__version__ = '0.1'

import pickle
from optparse import OptionParser
from optparse import SUPPRESS_USAGE
from math import sqrt,log


try:
    from PIL import Image, ImageDraw
except ImportError:
    print ('error while importing the PIL library.  please install it:  easy_install PIL')
    exit()

try:
    from pylab import get_cmap
    from matplotlib.colors import ColorConverter
    from matplotlib.colors import rgb2hex
    converter = ColorConverter()
except ImportError:
    print ('error while importing the MatPlotLib library.  please install it:  easy_install matplotlib')
    exit()

try:
    from numpy import logspace
except ImportError:
    print ('error while importing the Numpy library.  please install it:  easy_install numpy')
    exit()


MAX_LATITUDE = 5.0
MIN_LATITUDE = - 34.0

MAX_LONGITUDE = - 33.0
MIN_LONGITUDE = -75.0

LATITUDE_TOTAL = MIN_LATITUDE -  MAX_LATITUDE
LONGITUDE_TOTAL = MAX_LONGITUDE - MIN_LONGITUDE


def geo2pixel(lat,lon,width,height):
    x = (lat+ (MAX_LATITUDE*-1))  * height/LATITUDE_TOTAL
    y = (lon+(MIN_LONGITUDE*-1))  * width/LONGITUDE_TOTAL
    return round(x),round(y)


def run_main(options):
    try:
        inp = open(options.input_file,'rb')
        geo_input = pickle.load(inp)
        inp.close()
    except:
        print 'Problems in opening the %s. Check the file.' % options.input_file
        exit()

    width,height = map(int,options.size.split(','))
    mode_colormap = options.mode
    n_connections = options.n_connections

    #Create image
    im = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    geo_final = {}

    #Remove the same start == end and repeated cities (start,end) == (end,start).
    for origem,destino in geo_input:
        if origem != destino:
            if not geo_final.has_key((origem,destino)):
                if not geo_final.has_key((destino,origem)):
                    geo_final.setdefault((origem,destino),0)
                    geo_final[(origem,destino)] += geo_input[(origem,destino)]
                else:
                    geo_final.setdefault((destino,origem),0)
                    geo_final[(destino,origem)] += geo_input[(origem,destino)]

    matrix_geo = {}
    #Find all valid cities and calculate the distances
    max_distance = -10000000
    for origem,destino in geo_final:
        if geo_final[(origem,destino)] > n_connections:
            x1,y1 = geo2pixel(origem[0],origem[1],width,height)
            x2,y2 = geo2pixel(destino[0],destino[1],width,height)
            distance = sqrt((y2-y1)**2 + (x2-x1)**2)*40000/360.0
            if distance > max_distance:  max_distance = distance
            matrix_geo[(x1,y1),(x2,y2)] = distance

    #Sort by distance.
    sorted_matrix = sorted(matrix_geo.items(),key= lambda x: x[1], reverse=True)

    cmap =  get_cmap('jet')  if mode_colormap == 'all' else get_cmap('jet')
    dist_bins = logspace(1,log(max_distance)/log(10),255)


    #Plot using the correct colormap
    for ((x1,y1),(x2,y2)),distance in sorted_matrix:
        for i in range(len(dist_bins)-1):
            if distance > dist_bins[i] and distance < dist_bins[i+1]:
                break
        p = rgb2hex(converter.to_rgb(cmap(255-i)))
        draw.line([(y1,x1),(y2,x2)], p )

    #Save the image.
    im.save(options.output_file)






if __name__ == '__main__':
    parser = OptionParser(usage=SUPPRESS_USAGE)
    print 'geocialMapper v.%s\nBy %s\n' %(__version__,__author__)
    print "Type --help parameter for help.\n"

    parser.add_option('-i','--input-file',dest='input_file',
                       help='Pickle object file with coordinates and quantity')
    parser.add_option('-s','--size',dest='size',
                       help='image dimmensions height,width')
    parser.add_option('-o', '--output-file', dest='output_file', default= 'map.jpg',
                       help='Output file for saving the image')
    parser.add_option('-c', '--colormap', dest='mode', default='wb',
                       help='Mode of colormap used: wb, all')
    parser.add_option('-p', '--connection', dest='n_connections', default=0, type='int',
                       help= 'Threshold for the number of interconnections between cities')

    (options,args) = parser.parse_args()

    if not options.input_file:
        parser.error('You must specifiy a valid pickle object to load data (-i parameter) !')

    if not options.size:
        parser.error('You must specifiy the dimmensions of the image (-s parameter) !')

    run_main(options)
