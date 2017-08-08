N = int(input())

for q in range(N):

	line = input().split(' ')
	n = int(line[0])
	A = int(line[1])
	B = int(line[2])
	C = int(line[3])
	D = int(line[4])
	x0 = int(line[5])
	y0 = int(line[6])
	M = int(line[7])

	data = [[0 for layer2 in range(3)] for layer1 in range(3)] # Structure to store information about the types of trees available

	X = x0
	Y = y0
	data[X%3][Y%3] += 1
	# Adding information about which types of trees are available
	for tree in range(n-1):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		data[X%3][Y%3] += 1

	# Finding which combinations of trees with X's and Y's whose Mod3 add up to 0
	'''
	Notation:
	A = (0,0)
	B = (1,0)
	C = (2,0)
	D = (0,1)
	E = (1,1)
	F = (2,1)
	G = (0,2)
	H = (1,2)
	I = (2,2)

	Possible combinations:
	AAA
	DDD
	GGG
	BBB
	EEE
	HHH
	CCC
	FFF
	III

	ADG
	BEH
	CFI
	ABC
	DEF
	GHI
	AEI
	BFG
	CDH
	GEC
	HFA
	IDB
	'''
	
	
	a = (0,0)
	b = (1,0)
	c = (2,0)
	d = (0,1)
	e = (1,1)
	f = (2,1)
	g = (0,2)
	h = (1,2)
	i = (2,2)

	cases = [
	a, # AAA
	d, # DDD
	g, # GGG
	b, # BBB
	e, # EEE
	h, # HHH
	c, # CCC
	f, # FFF
	i, # III
	[a,d,g], # ADG
	[b,e,h], # BEH
	[c,f,i], # CFI
	[a,b,c], # ABC
	[d,e,f], # DEF
	[g,h,i], # GHI
	[a,e,i], # AEI
	[b,f,g], # BFG
	[c,d,h], # CDH
	[g,e,c], # GEC
	[h,f,a], # HFA
	[i,d,b]  # IDB
	]

	value = 0

	for i in range(9):
		# Number of combinations of triangles in the mono-case
		case = cases[i]
		number = data[case[0]][case[1]]
		value += ( (number) * (number - 1) * (number - 2) ) / 6

	for i in range(9, len(cases)):
		# number of combinations of triangles in the multi-case
		case = cases[i]
		internalValue = 1
		for point in case:
			internalValue *= data[point[0]][point[1]]
		value += internalValue

	print('Case #' + str(q + 1) + ': ' + str(int(value)))
