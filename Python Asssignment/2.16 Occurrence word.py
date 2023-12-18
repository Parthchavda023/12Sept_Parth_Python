'''Write a Python program to count the occurrences of each word in a
given sentence'''


p=input("Enter Word/Paragraph:")
p.split()   #Word/paragraph Na letter ne sepatare krva

s=input("Enter Any character:")

count=0

for i in p:
    if i==s:
        count+=1

print(p.count(s))