data = input().split()
for num in data:
    intNum = int(num)
    if intNum%2 == 0:
        print(str(num), 'is even')
    else:
        print(str(num), 'is odd',)