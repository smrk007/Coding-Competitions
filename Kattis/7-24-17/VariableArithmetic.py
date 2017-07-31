data = []

def isInt(string):
    for char in '1234567890':
        if string[0] == char:
            return True
    return False

'''while True:
    try:
        data.append(input())
    except EOFError:
        data.pop()
        break'''

data = open('sample.in','r')
data = data.read().split('\n')
data = ' '.join(data)
data = data.split(' ')


code = 0
vExist = set()
vValue = dict()
line = [0]

next = data.pop(0)
if isInt(next):
    line[0] += int(next)
else:
    line.append(next)

while len(data) > 0:

    if code == 0:
        next = data.pop(0)
        if next == "+":
            code = 1
        elif next == "=":
            code = 2
        else:
            line[0] = str(line[0])
            print(' + '.join(line))
            vExist.clear()
            vValue.clear()
            line = [0]
            if next in vValue:
                line[0] += vValue[next]
            elif isInt(next):
                line[0] += int(next)
            else:
                line.append(next)

    elif code == 1:
        next = data.pop(0)

        if isInt(next):
            line[0] += int(next)
        else:
            line.append(next)
        code = 0

    elif code == 2:
        vExist.add(line[1])
        vValue[line[1]] = int(data.pop(0))
        code = 0
