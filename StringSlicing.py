#slicing in python is same as subString in java

from re import L


name='''Amol'''

print(name[1:4])
print(name[:4]) #blank space considered as 0
print(name[1:]) #print(name[1:4]) same as that


#negative slicing 
#  a  m  o  L
#  0  1  2  3 
#  -4 -3 -2 -1

print(name[-3:-1]) #now -1 is included 
print(name[-4:4])

