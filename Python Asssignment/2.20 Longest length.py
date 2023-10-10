'''Write a Python function that takes a list of words and returns the length
of the longest one.'''

# p=('parth','prakash','raj','pankaj')
# a=len(p[0])
# b=p[0]

# for i in p:
#     if len(i)>a:
#         a=len(i)
#         b=i

# print("longest word:",b)
# print(f"{b} length is {a}")

#--------User list input---------#

p=[]
n=int(input("Enter number of range:"))

for i in range(n):
    nm=input("Enter Name:-")
    p.append(nm)

print(p)

a=len(p[0])
b=p[0]
for i in p:
    if len(i)>a:
        a=len(i)
        b=i

print(p)
print("longest word:",b)
print(f"{b} length is {a}")