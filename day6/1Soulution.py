from functools import reduce
# Part 1
def reducer(a, b):
    combo = ""
    for x in [a,b]:
        for y in x:
            if y not in combo:
                combo += y
    return combo
def answerP1(a,b):
    return a + len(b)
    
map = None
with open('./input.txt', 'r') as f:
    map = f.read()
map = map.split('\n\n')
map = [x.split('\n') for x in map]
map = [reduce(reducer, x) for x in map]

answer1 = reduce(answerP1, map, 0)
# Part 2
