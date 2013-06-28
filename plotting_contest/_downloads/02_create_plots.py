#!/usr/bin/env python

import os
import random
import matplotlib
matplotlib.use('Agg')

import datetime
import pylab as P
import numpy as N

import orbit_plot_utils
from variables import data_dict
from variables import color_table

from matplotlib.font_manager import FontProperties
ital = FontProperties()
ital.set_style('italic')

au2km = 149597870.691
xpagescale = au2km*0.25
ypagescale = xpagescale/8.5*11.0
ymin = -ypagescale*1.75/11.0
ymax = ymin + ypagescale

pages = range(198)
xoffset = -xpagescale*4.75/8.5

# 72 (points/inch) * 8.5 (inches) / xpagescale (km)
km2points = 72*8.5/xpagescale
points2km = 1.0/km2points

planets = [i for i in data_dict if str(i)[-2:] == '99' and i > 0 and i < 1000]
satellites = [i for i in data_dict if str(i)[-2:] != '99' and i > 0 and i < 1000]

# minimum line width
mlw = 0.1

def data_clip(x_data, x_min, x_max, y_data, y_min, y_max, d_data, date_min, date_max): 
    ''' 
    Clips data to just outside the plot axes.  Creates a boolean array of
    shaped like clip_data with contiguous values between data_min and data_max
    set to true.  Uses this boolean array to mask x_data and y_data.
    '''
    x_b = N.logical_and(x_data >= x_min,
                        x_data <= x_max)
    y_b = N.logical_and(y_data >= y_min,
                        y_data <= y_max)
    d_b = N.logical_and(d_data >  date_min,
                        d_data <  date_max)

    for vari in [x_b, y_b]:
        min_indices = N.compress(vari, N.indices(x_data.shape))

        if len(min_indices) == 0:
            return [0],[0],[0]

        mini = min_indices[0] - 1
        if min_indices[0] == 0:
            mini = 0
        maxi = min_indices[-1] + 1
        if min_indices[-1] == (len(vari) - 1):
            maxi = -1
        vari[mini] = True
        vari[maxi] = True

    f_b = N.logical_and(d_b, x_b, y_b)
    indices = N.compress(f_b, N.indices(x_data.shape))

    if len(indices) == 0:
        return [0],[0],[0]

    low_step = 1
    if indices[0] == 0:
        low_step = 0
    xplot = x_data[indices[0] - low_step: indices[-1] + 2]
    yplot = y_data[indices[0] - low_step: indices[-1] + 2]
    odate = d_data[indices[0] - low_step: indices[-1] + 2]
    return xplot, yplot, odate


def make_plot_framework(figsize, facecolor = 'white'):
    P.figure(figsize = figsize, frameon = False)
    P.axes([0, 0, 1, 1], axisbg = facecolor)
    return


