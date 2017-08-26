while True:

    line = input().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])

    n = line[0]
    m = line[1]

    if n == 0 and m == 0:
        break


    anyValid = False
    min = 0
    mostTickets = 0
    bestA = 0
    bestB = 0
    for i in range(n):
        case = input().split(' ')
        for i in range(len(case)):
            case[i] = int(case[i])
        a = case[0]
        b = case[1]

        if a <= m:
            if not anyValid:
                anyValid = True
                bestA = a
                bestB = b
                min = b/a
            elif b/a <= min and b > bestB:
                min = b/a
                bestA = a
                bestB = b
    if anyValid:
        print("Buy " + str(bestA) + " tickets for $" + str(bestB))
    else:
        print("No suitable tickets offered")
