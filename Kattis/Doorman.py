M = int(input)
queue = input().split()

options = [queue.pop(0), queue.pop(0)]
current = 0
maximum = 0

while True:

    if current == 0:
        next = options.pop(0)
        if 