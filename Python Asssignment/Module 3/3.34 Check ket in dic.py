'''Write a Python script to check if a given key already exists in a dictionary.
like:
{'Id':101,'nm':'Parth','sub':'Python'} #items
Id,nm,sub   #key
values=101,Parth,Python
'''


# p={'Id':101,'nm':'Parth','sub':'Python'}

# if 'id' in p.keys():
#     print("Key is already in Dictionary")
# else:
#     print('Key in not in Dictionary')


#----user input----#

p={}
n=int(input('Enter Number of Range:'))

for i in range(n):
    key=input("Enter Key:")
    value=input('Enter Value:')
    p[key]=value

print(p)

s=input("Enter name of key to be check=")

if s in p.keys():
    print("Key is already in Dictionary")
elif s in p.values():
    print("This is Values not a key")
else:
    print('Key in not in Dictionary')