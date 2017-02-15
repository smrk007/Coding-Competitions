inFile = open('notlast.in','r')
outFile = open('notlast.out','w')

lines = inFile.read().split('\n')
lines = lines[1:]

# Initialization of initials and names

initials = ['B','E','D','G','A','M','H']
total_milk = [0,0,0,0,0,0,0]
names = ['Bessie','Elsie','Daisy','Gertie','Annabelle','Maggie','Henrietta']

# Supporting Functions

def indx(line):
    #returns the index of the first integer
    for char in line:
        for digit in '1234567890':
            if char == digit:
                return(line.index(char))

# Principal Code

for line in lines:
    
    if len(line)>0:
        quant_milk = line[indx(line):]
        initial = line[0]
        total_milk[initials.index(initial)] += int(quant_milk)
               
    
smallest = min(total_milk)
for x in range(7):
    if total_milk[x] == smallest:
        total_milk[x] += 1000

new_smallest = min(total_milk)

how_many = 0
for x in total_milk:
    if x == new_smallest:
        how_many += 1
        
if how_many != 1:
    outFile.write('Tie')
else:
    for x in range(7):
        if total_milk[x] == new_smallest:
            outFile.write(names[x])


inFile.close()
outFile.close()