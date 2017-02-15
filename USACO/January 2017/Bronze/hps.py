### Header

inFile = open('hps.in','r')
outFile = open('hps.out','w')

lines = inFile.read().split('\n')
N = int(lines[0])

lines = lines[1:]

### Supporting Functions



### Principal Code

total_hoof = 0
total_paper = 0
total_scissors = 0
for i in lines:
    if i == 'H':
        total_hoof += 1
    if i == 'P':
        total_paper += 1
    if i == 'S':
        total_scissors += 1

highest = 0
for order in [('H','P'),('H','S'),('S','H'),('S','P'),('P','S'),('P','H')]:
    
    if order[1] == 'P':
        value = total_paper
    if order[1] == 'H':
        value = total_hoof
    if order[1] == 'S':
        value = total_scissors
    for i in lines:
        if i == order[1]:
            value -= 1
        if i == order[0]:
            value += 1
        if value >= highest:
            highest = value

### Footer

outFile.write(str(highest))

inFile.close()
outFile.close()
