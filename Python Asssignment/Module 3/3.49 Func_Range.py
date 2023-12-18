'''Write a Python function to check whether a number is in a given range'''


# def rangenum(start,num,end):
#     if num in range(start,end+1):
#         print('The Number in Range')
#     else:
#         print("out of Range")

# rangenum(1,15,20)


#-----User inout-----#

def rangenum(start,num,end):
    if num in range(start,end+1):
        print('The Number in Range')
    else:
        print("out of Range")

ststart=int(input("Enter Start Range:"))
stnum=int(input("Enter Number:"))
stend=int(input("Enter End Range:"))
rangenum(ststart,stnum,stend)
