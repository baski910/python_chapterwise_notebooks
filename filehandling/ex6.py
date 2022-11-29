####################################################################
# fileobject = open(filepath,filemode,buffering)
# write - writes the content passed as argument to the filed pointed to by file object
#
# writelines - takes a list as argument and writes the list element to the file pointed to by the file object
###########################################################################

fh = open('file1.txt','w')

fh.write("programming in python is fun\n")
fh.write("python is a simple language to learn\n")

fh.close()