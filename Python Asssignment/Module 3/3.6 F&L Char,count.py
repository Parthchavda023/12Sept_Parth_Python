'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings. '''


# p=['level', 'hello', 'world', 'madam', 'racecar']
# str=0

# for i in p: 
#     if len(i)>=2 and i[0]==i[-1]:
#         str+=1

# print('String:-',str)

#-------User Input---------#

p=[]
count=0
n=int(input("Enter Number od string:"))

for i in range(n):
    s=input("Emter String Name:")
    p.append(s)

print(p)
 
for j in p:
    if len(j)>=2 and j[0]==j[-1]:
        count+=1
    
print(count)