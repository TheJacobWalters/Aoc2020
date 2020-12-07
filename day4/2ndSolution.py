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

# Start part 2
def Diff(li1, li2, attr):
    li_dif = [i for i in li1 + li2 if i not in li2 ]
    for x in li_dif:
        print(x[attr], x)
# byr, iyr, eyr

records2 = [x for x in records2 if int(x['byr'])>=1920 and int(x['byr'])<=2002]

records2 = [x for x in records2 if int(x['iyr'])>=2010 and int(x['iyr'])<=2020]

records2 = [x for x in records2 if int(x['eyr'])>=2020 and int(x['eyr'])<=2030]

# hgt
records3 = []
regex = '([0-9]+)([cmin]+)'
for x in records2:
    res = search(regex, x['hgt'])
    if res == None:
        continue
    y = int(res.group(1))
    if res.group(2) == 'cm':
        if (y >= 150) and (y <= 193):
            records3.append(x)
    elif res.group(2) == 'in':
        if (y >= 59) and (y <= 76):
            records3.append(x)
    else:
        print(res.group(1), res.group(2))
# hcl
regex = '#[0-9a-f]{6}'
records3 = [x for x in records3 if search(regex, x['hcl'])]
# ecl
colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
records3 = [x for x in records3 if x['ecl'] in colors]
# pid
regex = '[0-9]{9}'
test = records3
records3 = [x for x in records3 if search(regex, x['pid'])]
Diff(test, records3, 'pid')
for x in records3:
    print(x['pid'])
#print(records3)
print(len(records3))
