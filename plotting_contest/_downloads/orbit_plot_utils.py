#!/usr/bin/env python

import math
import string
import datetime
import gzip

# Uranus, Neptune, and Pluto have minimal orbits available via HORIZONS.
# Chose to "center" the "x" axis on 330 degrees in order to image the
# outer planets.
EPHEMERIS_SHIFT = 360 - 330

class PlotUtils:
    def __init__(self, miny=96798622./4, maxy = 96798622.):
        self.months_dict = { 'Jan': 1,
                             'Feb': 2,
                             'Mar': 3,
                             'Apr': 4,
                             'May': 5,
                             'Jun': 6,
                             'Jul': 7,
                             'Aug': 8,
                             'Sep': 9,
                             'Oct':10,
                             'Nov':11,
                             'Dec':12 }

        self.au2km = 149597870.691

        self.maxy =   maxy
        self.miny =   miny

    def eph_open(self, filename, compress=0):
        fp = gzip.open(filename, "r")
   
        lines = fp.readlines()

        fp.close()

        # This seemed the best way, even though relying on very specific strings.
        # Find line that begins with $$SOE
        cnt = 0
        for line in lines:
            cnt = cnt + 1
            words = string.split(line)
            if len(words) == 0:
                continue
            if words[0] == '$$SOE':
                break

        lines = lines[cnt:]

        # Find line that begins with $$EOE
        cnt = 0
        for line in lines:
            cnt = cnt + 1
            words = string.split(line)
            if len(words) == 0:
                continue
            if words[0] == '$$EOE':
                break

        lines = lines[:cnt - 1]

        # Now lines list are those lines from the ephemeris data that are
        # between $$SOE and $$EOE.
        lines = [string.split(l) for l in lines]

        final_lines = []
        for rec in lines:
            year = int(rec[0][:4])
            month = self.months_dict[rec[0][5:8]]
            day = int(rec[0][9:11])
            hour = int(rec[1][:2])
            minute = int(rec[1][3:])

            d1 = datetime.datetime(year, month, day, hour=hour, minute=minute)

            longitude = math.radians(float(rec[2])  + EPHEMERIS_SHIFT)
            radius = float(rec[4]) * self.au2km

            x = radius * math.cos(longitude)
            y = radius * math.sin(longitude)


            final_lines.append([d1, (x, y), (radius, longitude)])

        if compress:
            final_lines = [i for i in final_lines if i[1][1] < self.maxy and
                                                 i[1][1] > -self.miny and
                                                 i[1][0] > -self.au2km]

        return final_lines


