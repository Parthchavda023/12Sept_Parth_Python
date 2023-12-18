'''Write a Python program to convert a list of characters into a string.
like p,a,r,t,h = parth '''



# p=['P','a','r','t','h']
# print('Without join:- ',p)

# # Join List
# s=''.join(p)
# print('join:-',s)

#--------user input-------#

p=[]
n=int(input("Enter Number of Range:"))

for i in range(n):
    i+=1
    s=input(f'Enter Character {i}:')
    p.append(s)

print("Join:","".join(p))