def make_plot_final_touch(xin, (xn0, yn0, xn1, yn1), box = False, border_color = False, box_color = 'black', zoom = 1, heliocentric = True):

    if border_color:
        tcolor = 'white'
    else:
        tcolor = 'gray'

    linespacing = 250000/zoom
    offset = 10000/zoom
    for lsat in xin:
        offset = max(data_dict[lsat]['radius'], offset)
        offset = data_dict[lsat]['radius']
        if data_dict[lsat]['horizontalalignment'] != 'left':
            offset = offset*(-1)
        if heliocentric:
            lx = label_data[lsat][0]
            ly = label_data[lsat][1]
        else:
            lx = label_data[lsat][2]
            ly = label_data[lsat][3]

        P.scatter([lx], [ly], N.pi*(data_dict[lsat]['radius']*km2points*zoom)**2, 'blue', linewidth=data_dict[lsat]['line_width'], edgecolors='none', zorder = 500)
        P.plot([lx], [ly] , 'gx', markersize = 4, zorder = 525)

        if box:
            if not (lx > box[0] and lx < box[2] and ly > box[1] and ly < box[3]):
                P.text(lx + offset, ly + linespacing, data_dict[lsat]['name'], fontproperties = ital, fontsize = 8, color = tcolor, zorder = 600, ha = data_dict[lsat]['horizontalalignment'], va = data_dict[lsat]['verticalalignment'])
        else:
            P.text(lx + offset, ly + linespacing, data_dict[lsat]['name'], fontproperties = ital, fontsize = 8, color = tcolor, zorder = 600, ha = data_dict[lsat]['horizontalalignment'], va = data_dict[lsat]['verticalalignment'])

    if box:
        print zoom, box_color
        P.plot((box[0], box[2], box[2], box[0], box[0]), (box[1], box[1], box[3], box[3], box[1]), color = box_color, zorder = 700, linewidth = 1)

    if border_color:
        # This is for the zoomed plots
        lw = 4
        delta = 90000/zoom
        P.plot((xn0, xn1 - (lw/2.4*points2km)/zoom, xn1 - (lw/2.4*points2km)/zoom, xn0, xn0), (yn0, yn0, yn1 - (lw/3.4*points2km)/zoom, yn1 - (lw/3.4*points2km)/zoom, yn0), color = border_color, linewidth = lw, zorder = 550)
        for lsat in xin:
            if lsat in planets:
                # date in the bottom left hand corner
                P.text(xn0 + 500000/zoom, yn0 + 500000/zoom, data_dict[data_dict[lsat]['target']]['label'].date(), fontsize = 6, color = tcolor, zorder = 600)
    else:
        # This is for the 1x plots
        points = 20
        ydelt = N.arange(ymin, ymax + 1, (ymax - ymin)/points)
        for sata in reversed(planets):
            clr = '0.9'
            if data_dict[sata]['name'] == 'Neptune':
                clr = '0.8'
            tdata = data_dict[sata]['perihelion']
            xdelt = tdata*N.cos(N.arcsin(ydelt/tdata))
            lside = 0.7
            angle = N.arctan2((ydelt[int(points*lside) + 1] - ydelt[int(points*lside) - 1]), (xdelt[int(points*lside) + 1] - xdelt[int(points*lside) - 1]))*180/N.pi + 180
            P.text(xdelt[int(points*lside)], ydelt[int(points*lside)], '%s perihelion' % (data_dict[sata]['name']), fontsize = 6, color = 'gray', rotation = angle, va = 'center', ha = 'center', zorder = 600)
            tdata = data_dict[sata]['aphelion']
            xdelt1 = tdata*N.cos(N.arcsin(ydelt/tdata))
            xdelt1 = xdelt1.tolist()
            xdelt1.reverse()
            xdelt1 = N.array(xdelt1)
            ydelt1 = ydelt.tolist()
            ydelt1.reverse()
            ydelt1 = N.array(ydelt1)
            angle = N.arctan2((ydelt1[int(points*(1.0 - lside)) + 1] - ydelt1[int(points*(1.0 - lside)) - 1]), (xdelt1[int(points*(1.0 - lside)) + 1] - xdelt1[int(points*(1.0 - lside)) - 1]))*180/N.pi
            P.text(xdelt1[int(points*(1.0 - lside))], ydelt1[int(points*(1.0 - lside))], '%s aphelion' % (data_dict[sata]['name']), fontsize = 6, color = 'gray', rotation = angle, va='center', ha='center', zorder = 600)
            P.fill(N.concatenate((xdelt, xdelt1)), N.concatenate((ydelt, ydelt1)), facecolor = clr, edgecolor = clr, linewidth=0.01)

    P.axis([xn0, xn1, yn0, yn1])
    P.yticks([], [])
    P.xticks([], [])
    return


