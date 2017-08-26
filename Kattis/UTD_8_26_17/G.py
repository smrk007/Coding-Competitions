N = int(input())
data = input().split(' ')
for i in range(len(data)):
    data[i] = int(data[i])
data = sorted(data)

output = []

group = []
for stop in data:
    if len(group) == 0:
        group.append(stop)
    elif stop == group[len(group)-1]+1:
        group.append(stop)
    else:
        if len(group) > 2:
            output.append(str(group[0]) + '-' + str(group[len(group)-1]))
        else:
            for i in group:
                output.append(str(i))
        group = [stop]

if  len(group) > 2:
    output.append(str(group[0]) + '-' + str(group[len(group)-1]))
else:
    for i in group:
        output.append(str(i))

print(' '.join(output))