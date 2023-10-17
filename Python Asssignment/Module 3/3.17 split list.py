'''Write a Python program to split a list into different variables.
like:-
input:['parth','sanjay']

output:
parth
sanjay
        '''


# p=['Parth','sanjay']
# print(p)

# for i in p:
#     print(i)

#----user input----#

p=[]
n=int(input('Enter Number of Range:'))

for i in range(n):
    s=input('Enter Value:')
    p.append(s)
    
print(p)

for i in p:
    print(i)