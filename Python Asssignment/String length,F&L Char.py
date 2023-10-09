'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings. '''


p=['level', 'hello', 'world', 'madam', 'racecar']
str=0

# print(len(p))

for i in p: 
    if len(i)>=2 and i[0]==i[-1]:
        str+=1

print('String:-',str)