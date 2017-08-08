import sys
import math

def distance(point1, point2):
    return math.sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )

while true:

    N = int(input())

    if N == 0:
        break

    data = []
    for _ in range(N):
        a = float(input())
        b = float(input())
        data.append((a,b))


    minimum = sys.maxsize
    points = []
    for i in range(N-1):
        for j in range(i+1,N):
            dist = distance(data[i],data[j])
            if dist < minimum:
                minimum = dist
                points = [data[i],data[j]]
    print(points[0][0], points[0][1], points[1][0], points[1][1])

