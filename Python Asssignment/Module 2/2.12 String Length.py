'''Write a Python program to calculate the length of a string.'''


# p='Write a Python program to calculate the length of a string.'
# print(len(p))

#--------User input----------#

# p=input("enter Word:")
# print(p)
# print(len(p))


#-------Using loop-----#

p=input("enter Word:")
len=0

for i in p:
    len+=1

print(len)