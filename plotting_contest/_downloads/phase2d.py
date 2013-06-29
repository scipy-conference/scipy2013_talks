"""
.. module:: phase2d
   :synopsis: A useful module for plotting 2 dimensional line diagram among
              eight phases. phase2d is a generic function to plot any model
              data and create user's own functions with customisable args.
              Also contains mjo_phase2d, miso_phase2d template functions.
.. moduleauthor:: Arulalan.T <arulalant@gmail.com>
   License : GPL V3
"""
import cdutil
from genutil import xmgrace
from timeutils import TimeUtility
import trig

timobj = TimeUtility()


def phase2d(xdata, ydata, sxyphase, dmin=None, dmax=None, colors=['red'],
            tcomment='', bcomment='', lcomment='', rcomment='',
            title='Phase Diagram', stitle1='', stitle2='', ctitle='Weak',
            pposition1=None, pdirection='anticlock', plocation='in', mintick=0):
    """
    phase2d : This will allow user to plot the 2 dimensional line plot in
              circular path among 8 phases. Also named as phase space diagram.

    Inputs:
        xdata : single dimensional xaxis dataset.
                eg : normalized pc1 time series
        ydata : single dimensional yaxis dataset.
                eg : normalized pc2 time series
                Both xdata & ydata should be continous time series dataset.

        xdata.id and ydata.id will be set as xaxis & yaxis label.

        dmin : data min - xaxis and yaxis minimum scale/label value.
               It must be -ve.
        dmin : data max - xaxis and yaxis maximum scale/label value.
               It must be +ve.
               By default both dmin, dmax takes as None. If it is None, then
               this function will automatically find out the min & max from
               the xdata & ydata. Finally set dmin = -dmax. So that we will
               get squared region.

        colors : phase line colors. It should be eithre string or list of
                 colors. If it is string or single color list, the it will
                 apply that color through out the data line in the graph.
                 If user passed it as list of colors (more than one colors)
                 then it will apply those colors to the available months data
                 set. So make sure that your colorlist and available months
                 length should be same.

        tcomment : Top Comment
        bcomment : Bottom Comment
        lcomment : Left Comment
        rcomment : Right Comment
        title : Title of the diagram
        stitle1 : Sub Title 1 - By default it will draw string as start year
                  and end year from the xdata.
        stitle2 : Sub Title 2 - By default it will draw string as season of
                  available months (from startmonth to endmonth).
                  User can overwrite the stitle1 & stitle2 strings.
        ctitle : Centred Title or text inside the circle.

        sxyphase : start x, y phase - start x,y points of xdata, ydata phase
                   number. So user can pass the phase number of the starting
                   points of the whole data (xdata, ydata). With depends upon
                   pdirection it will be draw the phase name over the 8
                   half quadrants of the graph. User no need to pass phase
                   numbers for the whole datasets (xdata, ydata). Just pass
                   the first or start day of season phase alone. User can use
                   pposition1 argument also instead of sxyphase argument.
                   No default argument takes place here. So user must pass
                   argument to this sxyphase arg. If user need to use
                   pposition1 arg, then they must pass None to this sxyphase
                   argument.

        pposition1 : phase position 1 - Lets understand the distribution of
                    8 phases. Lets consider from 0 to 45 degree region as
                    phase position 1 (pposition1).From 45 to 90 degree region
                    as phase position 2(pposition2) and so on. So if we walk
                    in anti-clock wise direction we will endup with pposition8
                    in the region of 315 to 360 degree.
                        User can pass argument to pposition1 as integer from
                    1 to 8. So whatever user passed in the pposition1 phase
                    number, that phase no string will be draw within in range
                    from 0 to 45 degree.
                       eg : pposition1=5 . i.e. phase name 'PHASE 5' will be
                            drawn in the 0 to 45 degree region of the graph.

                       By default it takes None argument.

                    ..note:: User can not use both sxyphase and pposition1
                             args. Can be used either sxyphase or pposition1
                             only.

        pdirection : phase direction - It can be either 'clock' or 'anticlock'
                     It will determine what is the phase number in the
                     pposition2, pposition3, ..., pposition8 w.r.t the input
                     of pposition1 argument or sxyphase and clock/anticlock
                     direction.
                     eg 1: pposition1 = 5, pdirection = 'anticlock'
                       pposition1=5, pposition2=6, pposition3=7, pposition4=8,
                       pposition5=1, pposition6=2, pposition7=3, pposition8=4.

                     i.e. w.r.t pposition1 as 5 and pdirection as 'anticlock'
                          the phase names of the rest phase positions are
                        determined as increment trend of pnames in ppositions.

                   eg 2: pposition1 = 5, pdirection = 'clock'
                       pposition1=5, pposition2=4, pposition3=3, pposition4=2,
                       pposition5=1, pposition6=8, pposition7=7, pposition8=6.

                     i.e. w.r.t pposition1 as 5 and pdirection as 'clock'
                          the phase names of the rest phase positions are
                        determined as decrement trend of pnames in ppositions.

                     same examples we can play with sxyphase also.

        plocation : It takes input as 'in/inside/out/outside'. If it is
                    'in' or 'inside', then the phase name/number will be drawn
                    inside the squared graph itself.
                    If it is 'out' or 'outside', then the phase name/number
                    will be drawn outside the squared graph.
        mintick : minor ticks count. By default it takes as 0. user can pass 4
                  also.

    Methods Used : _sortMonths, getTimeAxisMonths, getHalfQuadrantOfCircle

    Return :
        It should return the 'x' of the xmgrace object which has plotted the
        data with this MJO args. User can either save it into ps, pdf, etc.,
        or modify/update further.

    Author : Arulalan.T

    Date : 20.02.2013

    License : GPL V3

    """

    if sxyphase and pposition1:
        raise ValueError("pass either sxyphase or pposition1 argument.\
                                                Dont pass both args!")
    if not sxyphase and not pposition1:
        raise ValueError("You must pass either sxyphase or pposition1 argument")
    if sxyphase:
        if not isinstance(sxyphase, int):
            raise ValueError("sxyphase argument must be integer type")
        if sxyphase < 1 or sxyphase > 8:
            raise ValueError("sxyphase argument must be within 1 to 8 only!")
    elif pposition1:
        if not isinstance(pposition1, int):
            raise ValueError("pposition1 argument must be integer type")
        if pposition1 < 1 or pposition1 > 8:
            raise ValueError("pposition1 argument must be within 1 to 8 only!")

    # create our xmgrace object
    x = xmgrace.init()
    x.portrait()

    # Now let's set the area of graph 0
    x.Graph[0].vymin = .20  # starts at 55% of the page
    x.Graph[0].vymax = .75   # stops at 90% of the page
    x.Graph[0].vxmin = .15  # starts at 10% of the page
    x.Graph[0].vxmax = .90   # stops at 75% of the page

    if not (dmin and dmax):
        # user not passed the data min & data max values.
        # So what, lets find it !
        xmin, xmax = min(xdata), max(xdata)
        ymin, ymax = min(ydata), max(ydata)
        dmin = min([xmin, ymin])
        dmax = max([xmax, ymax])
        if abs(dmin) == abs(dmax):
            dmax = round(dmax) + 1
        else:
            dmax = round(max([abs(dmin), abs(dmax)])) + 1
        # end of if abs(umin) == abs(umax):
        dmin = -dmax
    # end of if not (min and max):

    # ok now let's set the min ans max for the Y axis
    x.Graph[0].yaxis.min = dmin  # ymin for graph 0
    x.Graph[0].yaxis.max = dmax  # ymax for graph 0

    # Now let's set the tick marks for Graph 0
    x.Graph[0].yaxis.tick.inc = 1   # Main tick every unit
    x.Graph[0].yaxis.tick.minor_ticks = mintick

    # ok now let's set the min ans max for the X axis
    x.Graph[0].xaxis.min = dmin  # xmin for graph 0
    x.Graph[0].xaxis.max = dmax  # xmax for graph 0

    # Now let's set the tick marks for Graph 0
    x.Graph[0].xaxis.tick.inc = 1  # Main tick every unit
    x.Graph[0].xaxis.tick.minor_ticks = mintick

    for setno in range(4):
        if setno != 0:
            # adding set to graph 0 to add lines
            x.add_set(graph=0)
        # end of if setno != 0:
        # First let's set the line width, style, color
        x.Graph[0].Set[setno].line.linewidth = 1
        x.Graph[0].Set[setno].line.color = 'black'
        x.Graph[0].Set[setno].line.linestyle = 'solid'
    # end of for setno in range(4):

    # line co-ordinates points
    p1 = [0, 0]
    p2 = [dmin, dmax]
    p3 = [dmax, dmin]
    # line x, y co-ordinates
    lines1 = [p1, p2, p2, p2]
    lines2 = [p2, p1, p2, p3]
    # plotting + and x cross lines to connect all the corners of the graph.
    x.plot(lines1, xs=lines2)

    # adding set to graph 0 to add the centred circle
    csetno = setno + 1
    x.add_set(graph=0)
    # set centred circle properties
    x.Graph[0].Set[csetno].symbol.type = 1
    # circle should follow its path on these conditions/points
    # (x=1, y=0),(x=-1, y=0),(x=0,y=1),(x=0,y=-1).
    # We set size of the circle according to the above rules!
    x.Graph[0].Set[csetno].symbol.size = 9.175
    x.Graph[0].Set[csetno].symbol.color = 'black'
    x.Graph[0].Set[csetno].symbol.fcolor = 'white'
    x.Graph[0].Set[csetno].symbol.linestyle = 1
    x.Graph[0].Set[csetno].symbol.linewidth = 1
    # plotting the centred circle
    x.plot([[0]], G=0, S=csetno)

    # to point the starting day of event, set its x, y, color properties
    start_x = 0
    start_y = 0
    start_clr = 'red'

    # plot type
    if isinstance(colors, str):
        ptype = 'single'
        start_clr = colors
    elif (isinstance(colors, (list, tuple)) and len(colors) == 1):
        ptype = 'single'
        start_clr = colors[0]
    elif len(colors) > 1:
        ptype = 'multi'
        avlColors = colors
    # end of if isinstance(colors, str):

    if ptype == 'single':
        csetno = csetno + 1
        x.add_set(graph=0)
        # set the line properties color & inter points color, size
        x.Graph[0].Set[csetno].line.linewidth = 1
        x.Graph[0].Set[csetno].line.color = start_clr
        x.Graph[0].Set[csetno].line.linestyle = 'solid'
        x.Graph[0].Set[csetno].symbol.type = 1
        x.Graph[0].Set[csetno].symbol.size = 0.125
        x.Graph[0].Set[csetno].symbol.color = start_clr
        # plotting the xdata, ydata in circle manner
        x.plot(ydata, xs=xdata, G=0, S=csetno)
        # to point the starting day of event by filled color square symbol
        # set its start_x, start_y
        start_x = xdata[0]
        start_y = ydata[0]

    elif ptype == 'multi':
        # available months in dictionary format contains years, month string
        # and dates
        xtimeAxis = xdata.getTime()
        ytimeAxis = ydata.getTime()
        if xtimeAxis[:].tolist() != ytimeAxis[:].tolist():
            raise ValueError("xdata (%s), ydata (%s) time axis are not same!"
                                                     % (xdata.id, ydata.id))
        # end of if xtimeAxis[:].tolist() != ytimeAxis[:].tolist():
        cdutil.setAxisTimeBoundsDaily(xtimeAxis)
        avlMonths = timobj.getTimeAxisMonths(xtimeAxis)
        avlMonthsList = []

        for year in avlMonths:
            months = avlMonths[year].keys()
            # sort the month string
            months = timobj._sortMonths(months)
            for mon in months:
                avlMonthsList.append((mon, avlMonths[year][mon]))
            # end of for mon in months:
        # end of for year in avlMonths:

        # innter lock connection months
        conMonths = []
        # now lets do innter lock connection between months last & first date
        preMonthLastDate = None
        for idx, (mon, (fdate, ldate)) in enumerate(avlMonthsList):
            if idx == 0:
                conMonths.append((mon, (fdate, ldate)))
            else:
                # previous month's last date as first day of this month &
                # this month last date for the purpose of continous line plot
                # while changing colors for different months.
                conMonths.append((mon, (preMonthLastDate, ldate)))
            # end of if idx == 0:
            preMonthLastDate = ldate
        # end of for idx, fdate, ldate in enumerate(avlMonthsList):
        # make memory free
        del avlMonths, avlMonthsList

        # month string x position to indicate below the graph with
        # corresponding line color
        monx = 0.4
        for montime, colr in zip(conMonths, avlColors):
            # get the month name string
            mon = montime[0]
            # month first last component time object date
            monFLDate = montime[1]
            # get the current month pc1 and pc2 data
            pc1 = xdata(time=monFLDate)
            pc2 = ydata(time=monFLDate)
            if monx == 0.4:
                # do it only one time, assign the first day of first month to
                # start_x, start_y, color to point the starting day of event
                # by filled color square symbol
                start_x = pc1[0]
                start_y = pc2[0]
                # set the starting color as begining of multi color list
                start_clr = colr
            # end of if monx == 0.4:
            csetno = csetno + 1
            x.add_set(graph=0)
            # set the line properties color & inter points color, size
            # for this month dataset
            x.Graph[0].Set[csetno].line.linewidth = 1
            x.Graph[0].Set[csetno].line.color = colr
            x.Graph[0].Set[csetno].line.linestyle = 'solid'
            x.Graph[0].Set[csetno].symbol.type = 1
            x.Graph[0].Set[csetno].symbol.size = 0.125
            x.Graph[0].Set[csetno].symbol.color = colr
            # plotting the xdata, ydata in circle manner
            x.plot(pc2, xs=pc1, G=0, S=csetno)
            # darw the month string with same as color of that month line
            # color to indicate monthly event
            x.add_string(monx, 0.09, mon[:3], color=colr,
                            char_size=0.6, rot=0, just=14)
            # increment the month string position
            monx += 0.05
        # end of for mon, colr in zip(conMonths, avlColors):
    else:
        raise ValueError("Wrong plot '%s' type has passed. \
                          Pass either 'single' or 'multi'" % ptype)
    # end of if ptype == 'single':

    # adding set to draw a small square symbol at the begining of the season.
    # it must be square symbol only. Becuause we can not plot this symbol
    # out side of the graph, using viewport.
    csetno = csetno + 1
    x.add_set(graph=0)
    x.Graph[0].Set[csetno].symbol.type = 2  # 'square' type
    x.Graph[0].Set[csetno].symbol.size = 0.45
    x.Graph[0].Set[csetno].symbol.color = start_clr
    x.Graph[0].Set[csetno].symbol.fcolor = start_clr
    x.plot([[start_y]], [[start_x]], G=0, S=csetno)

    # Since we can not use viewport to plot the symbol to indicate what the
    # above square symbol meant to be, here we are using add_box function to
    # draw a small square below the graph with text 'Start day of season'.
    x.add_box(0.75, 0.158, 0.758, 0.164, color=start_clr, fillcolor=start_clr)
    # drawing the text behind to the above small square box
    x.add_string(0.83, 0.16, 'Start day of season', color='black',
                                    char_size=0.6, rot=0, just=14)
    # draw the xdata id as xaxis label
    x.add_string(0.53, 0.16, xdata.id, color='black', char_size=0.7,
                                                     rot=0, just=14)
    # draw the ydata id as yaxis label
    x.add_string(0.10, 0.48, ydata.id, color='black', char_size=0.7,
                                                    rot=90, just=14)
    # draw the bottom comment
    x.add_string(0.53, 0.13, bcomment, color='blue', char_size=1.3,
                                                     rot=0, just=14)
    # draw the top comment
    x.add_string(0.53, 0.81, tcomment, color='blue', char_size=1.3,
                                                     rot=0, just=14)
    # draw the left comment
    x.add_string(0.06, 0.48, lcomment, color='blue', char_size=1.3,
                                                    rot=90, just=14)
    # draw the right comment
    x.add_string(0.97, 0.48, rcomment, color='blue', char_size=1.3,
                                                   rot=270, just=14)

    # phase quadrant/positions no, and its x, y coordinate points to draw
    # phase name inside the graph
    phases_loc_in = ((1, (2.5, 1)), (2, (1, 3.5)), (3, (-2, 3.5)),
                  (4, (-3.5, 1)), (5, (-3.5, -1)), (6, (-2, -3.5)),
                  (7, (1, -3.5)), (8, (2.5, -1)))
    # phase quadrant/positions no, its x, y coordinate points to draw
    # phase name and its rotation(direction) outside the graph
    phases_loc_out = ((1, (4.25, 2.5), 270), (2, (1, 4.25), 0),
        (3, (-2, 4.25), 0), (4, (-4.5, 1.5), 90), (5, (-4.5, -2.5), 90),
        (6, (-2, -4.65), 0), (7, (1, -4.65), 0), (8, (4.25, -1.5), 270))

    # general phase sequence
    phase_sequence = range(1, 9)

    if sxyphase:
        # passed start x, y points of xdata, ydata phase name/number.
        # assign the above phase name/number of start x, y points
        # of xdata, ydata
        pos = sxyphase
        # get the actual half quadrant of the circle of the start x, y points
        # of xdata, ydata. subtract 1 for python index access of list.
        hq = trig.getHalfQuadrantOfCircle(start_x, start_y) - 1
        # reorder the phase_sequence w.r.t starting x,y points of xdata,ydata
        phase_sequence = phase_sequence[hq:] + phase_sequence[:hq]
    elif pposition1:
        # passed phase name/number of pposition1 or first positive half
        # quadrant of the circle region phase name/number
        # assign the first position phase number as passed by user arg
        pos = pposition1
    # end of if sxyphase:

    phases_name = {}
    if pdirection in ['clock', 1]:
        # for clock wise phase increment should be -ve w.r.t phase positions
        inc = -1
    elif pdirection in ['aclock', 'anticlock', -1]:
        # for anti-clock wise phase increment should be +ve w.r.t
        # phase positions
        inc = 1
    else:
        raise ValueError("Wrong pdirection '%s' has passed.\
                pass either 'clock' or 'anticlock'" % pdirection)
    # end of if pdirection in ['clock', 1]:

    # loop through phase positions from 1 to 8.
    for phase_position in phase_sequence:
        # assign the phase name to the corresponding phase position as per
        # user input for the pposition1.
        phases_name[phase_position] = 'PHASE ' + str(pos)
        # if phase name is reached 8, then next phase name should be 1 in
        # case of anticlock wise direction. inc will take care of the below
        # pos = 0 to convert pos = 1.
        if pos == 8 and inc == 1: pos = 0
        # if phase name is reached 1, then next phase name should be 8 in
        # case of clock wise direction. inc will take care of the below
        # pos = 9 to convert pos = 8.
        if pos == 1 and inc == -1: pos = 9
        # either increment or decrement w.r.t clock/anticlock wise direction
        pos += inc
    # end of for phase_position in phase_sequence:

    # draw strings/names of 8 phases inside/outside of the graph
    if plocation in ['in', 'inside']:
        for (idx, (px, py)) in phases_loc_in:
            pname = phases_name[idx]
            # to plot the string w.r.t some x, y position justification
            # must be 0 and location type must be world.
            x.add_string(px, py, pname, color='black',
                         char_size=0.8, rot=0, just=0)
            # make the loctype as world to recently added string
            # (i.e. the above string added)
            x.String[-1].loctype = 'world'
        # end of for (idx, (px, py)) in phases_loc:
    elif plocation in ['out', 'outside']:
        for (idx, (px, py), r) in phases_loc_out:
            pname = phases_name[idx]
            # to plot the string outside with rotation
            x.add_string(px, py, pname, color='black',
                         char_size=0.8, rot=r, just=0)
            x.String[-1].loctype = 'world'
        # end of for (idx, (px, py), r) in phases_loc_out:
    else:
        raise ValueError("Wrong plocation '%s' has passed.\
                    pass either 'in' or 'out'" % plocation)
    # end of if plocation in ['in', 'inside']:

    # set the subtitle1 as year if user not passed
    st1x = 0.76
    if not stitle1:
        if ptype == 'single':
            taxis = xdata.getTime().asComponentTime()
            syear, eyear = taxis[0].year, taxis[-1].year
            # make memory free
            del taxis
        elif ptype == 'multi':
            syear, eyear = conMonths[0][1][0].year, conMonths[-1][1][0].year
        # end of if ptype == 'single':
        stitle1 = 'Year : %d' % syear
        if syear < eyear:
            stitle1 += ' to %d' % eyear
            st1x = 0.795
    # end of if not stitle1:

    # set the subtitle2 as season months if user not passed
    if not stitle2:
        if ptype == 'single':
            taxis = xdata.getTime().asComponentTime()
            smon = cdutil.getMonthString(taxis[0].month)
            emon = cdutil.getMonthString(taxis[-1].month)
            # make memory free
            del taxis
            stitle2 = 'Season : %s to %s' % (smon.capitalize()[:3],
                                             emon.capitalize()[:3])
        elif ptype == 'multi':
            stitle2 = 'Season : %s to %s' % (conMonths[0][0].capitalize()[:3],
                                         conMonths[-1][0].capitalize()[:3])
    # end of if not stitle2:
    # draw the title, subtitle1 and subtitle2
    x.add_string(0.52, 0.9, title, color='black', char_size=1.5, rot=0, just=14)
    x.add_string(st1x, 0.86, stitle1, color='black', char_size=0.8, rot=0, just=14)
    x.add_string(0.8, 0.84, stitle2, color='black', char_size=0.8, rot=0, just=14)
    # draw the centred title / circle title
    x.add_string(0, 0, ctitle, color='black', char_size=0.8, rot=0, just=14)
    x.String[-1].loctype = 'world'
    # update the x to plot all the strings
    x.update()
    return x
