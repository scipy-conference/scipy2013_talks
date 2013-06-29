from math import pi, atan


def getHalfQuadrantOfCircle(x, y):
    """
    getHalfQuadrantOfCircle : return the half quadrant of the circle for the
        given x, y points. Usually we split the circle into 4 equal quadrants,
        but in this function we split circle into 8 equal parts. Thats why
        we call it as half quadrants. i.e we split one quadrant into two equal
        parts (two equal half quadrants).

    Written By : Arulalan.T

    Date : 02.04.2013
    
    License : GPL V3
    
    """

    if x == 0: x = 1
    tmp = atan(y/x)
    if (y*x > 0):
        if (x < 0): tmp += pi
    else:
        if (y > 0): tmp += pi
        if (y < 0): tmp += 2*pi
    # end of if (y*x > 0):

    if ((tmp >= 0) and (tmp < pi/4)): hq = 1
    elif (tmp < 2*pi/4): hq = 2
    elif (tmp < 3*pi/4): hq = 3
    elif (tmp < pi): hq = 4
    elif (tmp < pi+pi/4): hq = 5
    elif (tmp < pi+2*pi/4): hq = 6
    elif (tmp < pi+3*pi/4): hq = 7
    elif (tmp <= 2*pi): hq = 8
    else: hq = -1
    return hq
# end of def getHalfQuadrant(x, y):

