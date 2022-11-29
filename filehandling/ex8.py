##################################################################
# reset cursor position
#  
# seek - takes 2 arguments
#        1st param - offset in terms of bytes
#        2nd param - position based on which offset is calculated
#                    0 - beginning
#                    1 - current cursor position
#                    2 - end of the file
#
# tell - returns the cursor position
######################################################################

fh = open('readme.txt','r')

fh.read() 

fh.seek(0,0) 

for line in fh.readlines():
    print(line)

fh.close()