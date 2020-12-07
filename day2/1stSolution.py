import re
regex = re.compile('([0-9]*)(?:-)([0-9]*)(?: )([a-z])(?:: )([a-z]*)')
lines = None
numberGoodPass = 0
with open('./input.txt', 'r') as f:
    lines = [x.strip() for x in f]

matchs = [regex.match(x) for x in lines]
for match in matchs:
    min, max, target, string = match.groups()
    min = int(min)
    max = int(max)
    count = string.count(target)
    if (count >= min) and (count <= max):
        numberGoodPass +=1
print(f"number of good matchs {numberGoodPass}")