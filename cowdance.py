### Header

inFile = open('cowdance.in','r')
outFile = open('cowdance.out','w')

lines = inFile.read().split('\n')

line0 = lines[0].split(' ')
N = int(line0[0])
Tmax = int(line0[1])


lines = lines[1:]

### Supporting Functions



def return_wo_Tmax(lis,Tmax):
    
    remaining = Tmax
    the_list = lis
    for cow in the_list:
        if (remaining>=min(the_list)):
            the_list,remaining = wo_if_max(the_list,remaining)
        else:
            return(the_list)         

def wo_if_max(the_list,remaining):
    
    old_remaining = remaining
    for x in the_list:
        if x <= remaining:
            new_remaining = old_remaining - x
            indx = the_list.index(x)
            new_list = the_list[:indx]+the_list[indx+1:]
            
            return(new_list,new_remaining)
        
### Principal Code

# Arranges cows in descending order
lis = []
for i in lines:
    if i != '':
        lis += [int(i)]
lis = sorted(lis, reverse = True)

output = 0

while lis != None:
    
    lis = return_wo_Tmax(lis,Tmax)
    output += 1

### Footer

outFile.write(str(output))

inFile.close()
outFile.close()