data = dict()

def findValue(arithList,data):
	addTheseTogether = arithList.split('+')
	out = 0
	for section in addTheseTogether:
		subSum = 0
		subtractThese = section.split('-')
		for i in range(len(subtractThese)):
			if i == 0:
				subSum += data[subtractThese[i]]
			else:
				subSum -= data[subtractThese[i]]
		out += subSum
	if out in data:
		return data[out]
	return 'unknown'

while True:

	try:
		line = input().split(' ')
		if line[0] == 'clear':
			data = dict()
		if line[0] == 'def':
			variable = line[1]
			value = int(line[2])
			data[value] = variable
			data[variable] = value
		if line[0] == 'calc':
			items = line[1:]
			unknown = False
			value = 0
			for string in items:
				if not (string == '-' or string == '+' or string == '=' or string in data):
					unknown = True
			if unknown:
				items.append('unknown')
			else:
				arithList = ''.join(items[:-1])
				items.append(findValue(arithList,data))
			print(' '.join(items))
	
	except EOFError:
		break
