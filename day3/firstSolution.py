import pdb
from functools import reduce
from operator import mul

map = None
with open('./input.txt', 'r') as f:
    map = f.read().split()
width = len(map[0])
length = len(map)
map = [x * 500 for x in map]

def calcHits(over,down):
    numberOfTreeHits = 0
    for x in range(len(map)):
        if x*down > len(map):
            break
        try:
            if '#' == map[x*down][x*over]:
                numberOfTreeHits += 1
        except:
            breakpoint()
    return numberOfTreeHits

results = []
coords = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for x in coords:
    results.append(calcHits(*x))
print(reduce(mul, results))
