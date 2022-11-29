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

fh = open('readme.txt','rb') # opening in binary mode allows us to use 
                             # values 1 and 2 in seek function for 2nd parameter

print(fh.read(5)) # returns 1st 5 bytes

print(fh.tell()) # returns 5

#fh.seek(10,0) # resets cursor to 10th byte from beginning of the file

fh.seek(5,1) # resets cursor to 10th byte from current cursor position

print(fh.tell()) # returns 10

print(fh.read(5)) # returns 5bytes from 10th byte

fh.close()