######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#
# re - module used to work with regular expression
# 
# match - takes 3 arguments. 3rd argument is optional
#         1st param - regular expression
#         2nd param - string to be matched
#         3rd param - flags
#         matches a single line.
#         return match object on success or False on failure
#
# search - takes 3 arguments. 3rd argument is optional
#         1st param - regular expression
#         2nd param - string to be matched
#         3rd param - flags
#         matches a against multiple lines
#         return match object on success or False on failure
########################################################
import re

s = "this line contains firstname and lastname Bob Smith and so on"

res = re.search(r'.*?(\b[A-Z][a-z]+\s[A-Z][a-z]+\b).*',s)

if res:
    print(res.group(1))
else:
    print("not matched")

fh = open('readme.txt','r')

count = 0

for line in fh.readlines():
    sobj = re.search(r'^\s*$',line)
    # ^ - search at the beginning
    # \s - matches a space
    # * - quantifies previous pattern zero or more times
    # $ - search at the end

    if sobj:
        print(line)
        count += 1

fh.close()
print("number of blank lines {}".format(count))

