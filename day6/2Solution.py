from functools import reduce
from collections import Counter
# Part 2
def reducer(a,b):
    x = Counter(a) & Counter(b)
    return "".join(list(x.elements()))

def solution(a,b):
    return a + len(b)
    
map = None
with open('./input.txt', 'r') as f:
    map = f.read()
map = map.split('\n\n')
map = [x.split('\n') for x in map]
map = [reduce(reducer, x) for x in map]
answer = reduce(solution, map, 0)