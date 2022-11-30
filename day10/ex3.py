######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#
# re - module used to work with regular expression
# www.mydomain.com - www.(....).com
#                    .*\.(.*)\..*
########################################################

import re

s1 = input("Enter a string\n")

sobj = re.search(r'.*\.(.*)\.(.*)',s1)

if sobj:
    print(sobj.group(1)) # returns characters between 2 dot
    print(sobj.group(2)) # returns character after 2nd dot
else:
    print("not matched")