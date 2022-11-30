######################################################
# regular expression - user defined expression to match
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
#
# hello\s[abcdefghijklmn] - hello anchor hello bat hello cat
# hello\s[a-n] - hello anchor hello bat hello cat
# hello\s[a-zA-Z0-9] - hello zeebra
# hello\s[\w] i.e, \w - a-zA-Z0-9
#######################################################

import re

s1 = input("Enter a string\n")

#sobj = re.search(r'hello\s[abcdefghijklmn]',s1)
#sobj = re.search(r'hello\s[a-n]',s1)
sobj = re.search(r'hello\s[\w]',s1)

if sobj:
    print("matched")
else:
    print("not matched")