# end of def phase2d(xdata, ydata, ...):


def mjo_phase2d(npc1, npc2, sxyphase=None, dmin=0, dmax=0,
        colors=['magenta', 'blue', 'violet', 'green', 'orange', 'red'],
        tcomment='Western Pacific', bcomment='Indian Ocean',
        lcomment='Western Hemisphere & Africa',
        rcomment='Maritime Continent', title='MJO Phase diagram of PC-1 and PC-2',
        stitle1='', stitle2='',
        ctitle='Weak MJO', pposition1=5, pdirection='anticlock',
        plocation='in', mintick=0):
    """
    mjo_phase2d : Madden-Julian Oscillation Phase 2 Dimensional Diagram

    Inputs :
        npc1 : Normalized PC1 (xdata)
        npc2 : Normalized PC2 (ydata)
        sxyphase : phase number of start x,y points of npc1, npc2. By default
                   it takes None. For the simplicity to the user, passed the
                   default/correct argument to the pposition1 as 5.
        pposition1 : phase number of the phase position1 of the graph. For the
                     MJO it must be 5. User can over write the sxyphase and
                     pposition1 args while calling this function, if needed.
        pdirection : By default it takes 'anticlock' to this MJO.
        plocation : Phase name/string drawn inside/outside of the graph. By
                    default it takes 'in'.
        colors : list contains 6 colors to indicate 6 months dataset. User
                 can overwrite it either by single or many color.
    Return :
        It should return the 'x' of the xmgrace object which has plotted the
        data with this MJO args. User can either save it into ps, pdf, etc.,
        or modify/update further.

    Refer : phase2d() for the detailed documents of all the arguments.
    
    Plot Properties Reference :
                    http://climate.snu.ac.kr/mjo_diagnostics/index.htm
                    
    Author : Arulalan.T

    Date : 20.02.2013

    License : GPL V3
    
    """

    return phase2d(npc1, npc2, sxyphase, dmin, dmax, colors, tcomment,
                   bcomment, lcomment, rcomment, title, stitle1, stitle2,
                   ctitle, pposition1, pdirection, plocation, mintick)
