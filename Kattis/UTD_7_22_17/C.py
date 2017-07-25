#f = open('sample.in', 'r')
#data = f.read().split()

# Functions

def value(element): # Returns the value of an element
    if len(element) == 9:
        a = int(element[0])
        b = int(element[2:4])
        c = 0
        if element[5:9] == 'p.m.':
            c =  1200
        output = ((a%12)*100) + b + c
        return output
    if len(element) == 10:
        a = int(element[0:2])
        b = int(element[3:5])
        c = 0
        if element[6:10] == 'p.m.':
            c = 1200
        output = ((a%12)*100) + b + c
        return output

def caseSort(case): # Returns a sorted version of a case
    sortedList = []
    unsortedList = case
    for i in range(len(unsortedList)):
        minIndex = 0
        minValue = 2400
        for j in range(len(unsortedList)):
            if unsortedList[j][0] < minValue:
                minIndex = j
                minValue = unsortedList[j][0]
        sortedList.append(unsortedList.pop(minIndex))
    return sortedList

# Principal Code

cases = []
N = -1
while N != 0:
    case = []
    N = int(input())
    for i in range(N):
        #p1 = data.pop(0)
        #p2 = data.pop(0)
        #out = ' '.join([p1,p2])
        #case.append(out)
        case.append(input())
    cases.append(case)

cases2 = []
for case in cases:
    newCase = []
    for element in case:
        newCase.append([value(element), element])
    cases2.append(newCase)

cases3 = []
for case in cases2:
    cases3.append(caseSort(case))


for case in cases3:
    for element in case:
        print(element[1])
    print()

