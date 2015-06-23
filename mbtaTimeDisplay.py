__author__ = 'Terrace Boiz'


import mbtaJsonParse

#print all northbound train times
def popNorth(dict, station='Roxbury Crossing'):
    result = station + " - Northbound " + "\n"
    for x in range (len(dict['Northbound'])):
        if (x == 0):
            result += "Next Train: "
            m, s = secsToMins(dict['Northbound'][x])
            result = timeHandler(m, s) + "\n"
        else:
            m, s = secsToMins(dict['Northbound'][x])
            result = timeHandler(m, s) + "\n"
    print result
    return result


#Print all southbound train times
def popSouth(dict, station='Roxbury Crossing'):
    result = station + " - Southbound " + "\n"
    for x in range (len(dict['Southbound'])):
        if (x == 0):
            result += "Next Train: "
            m, s = secsToMins(dict['Southbound'][x])
            result += timeHandler(m, s) + "\n"
        else:
            m, s = secsToMins(dict['Southbound'][x])
            result += timeHandler(m, s) + "\n"
    print result
    return result

def panelTrain(dict, station='Roxbury'):
    m1, s1 = secsToMins(dict['Northbound'][0])
    m2, s2 = secsToMins(dict['Northbound'][1])
    result1, color1 = timeHandler(m1,s1, True)
    result2, color2 = timeHandler(m2,s2, True)
    return result1, color1, result2, color2


#Convert seconds into minutes and seconds
def secsToMins(seconds):
    m, s = divmod(seconds, 60)
    return (m, s)

#Format the arrival times
def timeHandler(m, s, panel=False):
    if (panel):
        if (m <= 1):
            return "%02d : %02d" % (m, s), "red"
        elif (m <= 3):
            return "%02d : %02d" % (m, s), "orange"
        else:
            return "%02d : %02d" % (m, s), "green"
    else:
        if (m < 1):
            return "%02d : %02d [BRD]" % (m, s)
        elif: (m == 1):
            return "%02d : %02d [ARR]" % (m, s)
        else:
            return "%02d : %02d" % (m, s)


