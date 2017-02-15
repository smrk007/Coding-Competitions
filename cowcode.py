### Header

inFile = open('cowcode.in','r')
outFile = open('cowcode.out','w')

line = inFile.read().split('\n')
line = line[0]


string = line[:line.index(' ')]
index = int(line[line.index(' ')+1:])

### Supporting Functions
if index < 1000000:
    
    def F(s):
        return(s+s[-1:]+s[:-1])
    
    ### Principal Code
    
    L = len(string)
    iterations = 0
    
    while L < index:
        L *= 2
        iterations += 1
        
    for x in range(iterations):
        string = F(string)
    
else:

    def max_mult_2(index,L):
        
        val = L
        while val < index:
            val *= 2
        return(int(val/2))
    
    ### Principal Code
    
    L = len(string)
    
    while index > L:
        
        
        adjust = 1+max_mult_2(index,L)
        index = index - adjust

### Footer


outFile.write(string[index-1])

inFile.close()
outFile.close()