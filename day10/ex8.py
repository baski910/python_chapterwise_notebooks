import re

fh = open('input.txt','r')

d1 = {}
d2 = {}

count = 1

for line in fh.readlines():
    line = line.rstrip('\n') # removes new line character

    sobj = re.search(r'^\s*$',line)

    if sobj:
        continue

    sobj = re.search(r'^#.*',line)

    if sobj:
        d1.setdefault('person{}'.format(count),dict(d2))
        count += 1
        d2.clear()
    else:
        persons = line.split(':')
        d2[persons[0]] = persons[1]

fh.close()

print(d1)