data = input().split()

N = int(data[0])

def copyOperations(initial, target, charDist, count):

    if len(charDist[target[0]]) == 0:
        return "impossible"
    length = 0
    valid = charDist(target[0])
    while len(valid) > 0:
        length += 1
        lenValid = len(valid)
        for i in range(len(valid)):
            if valid[lenValid-i-1] == 0:
                if initial[1] != target[length]:
                    del valid[lenValid-i-1]
            elif valid[lenValid-i-1] == len(initial) - 1:
                if initial[len(initial)-2] != target[length]:
                    del valid[lenValid-i-1]
            else:
                if (initial[valid[lenValid-i-1]+1] != target[length]) or \
                        (initial[valid[lenValid-i-1]-1] != target[length]):
                    del valid[lenValid-i-1]
    if length == len(target):
        return count + 1
    return copyOperations(initial, target[length:], charDist, count + 1)

for case in range(N):

    initial = data[2*case + 1]
    target = data[2*case + 2]

    charDist = {
        'A' : [],
        'C' : [],
        'G' : [],
        'T' : []
    }

    for charIndex in range(len(initial)):
        charDist[initial[charIndex]].append(charIndex)

    print(copyOperations(initial, target, charDist, 0))