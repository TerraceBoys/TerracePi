__author__ = 'Terrace Boiz'


# print all northbound train times
def pop_north(dict, station='Roxbury Crossing'):
    result = station + " - Northbound " + "\n"
    for x in range(len(dict['Northbound'])):
        if x == 0:
            result += "Next Train: "
            m, s = secs_to_mins(dict['Northbound'][x])
            result += time_handler(m, s) + "\n"
        else:
            m, s = secs_to_mins(dict['Northbound'][x])
            result += time_handler(m, s) + "\n"
    return result


# Print all southbound train times
def pop_south(dict, station='Roxbury Crossing'):
    result = station + " - Southbound " + "\n"
    for x in range(len(dict['Southbound'])):
        if x == 0:
            result += "Next Train: "
            m, s = secs_to_mins(dict['Southbound'][x])
            result += time_handler(m, s) + "\n"
        else:
            m, s = secs_to_mins(dict['Southbound'][x])
            result += time_handler(m, s) + "\n"
    return result


def panel_train(dict, station='Roxbury'):
    if 'Northbound' in dict:
        t1Mins, t1Secs = secs_to_mins(dict['Northbound'][0])
        result1, color1 = time_handler(t1Mins, t1Secs, True)
        if len(dict['Northbound']) > 1:
            trainMinutes = []
            for train in dict['Northbound']:
                mins, secs = secs_to_mins(train)
                if mins <= 32:
                    trainMinutes.append(mins)
            return result1, color1, trainMinutes
        else:
            return result1, color1, [t1Mins]


# Convert seconds into minutes and seconds
def secs_to_mins(seconds):
    m, s = divmod(seconds, 60)
    return m, s


# Format the arrival times
def time_handler(m, s, panel=False):
    if panel:
        if m <= 1:
            return "%02d : %02d" % (m, s), "red"
        elif m <= 3:
            return "%02d : %02d" % (m, s), "orange"
        else:
            return "%02d : %02d" % (m, s), "green"
    else:
        if m < 1:
            return "%02d : %02d [BRD]" % (m, s)
        elif m == 1:
            return "%02d : %02d [ARR]" % (m, s)
        else:
            return "%02d : %02d" % (m, s)