def make_heliocentric_plots(xin, yin, figsize, (xn0, yn0, xn1, yn1), dates, box = False, border_color = False, box_color = 'black', crosshairs = False, label = "", zoom = 1):
    '''
    Makes most, if not all of the plots.
    '''
    if border_color:
        make_plot_framework(figsize, facecolor = 'black')
        tcolor = 'white'
    else:
        make_plot_framework(figsize)
        tcolor = 'gray'

    linespacing = 250000/zoom
    doffset = 1200000/zoom

    for lsat in xin:
        dmin = data_dict[data_dict[lsat]['target']]['label'] - datetime.timedelta(days = 63)
        da = []
        for index in range(23):
            da.append(dmin + datetime.timedelta(days = 7*index))
        da_color = da[0].toordinal() % 7
        for index in range(len(da) - 1):
            x_plot,y_plot,odates = data_clip(xin[lsat], xn0, xn1, yin[lsat], yn0, yn1, N.array(dates[lsat]), da[index], da[index + 1])
            if x_plot[0] == 0:
                continue
            zorder = 510
            if lsat in planets:
                zorder = 490
                if not border_color:
                    # TODO: date offset? right now inflexible
                    if box and odates[0] == data_dict[lsat]['label']:
                        P.text(x_plot[0] + (box[2] - box[0])/2 + 100000/zoom, y_plot[0] - linespacing, odates[0].date(), fontsize = 6, color = tcolor, zorder = 600)
                    else:
                        P.text(x_plot[0] + doffset, y_plot[0] - linespacing, odates[0].date(), fontsize = 6, color = tcolor, zorder = 600)
            lw = 2.0*data_dict[lsat]['radius']*km2points*zoom
            if lw < mlw:
                lw = mlw
            if border_color:
                # Not zoomed
                P.plot(x_plot, y_plot, linewidth = lw + 0.02, solid_capstyle = 'butt', linestyle = data_dict[lsat]['line_style'], color = 'black', zorder = zorder, lod = True)
            else:
                P.plot(x_plot, y_plot, linewidth = lw + 0.02, solid_capstyle = 'butt', linestyle = data_dict[lsat]['line_style'], color = 'black', zorder = zorder, lod = True)
            P.plot(x_plot, y_plot, linewidth = lw, solid_capstyle = 'butt', linestyle = data_dict[lsat]['line_style'], color = color_table[(da_color + index) % 7], zorder = zorder, lod = True)

    make_plot_final_touch(xin, (xn0, yn0, xn1, yn1), box = box, border_color = border_color, box_color = box_color, zoom = zoom, heliocentric = True)
    return (xn0, yn0, xn1, yn1)


def make_planet_centered_plots(xin, yin, figsize, (xn0, yn0, xn1, yn1), dates, box = False, border_color = False, box_color = 'black', crosshairs = False, label = "", zoom = 1):
    '''
    Makes most, if not all of the plots.
    '''
    if border_color:
        make_plot_framework(figsize, facecolor = 'black')
    else:
        make_plot_framework(figsize)

    # This clips and plots the data
    for lsat in xin:
        if lsat not in planets:
            lw = 2.0*data_dict[lsat]['radius']*km2points*zoom
            if lw < mlw:
                lw = mlw
            P.plot(xin[lsat], yin[lsat], linewidth = lw, linestyle = data_dict[lsat]['line_style'], color = 'black', zorder = 510, lod = True)

            dmin = data_dict[data_dict[lsat]['target']]['label']
            da = []
            for index in range(4):
                da.append(dmin + datetime.timedelta(hours = index))
            da_color = ['red', 'blue', 'green']
            for index in range(len(da) - 1):
                x_plot,y_plot,odates = data_clip(td[lsat][5], xn0, xn1, td[lsat][6], yn0, yn1, N.array(td[lsat][0]), da[index], da[index + 1])
                if x_plot[0] == 0:
                    continue
                P.plot(x_plot, y_plot, linewidth = lw, linestyle = data_dict[lsat]['line_style'], color = da_color[index], zorder = 511, lod = True)

    make_plot_final_touch(xin, (xn0, yn0, xn1, yn1), box = box, border_color = border_color, box_color = box_color, zoom = zoom, heliocentric = False)
    return (xn0, yn0, xn1, yn1)


