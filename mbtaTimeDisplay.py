__author__ = 'Terrace Boiz'


import mbtaJsonParse

#print all northbound train times
def popNorth():
    print "Northbound (Oak Grove)"
    for x in range (len(mbtaJsonParse.schedule['Northbound'])):
        if (x == 0):
            m, s = divmod(mbtaJsonParse.schedule['Northbound'][x], 60)
            print "Next Train:",
            timeHandler(m, s)
        else:
            m, s = divmod(mbtaJsonParse.schedule['Northbound'][x], 60)
            timeHandler(m, s)
    print "\n"


#Print all southbound train times
def popSouth():
    print "Southbound (Forrest Hills)"
    for x in range (len(mbtaJsonParse.schedule['Southbound'])):
        if (x == 0):
            m, s = divmod(mbtaJsonParse.schedule['Southbound'][x], 60)
            print "Next Train:",
            timeHandler(m, s)
        else:
            m, s = divmod(mbtaJsonParse.schedule['Southbound'][x], 60)
            timeHandler(m, s)
    print "\n"


#Format the arrival times
def timeHandler(m, s):
    if (m <= 1 and s <= 10):
        print "%02d:%02d (BRD)" % (m, s)
    elif (m <= 1):
        print "%02d:%02d (ARR)" % (m, s)
    else:
        print "%02d:%02d" % (m, s)