"""
.. module:: timeutils
   :synopsis: A useful module for cdtime.comptime conversion to timestr,
              moveTime, tRange, xtRange, cdtime.timeAxis and more ...
.. moduleauthor:: Arulalan.T <arulalant@gmail.com>
   License : GPL V3
"""
import re
import cdms2
import cdutil
import cdtime


class _TimeUtilityError(Exception):

    def __init__(self, *args):
        print "\nDaysError Error : "
        for i in args:
            print i


class _TimeUtilityStringError(_TimeUtilityError):
    pass


class _TimeUtilityIntegerError(_TimeUtilityError):
    pass


class _TimeUtilityTypeError(_TimeUtilityError):
    pass


class _TimeUtilityInputError(_TimeUtilityError):
    pass


class TimeUtility():

    def __init__(self):

        self.timeAxis = None
        # set cdtime.comptime pattern regular expression object
        self.comppattern = re.compile(r"""
                                ([0-9]{1,4})          # YYYY formate (1 to 4
                                                      # digits of year accept)
                                -                     # ifen - seperator
                                ([01]?[0-9])          # MM formate
                                -                     # ifen - seperator
                                ([0123]?[0-9])        # DD formate
                                (\s{1}                # space seperator
                                ([012]?[0-9])         # hh formate
                                :?                    # colon : seperator
                                ([012345]?[0-9])?     # mm formate
                                :?                    # colon : seperator
                                ([012345]?[0-9])?     # ss formate (Sec)
                                .?                    # dot seperator
                                ([0-9]))?             # ss formate (millisec)
                                $                     # End of input
                                # hh:mm:ss.ss all are optional one by suffix ?
                                """, re.VERBOSE)

        # set yyyymmddhh pattern regular expression object
        self.ymdpattern = re.compile(r"""
                               (\d{4})                 # YYYY formate
                               ([01][1-9])             # MM formate
                               ([0123][0-9])           # DD formate
                               ([01][0-9]|[2][0-3])?   # HH formate (optional)
                               $                       # End of input
                               """, re.VERBOSE)
    # end of def __init__(self):

    def timestr2comp(self, date):
        """
        :func:`timestr2comp`: To convert date from yyyymmdd[hh] formate into
                          cdtime.comptime formate
        Condition :
                passing date must be yyyymmdd formate in either int or str
        Inputs:
                date in yyyymmdd formate or yyyymmddhh formate.
                i.e. hour(hh) is optional.
        Outputs:
                It should return the date in cdtime.comptime object type
        Usage:
            example1:
                >>> timestr2comp(20110423)
                2011-4-23 0:0:0.0
                  .. note:: It should return as cdtime.comptype. Here we didnt
                            pass the hour. i.e only yyyymmdd formate
            example2:
                >>> timestr2comp(2011082010)
                2011-8-20 10:0:0.0
                  ..note:: Here it should return cdtime with hours also.
                           We passed yyyymmddhh formate. i.e include hh
            example3:
                >>> timestr2comp(2011082023)
                2011-8-20 23:0:0.0
                  ..note:: we cannot pass 24 as hour here. Max 23 hours only.

        Written by: Arulalan.T

        Date: 23.04.2011
        Updated : 21.08.2011

        """
        if str(type(date)) == "<type 'comptime'>":
            # passed date itself comptime object only
            return date
        if isinstance(date, int):
            date = str(date)
        # re match
        if self.comppattern.match(date):
            # i.e. date is comptime in string formate
            # so make it as comptime object
            return cdtime.s2c(date)

        if self.ymdpattern.match(date):
            # i.e date is yyyymmdd string formate
            year = int(date[0:4])
            month = int(date[4:6])
            day = int(date[6:8])
            if len(date) == 10:
                hour = int(date[-2:])
                return cdtime.comptime(year, month, day, hour)
            else:
                return cdtime.comptime(year, month, day)
        else:
            raise _TimeUtilityStringError('The given date either comptime \
                         object or comptime string or yyyymmdd formate only')
    # end of def timestr2comp(self, date):

    def comp2timestr(self, comptime, returnHour='y'):
        """
        :func:`comp2timestr`: To convert date from cdtime.comptime into
                                'yyyymmdd' formate or 'yyyymmddhh' formate
                                as string

        Condition :   passing date must be comptime formate

        Inputs :    date in comptime.
                    returnHour takes 'y' or 'yes' or 'n' or 'no'.
                    Default it takes 'y'.

        Outputs : It should return the date in 'yyyymmddhh' string formate, if
                  returnHour passed 'y' or 'yes'.
                  It should return the date in 'yyyymmdd' string formate, if
                  returnHour passed 'n' or 'no'.

        Usage :
          example1 :
             >>> compobj = cdtime.comptime(2010,4,29) -> 2010-4-29 0:0:0.0
             >>> comp2timestr(compobj)
             >>> '2010042900'
           .. note:: It should return in yyyymmddhh string formate by default.
                     Hour is 00.

          example2 :
             >>> compobj = cdtime.comptime(2010,4,29,10) -> 2010-4-29 10:0:0.0
             >>> comp2timestr(compobj)
             >>> '2010042910'
           .. note:: It should return in yyyymmddhh string formate by default.
                     Hour is 10.

          example2 :
             >>> compobj = cdtime.comptime(2010,4,29,10) -> 2010-4-29 10:0:0.0
             >>> comp2timestr(compobj, returnHour = 'n')
             >>> '20100429'
           .. note:: It should return in yyyymmdd string formate only even
                     though hour passed in the component object. Because we
                     passed returnHour as 'n'.

        Written by : Arulalan.T

        Date : 29.04.2011
        Updated : 21.08.2011

        """

        if str(type(comptime)) == "<type 'comptime'>":
            # convert comptime into yyyymmdd
            yyyymmdd = str(int(comptime.absvalue))
        if isinstance(comptime, str):
            # if comptime is string
            if self.comppattern.match(comptime):
                comptime = cdtime.s2c(comptime)
                yyyymmdd = str(int(comptime.absvalue))
            else:
                raise _TimeUtilityTypeError("passed date is not \
                              cdtime.comptime object or its string formate")
        if returnHour in ['y', 'yes']:
            hh = str(comptime.hour)
            if len(hh) == 1:
                # make h as hh formate
                hh = '0' + hh
            return yyyymmdd + hh
        elif returnHour in ['n', 'no']:
            return yyyymmdd
        else:
            raise _TimeUtilityTypeError("returnHour takes either 'y/yes' \
                                                    or 'n/no' option only")
        # end of def comp2timestr(self, comptime):

    def _sortMonths(self, months):
        """
        :func:`_sortMonths`: Sorting the months and seasons with respect to
                             the calendar.

        Inputs : months is list which contains the combinations of months name
                 and seasons name.

        Outputs : It should return the list which contains the sorted months
                  first and then followed by seasons.

        Usage :

            example 1:
                >>> x = ['JANUARY', 'august', 'November', 'mar']
                >>> _sortMonths(x)
                ['JANUARY', 'mar', 'august', 'November']

            example 2:
                >>> x = ['DJF', 'JJAS']
                >>> t._sortMonths(x)
                ['JJAS', 'DJF']

            example 3:
                >>> x = ['DJF', 'december', 'March', 'JJAS', 'Nov']
                >>> _sortMonths(x)
                ['March', 'Nov', 'december', 'JJAS', 'DJF']

             ..note::  Here we passed various type of month string types.
                       i.e. Here case is in-senstive. Even we mixed the months
                       and seasons, it should be arranged the sorted months
                       and then sorted seasons.

        Written By : Arulalan.T

        Date : 03.12.2011

        """
        Months = {}
        Seasons = {}
        sortedMonths = []

        for mon in months:
            index = cdutil.getMonthIndex(mon)
            if len(index) > 1:
                # Got Season
                Seasons[index[0]] = mon
            else:
                # Got Month
                Months[index[0]] = mon
        # Sort the month and append to the list
        mkeys = Months.keys()
        mkeys.sort()
        for monidx in mkeys:
            sortedMonths.append(Months.get(monidx))
        # Sort the season and append to the list
        skeys = Seasons.keys()
        skeys.sort()
        for seaidx in skeys:
            sortedMonths.append(Seasons.get(seaidx))
        return sortedMonths
    # end of def sortMonths(self, months):

    def getTimeAxisMonths(self, timeAxis, returnType='c', returnHour='y'):
        """
        :func:`getTimeAxisMonths`: Get the available months name and its
                             firstday & lastday from the passed timeAxis.

        Condition : timeAxis must be an instance of cdms2.axis.TransientAxis

        Inputs : Pass the any range of timeAxis object.
                 returnType is either 'c' or 's'. If 'c' means the dates are
                 cdtime.comptime object itself. if 's' means the dates are
                 yyyymmddhh string (by default) or yyyymmdd w.r.t returnHour.
                 returnHour takes either 'y/yes' or 'n/no'.

        Outputs : It should return a dictionary which has key as the year.
                  This year key has the value as dictionary type itself.
                  The nested dictionary has month as key and
                  value as tuple, which contains the stardate and enddate of
                  that month.
                  It should return month only for the available months in the
                  passed timeAxis.

        Usage :
            ..seealso:: we can pass any range of timeAxis. Even its hourly
                        series, it should works.
        ..seealso:: getTimeAxisFullMonths(), getTimeAxisPartialMonths()

            example 1:
                >>> tim = _generateTimeAxis(70, '2011-5-25')
                >>> tim
                   id: time
                   Designated a time axis.
                   units:  days since 2011-5-25
                   Length: 70
                   First:  0
                   Last:   69
                   Other axis attributes:
                      calendar: gregorian
                      axis: T
                   Python id:  0x8aea74c

                >>> getTimeAxisMonths(tim)
                {2011: {
                'MAY': (2011-5-25 0:0:0.0, 2011-5-31 0:0:0.0),
                'JUNE': (2011-6-1 0:0:0.0, 2011-6-30 0:0:0.0),
                'JULY': (2011-7-1 0:0:0.0, 2011-7-31 0:0:0.0),
                'AUGUST': (2011-8-1 :0:0.0, 2011-8-2 0:0:0.0)}
                }

             ..note::  Here 2011 as the key for the primary dictionary.
                       And MAY, JUNE, JULY and AUGUST are the keys for the
                       secondary(inner) dictionary, which contains the
                       stardate and enddate of that month and year.

                >>> tim.asComponentTime()[0]
                2011-5-25 0:0:0.0
             ..note:: The actual firstdate of the timeAxis is 25th may 2011.
                      But its not complete month. Even though it is returning
                      that available may month startdate and its enddate.

                >>> tim.asComponentTime()[-1]
                2011-8-2 0:0:0.0
             ..note:: The actual lastdate of the timeAxis is 2nd aug 2011.
                      But its not complete month. Even though it is returning
                      that available may month startdate and its enddate.

             ..note:: It also returnning the fully available months, in this
                      example June & July.

            example 2:
                >>> tim1 = _generateTimeAxis(70, '2011-12-1')
                >>> tim1
                   id: time
                   Designated a time axis.
                   units:  days since 2011-12-1
                   Length: 70
                   First:  0
                   Last:   69
                   Other axis attributes:
                      calendar: gregorian
                      axis: T
                   Python id:  0xa2c10ac

                >>> getTimeAxisMonths(tim1, returnType = 's',
                                             returnHour = 'n')
                {2011: {'DECEMBER': ('20111201', '20111231')},
                 2012: {'JANUARY': ('20120101', '20120131')}}

              ..note:: In this example, we will get 2011 and 2012 are the
                       keys of the primary dictionary. And 2011 has 'DECEMBER'
                       month and its startdate & enddate as key and value.
                       Same as for 2012 has 'JANUARY' month and its startdate
                       & enddate as key and value. Here dates are in yyyymmdd
                       string formate. Here we passed returnHour as 'n'.

        Written By : Arulalan.T

        Date : 06.03.2013

        """
        if not (isinstance(timeAxis, cdms2.axis.TransientAxis) or
                isinstance(timeAxis, cdms2.axis.FileAxis) or
                isinstance(timeAxis, cdms2.axis.Axis)):
            raise _TimeUtilityTypeError("Passed timeAxis is not the type of \
                                cdms2.axis.Axis or cdms2.axis.TransientAxis")
        if not returnType in ['c', 's']:
            raise _TimeUtilityTypeError("returnType either should 's' or 'c'.\
                if 's' means the return date should be in string type. \
               if 'c' means the return date should be cdtime type itself")
        if not returnHour in ['y', 'yes', 'n', 'no']:
            raise _TimeUtilityInputError("returnHour must be 'y/n' only")
        availableMonths = {}
        # store the timeAxis as component time objects in list
        timeAxisCompTime = timeAxis.asComponentTime()
        for month in range(1, 13):
            # Doing the find process for all the 12 months
            # getting the month string
            month = cdutil.getMonthString(month)
            # slice the timeaxis based on month
            monthlist = cdutil.monthBasedSlicer(timeAxis, month)
            if monthlist[0]:
                # day are available in this month. i.e. not empty month
                # get the first and last index of the month in timeAxis
                for n in range(0, len(monthlist[0])):
                    # this loop is for big scale timeAxis
                    monthFirstIndex = monthlist[0][n][0]
                    monthLastIndex = monthlist[0][n][-1]
                   # get the first and last date of month from the timeAxis
                    # as component time object.
                    monthFirstTime = timeAxisCompTime[monthFirstIndex]
                    monthLastTime = timeAxisCompTime[monthLastIndex]
                    # get the year
                    year = monthFirstTime.year

                    if returnType == 's':
                        # get the stardate & enddate as string
                        monthFirstTime = self.comp2timestr(monthFirstTime,
                                                          returnHour)
                        monthLastTime = self.comp2timestr(monthLastTime,
                                                          returnHour)
                    # end of if returnType == 's':
                    monthTimeRange = (monthFirstTime, monthLastTime)

                    if year in availableMonths:
                        availableMonths[year][month] = monthTimeRange
                    else:
                        availableMonths[year] = {month: monthTimeRange}
                    # end of if year in availableMonths:
                # end of for n in range(0, len(monthlist[0])):
            else:
                # days are not available in this month, in the passed timeAxis
                continue
            # end of if monthlist[0]:
        # end of for month in range(1, 13):
        # make memory free
        del timeAxisCompTime
        # return the fully available months of the timeAxis
        return availableMonths
    # end of def getTimeAxisMonths(self, timeAxis, ...):
# end of class TimeUtility():

