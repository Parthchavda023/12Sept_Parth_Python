'''Write a python program to find the longest words in file.'''


fl=open('Longest.txt','w')
fl.write("Hello I'm Parth Chavada")


fl=open('Longest.txt','r')
p=(fl.read())
print(p)
print((str(p.split())))
a=len(p[0])
b=p[0]
for i in p:
    if len(i)>a:
        a=len(i)
        b=i

print(p)
print("longest word:",b)
print(f"{b} length is {a}")