# end of mjo_phase2d(npc1, npc2, ...):


def miso_phase2d(xdata, ydata, sxyphase=None, dmin=None, dmax=None,
        colors=['violet', 'green', 'orange', 'red'],
        tcomment='Centre India & North India', bcomment='Southern tp & IO',
        lcomment='Peninsular & Centre India', rcomment='FootHill & SIO',
        title='Indian Monsoon Intraseasonal Oscillation Index',
        stitle1='', stitle2='', ctitle='Weak MISO',
        pposition1=8, pdirection='clock', plocation='out', mintick=4):
    """
    miso_phase2d : Monsoon Intraseasonal Oscillation Phase 2 Dimensional
                   Diagram
    Inputs :
        xdata : Normalized PC1 or relevant data
        ydata : Normalized PC2 or relevant data
        sxyphase : phase number of start x,y points of npc1, npc2. By default
                   it takes None. For the simplicity to the user, passed the
                   default/correct argument to the pposition1 as 8.
        pposition1 : phase number of the phase position1 of the graph. For the
                     MJO it must be 8. User can over write the sxyphase and
                     pposition1 args while calling this function, if needed.
        pdirection : By default it takes 'clock' to this MJO.
        plocation : Phase name/string drawn inside/outside of the graph. By
                    default it takes 'in'.
        colors : list contains 6 colors to indicate 6 months dataset. User
                 can overwrite it either by single or many color.
    Return :
        It should return the 'x' of the xmgrace object which has plotted the
        data with this MJO args. User can either save it into ps, pdf, etc.,
        or modify/update further.

    Refer : phase2d() for the detailed documents of all the arguments.
    
    Plot Properties Reference : "An Indian monsoon intraseasonal oscillations
         (MISO) index for real time monitoring and forecast verification",
         E. Suhas • J. M. Neena • B. N. Goswami, Clim Dyn, 
         DOI 10.1007/s00382-012-1462-5
    
    Author : Arulalan.T

    Date : 20.02.2013

    License : GPL V3

    """

    return phase2d(xdata, ydata, sxyphase, dmin, dmax, colors, tcomment,
                   bcomment, lcomment, rcomment, title, stitle1, stitle2,
                   ctitle, pposition1, pdirection, plocation, mintick)
# end of miso_phase2d(npc1, npc2, ...):


