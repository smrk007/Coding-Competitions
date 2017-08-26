line1 = input().split(' ')
N = int(line1[0]) # Number of People
T = int(line1[1]) # Time Available

# Data formatting
data = []
for x in range(N):
	line = input().split(' ')
	cash = int(line[0])
	time = int(line[1])
	element = (cash,time)
	data.append(element)

# Supporting functions
def mergeSort(data):

	length = len(data)

	if length == 1:
		return data

	halfway = int(length/2)
	first = mergeSort(data[:halfway])
	second = mergeSort(data[halfway:])
	sortedList = []

	while len(first) > 0 or len(second) > 0:
		if len(first) == 0:
			for i in range(len(second)):
				sortedList.append(second.pop(0))
		elif len(second) == 0:
			for i in range(len(first)):
				sortedList.append(first.pop(0))
		else:
			if first[0][0] > second[0][0]:
				sortedList = [first.pop(0)] + sortedList
			else:
				sortedList = [second.pop(0)] + sortedList

	return sortedList

# Crude sorting algorithm for data
'''
sortedData = []
for x in range(N):
	maximum = data[0][0]
	index = 0
	if len(data) == 1:
		sortedData.append(data[0])
	else:
		for i in range(1,len(data)):
			if data[i][0] > maximum:
				maximum = data[i][0]
				index = i
		sortedData.append(data.pop(index))
'''

# Merge sort so that we can have O(n log(n)) instead of O(n^2)
sortedData = mergeSort(data)

taken = set()
money = 0
for person in sortedData:
	for time in range(person[1] + 1):
		if (person[1] - time) not in taken:
			taken.add(person[1] - time)
			money += person[0]
			break

print(money)
