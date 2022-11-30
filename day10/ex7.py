######################################################
# regular expression - user defined expression to match/
#                      extract from the given input
# metacharacters - . * + ? {} () [] \w \d \b ^ $
# \bhello\b - matches hello if it comes as separate word
#######################################################

import re

#s1 = "helloworld"
s1 = "hi hello python"

sobj = re.search(r'\bhello\b',s1)

if sobj:
    print("matched")
else:
    print("not matched")