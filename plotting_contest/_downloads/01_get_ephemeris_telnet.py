#!/usr/bin/env python
'''
This script collects ephemeris data from JPL Horizons and puts it into the
sub-directory ephemeris_helio.

'''

# Be careful!  This script with the --overwrite argument can replace the
# ephemeris file(s).

import telnetlib
import urllib
import datetime
import os.path
import time
import gzip
import sys

import variables

data_dict = variables.data_dict

HOST = "horizons.jpl.nasa.gov"
PORT = 6775

mo = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

overwrite = False
try:
    if sys.argv[1] == '--overwrite':
        overwrite = True
except IndexError:
    overwrite = False

if not os.path.exists('ephemeris_helio'):
    os.mkdir('ephemeris_helio')

delta = datetime.timedelta(days=1)
tn = telnetlib.Telnet(HOST, PORT)
tn.set_debuglevel(0)

for orb in data_dict:

    orb_data = data_dict[orb]

    if os.path.exists('ephemeris_helio/%.3i_%s_eph.txt.gz' % (orb, orb_data['name'])):
        if overwrite:
            os.remove('ephemeris_helio/%.3i_%s_eph.txt.gz' % (orb, orb_data['name']))
        else:
            continue

    # Pull final_sdate and final_edate from parent planet
    final_sdate = orb_data['sdate']
    final_edate = orb_data['edate']
    interval = orb_data['interval']
    if final_sdate == None:
        final_sdate = data_dict[orb_data['target']]['sdate']
    if final_edate == None:
        final_edate = data_dict[orb_data['target']]['edate']
    if interval == None:
        interval = data_dict[orb_data['target']]['interval']

    tn.read_until("Horizons> ")
    print orb
    if orb < 10000:
        tn.write("%i\n" % orb)
    elif orb >= 10000 and orb <= 19999:
        tn.write("%i\n" % -(orb - 10000))
    else:
        tn.write("%i\n" % -orb)

    index,res,text = tn.expect(['<cr>: ', '<q> ends display. >'])
    if index == 1:
        tn.write("q")
        tn.read_until('<cr>: ')
    tn.write("E\n")
    tn.read_until("o,e,v,?] : ")
    tn.write("o\n")
    index,match,text = tn.expect(["cr=\(y\), n, \?", "geo"])  
    if index == 1:
        tn.write("@sun\n")
    elif index == 0:
        tn.write("\n")
    index,sdate,text = tn.expect(['\[.*\]'])
    tn.read_until(" : ")
    if orb < 10000:
        tn.write(final_sdate.strftime('%Y-%b-01\n'))
    else:
        sdate = sdate.group()[3:-1].strip()
        sdate = datetime.datetime(int(sdate[:4]), mo[sdate[5:8]], int(sdate[9:11])) + delta
        tn.write(sdate.strftime('%Y-%b-%d\n'))
    index,sdate,text = tn.expect(['\[.*\]'])
    tn.read_until(" : ")
    if orb < 10000:
        tn.write(final_edate.strftime('%Y-%b-01\n'))
    else:
        sdate = sdate.group()[3:-1].strip()
        sdate = datetime.datetime(int(sdate[:4]), mo[sdate[5:8]], int(sdate[9:11])) - delta
        tn.write(sdate.strftime('%Y-%b-%d\n'))
    tn.read_until(" : ")
    tn.write("%i%s\n" % (interval[0], interval[1]))
    tn.read_until(" : ")
    tn.write("n\n")
    tn.read_until(" : ")
    tn.write("18,19\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("YES\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.read_until(" : ")
    tn.write("\n")
    tn.write("q")
    tn.read_until("? : ")
    tn.write("F\n")
    index,ftpurl,text = tn.expect(['ftp://.*\n', '\? : '])
    if index == 1:
        tn.write("F\n")
        index,ftpurl,text = tn.expect(['ftp://.*\n'])
    tn.read_until(" : ")
    tn.write("N\n")
    print ftpurl.group()
    print orb_data['name']
    filename, header = urllib.urlretrieve(ftpurl.group(), 'ephemeris_helio/%.3i_%s_eph.txt' % (orb, orb_data['name']))
    f_in = open(filename, 'rb')
    f_out = gzip.open(filename + '.gz', 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    os.remove(filename)