def extra_axis():
    # Begin loop to create axes
    x_axis_locations = [0.075, 0.05, 0.025]
    x_axis_scale = [1.0, 1.0/au2km, 1.0/au2km*8.3167464]
    # Now set to zeros so really don't need any more.
    x_tick_start = [0, 0, 0]
    x_tick_increment = [1.0e7, 0.1, 1.0]
    x_tick_max = [7.5e9, 60.0, 480.0]
    x_label_format = ["%.1e km", "%.1f au", "%i light minutes"]
    for index in range(3):
        if page == 0:
            axes_min = -float(xoffset)/xpagescale
            x_min = -0.0001
        else:
            axes_min = 0
            x_min = x0*x_axis_scale[index]
        P.axes([axes_min, x_axis_locations[index], 1, 0.00001])
        P.axis(xmin = x_min, xmax = x1*x_axis_scale[index])
        x_tick_marks = N.arange(x_tick_start[index], x_tick_max[index], x_tick_increment[index])
        x_tick_marks = x_tick_marks[N.logical_and(x_tick_marks >= x_min, x_tick_marks < x1*x_axis_scale[index])]
        x_tick_labels = [x_label_format[index] % i for i in x_tick_marks]
        P.xticks(x_tick_marks, x_tick_labels, fontsize = 7)
        P.yticks([], [])

td = {}
label_data = {}
# This loop read the data in from the ephemeris file into x, y, and the point
# of interest labelx, labely
# Need planets handled first in order to get planet centered data.
for sat in planets + satellites + [0]:
    # sat, date, helio_x, helio_y, pl_x, pl_y, color
    # sat,       helio_label_x, helio_label_y, pl_label_x, pl_label_y, label
    date = []
    helio_x = []
    helio_y = []
    pl_x = []
    pl_y = []
    xy = orbit_plot_utils.PlotUtils()
    xy = xy.eph_open('ephemeris_helio/%.3i_%s_eph.txt.gz' % (sat, data_dict[sat]['name']))
    parent = data_dict[sat]['target']
    for rec in xy:
        date.append(rec[0])
        helio_x.append(rec[1][0])
        helio_y.append(rec[1][1])

    helio_x = N.array(helio_x)
    helio_y = N.array(helio_y)

    pl_x = N.zeros(len(helio_x))
    pl_y = N.zeros(len(helio_x))
    plx = N.zeros(len(helio_x))
    ply = N.zeros(len(helio_x))
    if sat in satellites:
        pl_x = helio_x - td[parent][1]
        pl_y = helio_y - td[parent][2]

    for index,d in enumerate(date):
        # Find label x,y
        if d == data_dict[parent]['label']:
            helio_label_x, helio_label_y = (helio_x[index], helio_y[index])
            if sat in satellites:
                pl_label_x, pl_label_y = (pl_x[index], pl_y[index])
            else:
                pl_label_x, pl_label_y = (0.0, 0.0)

    if sat in satellites:
        # The rest of the loop optimizes the set so that I have one orbit of
        # each satellite.  Basically just feeds the (x,y) into a new dictionary
        # using the int(angle) in degrees as the key.
        ang = N.arctan2(pl_y, pl_x)*180/N.pi
        ang = N.int0(ang)
    
        angle_dict = {}
        for index,angle in enumerate(ang):
            # This rather strange test to to try and get the orbit from the
            # beginning of the pl_x, pl_y.
            # This might fix the offset on the orbit of Uranus:Miranda from the
            # gray orbit to the colored hourly orbits.
            if len(angle_dict) == 359:
                break
            angle_dict[angle] = (pl_x[index], pl_y[index])

        angle_keys = angle_dict.keys()
        angle_keys.sort()

        plx = []
        ply = []
        for key in angle_keys:
            plx.append(angle_dict[key][0])
            ply.append(angle_dict[key][1])
        # Need to add the first point to close the circle
        plx.append(plx[0])
        ply.append(ply[0])

    td[sat] = [date, helio_x, helio_y, N.array(plx), N.array(ply), pl_x, pl_y]
    label_data[sat] = [helio_label_x, helio_label_y, pl_label_x, pl_label_y, str(sat)]

zoom_border_color = {100: 'green', 10: 'red'}
zoom_box_color = {100: 'black', 10: 'green', 1: 'red'}


