''' Write a Python program to map two lists into a dictionary.

important note:-The lengths of keys and values must be the same 
                when you use the zip() method.'''

# p=[101,102,103,104]
# s=['Parth','Sanjay','Vipul','Prakash']


# print(p)
# print(s)
# sp=dict(zip(p,s))
# print(sp)


#----user input-----#

p=[]
s=[]
n=int(input('Enter number of Range:'))

for i in range(n):
    dic1=input("Enter Keys of Dic1:")
    p.append(dic1)

for j in range(n):
    dic2=input("Enter Value of Dic2:")
    s.append(dic2)

print(p)
print(s)
sp=dict(zip(p,s))
print(sp)