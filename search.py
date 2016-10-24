import re

searchString = ''
file = ''
with open(file, 'r') as f:
    dump = f.readlines()

for line in dump:
    if searchString in line:
        print line

s = re.split(searchString, dump)
array = []
for i in dump:
    if re.search(searchString, i):
          array.append(i)