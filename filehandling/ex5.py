####################################################################
# fileobject = open(filepath,filemode,buffering)
# read - returns the entire file content without argument
#        returns the bytes specified by argument, if argument is provided
#
# readline - return 1 line from current cursor position
#
# readlines - returns the file as list.
###########################################################################

fh = open('/home/baskar/Documents/14062021/day7/readme.txt','r')

#print(fh.read()) # return the entire file content

#print(fh.read(100)) # returns 1st 100 bytes from the file

#print(fh.readline()) # returns the 1st line
#print(fh.readline()) # returns the 2nd line

content = fh.readlines() # returns the file as list. each line becomes element of the list

print(content)

fh.close()


