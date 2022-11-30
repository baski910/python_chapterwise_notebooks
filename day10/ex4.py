######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#
# re - module used to work with regular expression
# www.mydomain.co.in  - .*\.(.*)\..* - returns 'co' because of greedy match
# www.mydomain.co.in -  .*?\.(.*?)\..* - return 'mydomain' because of non-greedy match
########################################################

import re

s1 = input("Enter a string\n")

sobj = re.search(r'.*?\.(.*?)\..*',s1)

if sobj:
    print(sobj.group(1)) # returns characters between 2 dot
    
else:
    print("not matched")