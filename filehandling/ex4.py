####################################################################
# fileobject = open(filepath,filemode,buffering)
# filepath = C:\Users\Administrator\Desktop\a.txt
# windows 
# r'C:\Users\Administrator\Desktop\a.txt'
# 'C:\\Users\\Administrator\\Desktop\\a.txt'
# 'C:/Users/Administrator/Desktop/a.txt'
# Linux - filepath as it is
#
# filemode
# read and write - r,r+,rb,rb+ - leads to error if the file is missing
# write and read - w,w+,wb,wb+ - creates the files if the file is missing, overwrite if exists
# append and read - a,a+,ab,ab+ - creates the files if the file is missing, appends if exists
#
# buffering - 0,1,-1
# 0 - no buffering
# 1 - custom buffer size
# -1 - OS defined
###########################################################################

fh = open('/home/baskar/Documents/14062021/day7/readme.txt','r')

print(fh.name) # returns the filename along with path
print(fh.mode) # file opening mode
print(fh.closed) # returns file closed status - False


fh.close()


