"""How will you compare two lists?"""

# p=[10,20,30]
# s=[10,30,20]
# # s=[11,21,31]

# p.sort()
# print(p)
# s.sort()
# print(s)

# if p==s:
#     print('List are Same...')
# else :
#     print('List are not Same...')

#------User input---------#

p=[]
s=[]

n=int(input("Enter number of Range 1:-"))
for i in range(n):
    x=input("Enter Your Value:-")
    p.append(x)

print('\n')

N=int(input("Enter number of Range 2:-"))
for j in range(N):
    y=input("Enter Your Value:-")
    s.append(y)

p.sort()
print(p)
s.sort()
print(s)

if p==s:
    print('List are Same...')
else :
    print('List are not Same...')