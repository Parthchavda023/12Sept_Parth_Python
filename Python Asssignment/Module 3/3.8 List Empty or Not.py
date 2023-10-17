'''Write a Python program to check a list is empty or not. '''


# p=[10,'Parth',20,'Sanjay',30,'Vipul']
# p=[]
# print(len(p))

# if len(p)==0:
#     print("List is Empty...")
# else:
#     print("List is Not Empty...")

#--------User input-----#

p=[]
n=int(input('Enter Number of Range:-'))

for i in range(n):
    s=input("Enter Value in a list:")
    p.append(s)

print(p)
print(len(p))

if len(p)==0:
    print("List is Empty...")
else:
    print("List is Not Empty...")

'''
#--------NOTE_----------#
-> Ahi output ma Range 0 apso to  list Empty j print thse.
-> pan jo tema range 0 sivay biji Value apso to len() e list ma avel 
space ni pan lenght ne count kri lese jethi list ma value na api 
hoy to pan list not empty print thse.
'''