for page in pages:
    x0 = page*xpagescale + xoffset 
    x1 = x0 + xpagescale

    print page
    box = False
    for sat in [0] + planets:
        if label_data[sat][0] > x0 and label_data[sat][0] < x1:
            satel = [i for i in data_dict if data_dict[i]['target'] == sat]
            for helio in [False, True]:

                inplx = {}
                inply = {}
                inpl_dates = {}
                inpl_label_x = []
                inpl_label_y = []
                inpl_label = []
                inhlx = {}
                inhly = {}
                for insat in satel:
                    inhlx[insat] = td[insat][1]
                    inhly[insat] = td[insat][2]
                    inplx[insat] = td[insat][3]
                    inply[insat] = td[insat][4]
                    inpl_dates[insat] = td[insat][0]
                    inpl_label_x.append(label_data[insat][2])
                    inpl_label_y.append(label_data[insat][3])
                    inpl_label.append(data_dict[insat]['label'])

                box = False
                for zoom in [100, 10]:
                    figsize = (8.0, 9.0)
                    if sat in [199, 399, 499, 999]:
                        figsize = (3.8, 11.0/2.5)
                    elif sat == 0: # Sun
                        figsize = (8.0, 11.0/2.5)
                    elif sat in [299]:
                        figsize = (2.7, 11.0/2.5)
                    dx = (x1 - x0)/8.5*figsize[0]/2/zoom
                    dy = (ymax - ymin)/11.0*figsize[1]/2/zoom
                    if helio:
                        print page, 'helio', zoom
                        xn0 = label_data[sat][0] - dx
                        xn1 = label_data[sat][0] + dx
                        yn0 = label_data[sat][1] - dy
                        yn1 = label_data[sat][1] + dy
                        if sat == 0:
                            xn0 = label_data[sat][0] - dx
                            xn1 = label_data[sat][0] + dx
                            yn0 = label_data[sat][1] - dy - data_dict[sat]['radius']
                            yn1 = label_data[sat][1] + dy - data_dict[sat]['radius']
                        box = make_heliocentric_plots(inhlx, inhly, figsize, 
                                         (xn0, yn0, xn1, yn1), inpl_dates, 
                                         box = box, 
                                         border_color = zoom_border_color[zoom],
                                         box_color = zoom_box_color[zoom], 
                                         crosshairs = ([label_data[sat][0]], 
                                                       [label_data[sat][1]],
                                                       [data_dict[sat]['label']]), 
                                         label = str(data_dict[sat]['name']), 
                                         zoom = zoom)

                        # EPS looks the best, but create PNG also for convenience
                        P.savefig('figs_eps/%s_%ix_helio_plot_page_001.eps' % (data_dict[sat]['name'].lower(), zoom))
                        P.savefig('figs_png/%s_%ix_helio_plot_page_001.png' % (data_dict[sat]['name'].lower(), zoom))
                    elif sat != 0:
                        print page, 'planet', zoom
                        xn0 = 0.0 - dx
                        xn1 = 0.0 + dx
                        yn0 = 0.0 - dy
                        yn1 = 0.0 + dy
                        box = make_planet_centered_plots(inplx, inply, figsize, 
                                         (xn0, yn0, xn1, yn1), inpl_dates, 
                                         box = box, 
                                         border_color = zoom_border_color[zoom],
                                         box_color = zoom_box_color[zoom], 
                                         crosshairs = (inpl_label_x, 
                                                       inpl_label_y,
                                                       inpl_label),
                                         label = str(data_dict[sat]['name']), 
                                         zoom = zoom)

                        P.savefig('figs_eps/%s_%ix_planet_plot_page_001.eps' % (data_dict[sat]['name'].lower(), zoom))
                        P.savefig('figs_png/%s_%ix_planet_plot_page_001.png' % (data_dict[sat]['name'].lower(), zoom))


    print page, 'full_plot'
    xp = {}
    yp = {}
    dt = {}
    for insat in td:
        if page + 1 in data_dict[insat]['pages']:
            xp[insat] = td[insat][1]
            yp[insat] = td[insat][2]
            dt[insat] = td[insat][0]

    box = make_heliocentric_plots(xp, yp, (8.5, 11), (x0, ymin, x1, ymax), dt, 
                     box = box, 
                     box_color = zoom_box_color[1], 
                     crosshairs = ([label_data[sat][0]], [label_data[sat][1]]),
                     )

    extra_axis()

    P.savefig('figs_eps/solar_system_plot_page_%.3i.eps' % (page + 1,))
    P.savefig('figs_png/solar_system_plot_page_%.3i.png' % (page + 1,))

