__author__ = 'Terrace Boiz'


import mbtaJsonParse

#print all northbound train times
def popNorth():
    print "Roxbury Northbound (Oak Grove)"
    for x in range (len(mbtaJsonParse.schedule['Northbound'])):
        if (x == 0):
            print "Next Train:",
            m, s = secsToMins(mbtaJsonParse.schedule['Northbound'][x])
            timeHandler(m, s)
        else:
            m, s = secsToMins(mbtaJsonParse.schedule['Northbound'][x])
            timeHandler(m, s)
    print "\n"


#Print all southbound train times
def popSouth():
    print "Roxbury Southbound (Forrest Hills)"
    for x in range (len(mbtaJsonParse.schedule['Southbound'])):
        if (x == 0):
            print "Next Train:",
            m, s = secsToMins(mbtaJsonParse.schedule['Southbound'][x])
            timeHandler(m, s)
        else:
            m, s = secsToMins(mbtaJsonParse.schedule['Southbound'][x])
            timeHandler(m, s)
    print "\n"


#Convert seconds into minutes and seconds
def secsToMins(seconds):
    m, s = divmod(seconds, 60)
    return (m, s)


#Format the arrival times
def timeHandler(m, s):
    if (m <= 1 and s <= 10):
        print "%02d:%02d (BRD)" % (m, s)
    elif (m <= 1):
        print "%02d:%02d (ARR)" % (m, s)
    else:
        print "%02d:%02d" % (m, s)