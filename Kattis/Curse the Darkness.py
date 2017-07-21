from math import *

data = input().split()

class vec2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # a**2 + b**2 == c**2
        a = self.x - other.x
        b = self.y - other.y
        return(sqrt(a**2 + b**2))

N = int(data[0])
it = 1

while it < len(data):

    book = vec2(int(data[it]), int(data[it+1]))
    it += 2

    candleQty = data[it]
    it += 1

    candles = []
    for i in range(candleQty):
        candles.append(vec2(int(data[it]), int(data[it+1])))
        it += 2

    done = False
    for candle in candles:
        if not done and book.distance(candle) < 8:
            print('light a candle')
            done = True
    if done == False:
        print('curse the darkness')
