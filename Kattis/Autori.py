data = input().split()

out = ""
for char in data[0]:
    for cap in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char == cap:
            out = out + cap

print(out)