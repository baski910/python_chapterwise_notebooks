######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#
# re - module used to work with regular expression
# * - zero or more times
# to*tal - ttal total tootal tooootal toooooooootal
# + - one or more times
# to+tal - total tootal tooootal toooooooootal
# ? - either zero or one
# https?://www.mydomain.com - https://www.mydomain.com http://www.mydomain.com
# {} - {n} pattern should occur 'n' number of time
# https://w{3}.mydomain.com
#####################################################
import re

s1 = input("Enter a string\n")

sobj = re.search(r'to*tal',s1)
#sobj = re.search(r'to+tal',s1)
#sobj = re.search(r'https?://www.mydomain.com',s1)
#sobj = re.search(r'https://w{3}.mydomain.com',s1)
if sobj:
    print("matched")
else:
    print("not matched")