import re
regex = re.compile('([0-9]*)(?:-)([0-9]*)(?: )([a-z])(?:: )([a-z]*)')
lines = None
numberGoodPass = 0
with open('./input.txt', 'r') as f:
    lines = [x.strip() for x in f]

matchs = [regex.match(x) for x in lines]
for match in matchs:
    first, second, target, string = match.groups()
    first = int(first)
    second = int(second)
    iter = re.finditer(target, string)
    positions = [ 1 + x.start() for x in iter]
    
    if (first in positions) and (second in positions):
        continue
    if (first in positions) or (second in positions):
        numberGoodPass += 1
print(f"number of good matchs {numberGoodPass}")