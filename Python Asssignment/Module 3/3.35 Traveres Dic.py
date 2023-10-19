'''How Do You Traverse Through A Dictionary Object In Python?
like:
#inpt:
{'id':101,'nm':'Parth','sub':'Python'}

#output
id-101
nm-Parth
sub-Python
'''

# p={'id':101,'nm':'Parth','sub':'Python'}

# print(p)
# for i,j in p.items():
#     print(i,'-',j)


#----user input----#

p={}
n=int(input("Enter number of Range:"))

for i in range(n):
    key=input('Enter Key=')
    value=input("Enter Value=")
    p[key]=value

print(p)

for i,j in p.items():
    print(i,'-',j)