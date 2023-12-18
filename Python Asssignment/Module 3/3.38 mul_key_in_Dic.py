'''Write a Python program to check multiple keys exists in a dictionary.'''

# p={'id':101,'Name':'Parth',"Sub":'Python',"ad":'Halvad'}
# # p={'id':101}

# s=p.keys()
# print(s)
# print(len(s))

# if len(s)>1:
#     print("Dictionary have multipal keys")
# else:
#     print("Dictionary has singal/zero key")


#------user input------#

p={}
n=int(input('Enter Number of Range:'))

for i in range(n):
    key=input('Enter key=')
    value=input("Enter value=")
    p[key]=value

print(p)
s=p.keys()
print(s)
print(len(s))

if len(s)>1:
    print("Dictionary have multipal keys")
else:
    print("Dictionary has singal/zero key")
