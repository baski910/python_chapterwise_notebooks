import pdb

chars = ['a','b','c','d','e']
numbers = [1,2,3]

for num in numbers:
  pdb.set_trace()
  for char in chars:
    print("{}:{}".format(num,char))
