from re import search
from functools import reduce
map = None
with open('./input.txt', 'r') as f:
    map = f.readlines()
map = [x.strip() for x in map]

# records will be a list of records
# current record will be appended to then
# appended to records and reset when a '' is encountered

records = []
def reduceFunc(x,y):
    if y == '':
        records.append(x)
        return ''
    return x + " " + y
    
reduce(reduceFunc, map,'')

# At this point each record contains the data
# transform the record into a list of key:value
records = [x.split() for x in records]
records2 = []
for record in records:
    newrecord = []
    for item in record:
        res = search("([#\w]*)(?::)([#\w]*)", item)
        tupform = ((res.group(1), res.group(2)))
        newrecord.append(tupform)
    records2.append(newrecord)
records2 = [dict(x) for x in records2]

def filterIfNotPresent(records, field):
    return [x for x in records if field in x.keys()]

for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
    records2 = filterIfNotPresent(records2, x)

print(len(records2))