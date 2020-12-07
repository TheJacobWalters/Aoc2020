# Test
'''
range = [0, 127]
for y in 'FBFBBFF':
    if y == 'F':
        #range[1] = range[1]//2
        range[1] = range[0] + ((range[1] - range[0]) // 2)
    elif y == 'B':
        range[0] += 1+ ( (range[1] - range[0]) // 2 )
    print(range)
'''
# Prog 1

map = None
with open('./input.txt', 'r') as f:
    map = f.readlines()
map = [x.strip() for x in map]
map = [[x[0:7],x[7:]] for x in map]

# calculate row x[0] is the first 7 chars of the address
for x in map:
    range = [0, 127]
    for y in x[0]:
        if y == 'F':
            range[1] = range[0] + ((range[1] - range[0]) // 2)
        elif y == 'B':
            range[0] += 1+ ( (range[1] - range[0]) // 2 )
    x.append(range[0])

# calc column [1] is the last 3 chars of the address
for x in map:
    range = [0, 7]
    for y in x[1]:
        if y == 'L':
            range[1] = range[0] + ((range[1] - range[0]) // 2)
        elif y == 'R':
            range[0] += 1+ ( (range[1] - range[0]) // 2 )
    x.append(range[0])

# append the seatId
for x in map:
    x.append((x[2] * 8) + x[3])

# part 2
seatIds = [x[-1] for x in map]
seatIds = sorted(seatIds)
for x in seatIds:
    if x == seatIds[0] or x == seatIds[-1]:
        continue
    
    if x-1 not in seatIds:
        print(x)
'''
x = []
for seat in map:
    #print(seat[-1] + 1 , seat[-1] -1)
    print(seat[-1] -1 in seatIds)
    
    if (seat[-1]+1 in seatIds) and (seat[-1]-1 in seatIds):
        x.append(seat[-1])
print(x)
'''