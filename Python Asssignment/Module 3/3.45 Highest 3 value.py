  '''Write a Python program to find the highest 3 values in a dictionary.'''


# p={'a':100,'c':200,'e':300,'b':400,'f':500,'h':200,'j':100}

# print(p)
# s=(list(sorted(p.values())))
# print(s)
# print("Highest 3 Value:",s[-3:]) 


#------user input-------#

p={}
n=int(input('Enter Number of Range:'))

for i in range(n):
    key=input("Enter Key:")
    Value=input('Enter Value:')
    p[key]=Value

s=list(sorted(p.values()))
print(s)
print("Highest 3 Value:",s[-3:]) 