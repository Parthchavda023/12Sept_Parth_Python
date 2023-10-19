'''Write a Python script to print a dictionary where the keys are numbers between 1 and 15. '''


# p={}
# for i in range(1,16):
#     p[i]=i*i

# print(p)


#-------User input-----#

p={}
n=int(input('Enter Number 1 to 15:'))

if n<1 or n>15:
    print("Please enter number 1to15 !!!")
else:
    for i in range(1,n+1):  #(1,n+1) = 1 thi start kri ne n+1 sudhi
        p[i]=i*i
    print(p)