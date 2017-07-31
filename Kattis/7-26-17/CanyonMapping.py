

N = int(input())
K = int(input())

if K == 1:
    Xs = []
    Ys = []
    for i in range(N):
        Xs.append(int(input()))
        Ys.append(int(input()))
    value = max([max(Xs)-min(Xs), max(Ys) - min(Ys)])
    print(round(value, 2))

else:
    '''
    Steps of the process:
        Define function, determining whether entire canyon mapped
        Set K squares into the map, such that they each initially have the position and size of a K = 1 square
        m = 1, and n = m initially
        Decrease the length of a side of each square by m, and then see if cert
    '''