s1="helloworld"
from random import shuffle

chars = [x for x in s1]

shuffle(chars)

print(''.join(chars))

import hashlib

b="helloworld"

obj = hashlib.md5(b.encode())

print(obj.hexdigest())