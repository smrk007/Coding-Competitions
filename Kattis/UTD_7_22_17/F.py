data = [
    [0, 0, 0, False]
]

def getTime(line):
    hour = int(line[0:2])
    min = int(line[3:5])/60
    sec = int(line[6:8])/3600
    return hour+min+sec

for line in sys.stdin:

    if len(line) > 8:
        entry = [0, 0, 0, False, '']
        entry[0] = getTime(line)
        entry[1] = line[10:]
        entry[2] = data[-1][1]*(entry[0]-data[-1][0]) + data[-1][2]
        data.append(entry)

    if len(line) == 8:
        entry = [0, 0, 0, True, line]
        entry[0] = getTime(line)
        entry[1] = data[-1][1]
        entry[2] = data[-1][1]*(entry[0]-data[-1][0]) + data[-1][2]
        data.append(entry)

for entry in data:
    if entry[3]:
        out = ' '.join([entry[4], '%.2f' % entry[2], 'km'])
        print(out)
