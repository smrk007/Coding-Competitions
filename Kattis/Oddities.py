data = input().split()
for num in data:
    intNum = int(num)
    if intNum%2 == 0:
        print(num, 'is', 'even')
    else:
        print(num, 'is', 'odd',)