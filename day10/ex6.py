######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#######################################################

import re

fh = open('numbers.txt','r')

for line in fh.readlines():
    line = line.rstrip('\n') # removes new line character
    sobj = re.search(r'.*#(\d+)', line)

    if sobj:
        print(sobj.group(1)) # returns digits from each line

fh.close()