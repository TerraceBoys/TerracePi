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


def panel_train(dict):
    m1, s1 = secs_to_mins(dict['Northbound'][0])
    m2, s2 = secs_to_mins(dict['Northbound'][1])
    result1, color1 = time_handler(m1, s1, True)
    result2, color2 = time_handler(m2, s2, True)
    return result1, color1, result2, color2


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


