'''Write a python program to find the longest words in file.'''


fl=open('longword.txt','w')
fl.write('Hello ...\nI am Parth Chavda\nI from Halavad')

fl=open('longword.txt','r')
#long words
l=fl.read().split()
print(l)
lw=len(max(l,key=len))
for i in l:
    if len(i)==lw:
        print(i)


#-------User Input-------#
#write Data
fl=open('longword2.txt','w')
data=input('Enter Data:')
fl.write(data)


#Read Data & find long Word
fl=open('longword2.txt','r')
l=fl.read().split()
print(l)
lw=len(max(l,key=len))

for i in l:
    if len(i)==lw:
        print(i)