'''Write a Python program to count the number of characters (character
frequency) in a string'''


# p='Write a Python program to count the number of characters (character frequency) in a string'
# print(p.count('c'))
# print(p.count('a'))

#--------User input--------#
p=input("Enter Word/Paragraph:")
p.split()   #Word/paragraph Na letter ne sepatare krva

s=input("Enter Any character:")

count=0

for i in p:
    if i==s:
        count+=1

print(p.count(s))
