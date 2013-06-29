#!/usr/bin/env python

# Copyright 2011
#Lucía B. Avalle
#Group of Electrochemistry. Experimental and Theoretical Aspects. Institute of Physics Enrique Gaviola (IFEG), FaMAF, UNC
# Córdoba, Argentina

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#Using the GNU GPL will require that all the released improved versions be free software. 
#This means you can avoid the risk of having to compete with a proprietary modified version of your own work.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Authors:
#       Leoncio Juan Ernesto Lopez (anicholo at gmail dot com)

# $Id: pulsefile.py 9 2011-06-06 00:27:31A takenoko $


"""The potentiostatic pulses applied to the solid/liquid interface consist of different amplitudes, starting at a potential where no hydrogen evolves."""

"""This program was developed to load transient data from file at location filename. The in files are formated according the output of two-channel oscilloscope. The out files have only time and CH* (*= 1, 2) columns space-separated. The structure and program code meet educational goals"""

import sys

try:
    infilename = sys.argv[1];  outfilename = sys.argv[2]
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)


def load_data(infilename):
    f = open(infilename, 'r'); lines = f.readlines(); f.close()

    i = 0; values = [] #empty list
    for line in lines[24:]: #eliminates the headers
        arglist = line.split(",")
        value = float(arglist[3]), float(arglist[4]) #start from zero: space[0],space[1],space[2],number[3],number[4],
	values.append(value) #tuple list
	i = i+1
    return values

def dump_data(filename, values):
    # write out 2-column files:
    of = open(filename, 'w')
    for i in range(len(values)):
        of.write('%12.5e %12.5e\n' % values[i]) 
    of.close()

values = load_data(infilename) #function call for execution
dump_data(outfilename, values)
print 'We are done!'

