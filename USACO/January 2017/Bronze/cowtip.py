inFile = open('cowtip.in','r')
outFile = open('cowtip.out','w')

lines = inFile.read().split('\n')


N = int(lines[0])

lines = lines[1:]

# Supporting Functions

def adjust_rectangle(row_num,cow_num,grid):
    
    for i in range(row_num+1):
        for j in range(cow_num+1):
            grid[i][j]+=1
    return(grid)

# Principal Code

#  Initializing the Grid

grid = []
for line in lines:
    row = []
    for cow in line:
        row += [int(cow)]
    grid += [row]

#  Initializing Diagonal Coordinates

diagonal = []
for x in range(N):
    diagonal = [x] + diagonal
for x in range(N-1):
    diagonal = ['x'] + diagonal
for x in range(N):
    diagonal += ['x']

total = 0

for d in range((2*N)-1):
    # for each diagonal
    
    for i in range(N):
        if diagonal[i] != 'x':
            if grid[i][diagonal[i]]%2 == 1:
                adjust_rectangle(i,diagonal[i],grid)
                total += 1
    
    diagonal = diagonal[1:]

outFile.write(str(total))

inFile.close()
outFile.close()
