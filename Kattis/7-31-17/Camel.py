N = int(input())
count = 0

camelList = []  # This represents the order Jaap's camel bets
other1 = [None] * N  # This represents the place of Jan's bets for each camel within the order
other2 = [None] * N  # This is the same as Jan's list, but for Thij
setOfPreviousCamels = set()  # This lets us know which camels have already been tried as the last camel in a bet

for i in range(3):
    for j in range(N):
        if i == 0:  # If it's Jaap's bet
            camelList.append(int(input()))
        if i == 1:  # If it's Jan's bet
            other1[int(input())] = j
        if i == 2:  # If it's Thij's bet
            other2[int(input())] = j

for camel in camelList:
    for previousCamel in setOfPreviousCamels:
        case1 = other1[previousCamel] < other1[camel]
        case2 = other2[previousCamel] < other2[camel]
        if case1 and case2:
            count += 1
    setOfPreviousCamels.add(camel)

print(count)
