'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

# p='w3resource'
# # p='Hello Parth'
# s={}

# for i in p:
#     if i in s:
#         s[i] += 1
#     else:
#         s[i] = 1

# print(s)


#----user input----#

p=input('Enter string:')
s={}

for i in p:
    if i in s:
        s[i]+=1
    else:
        s[i]=1

print(s) 