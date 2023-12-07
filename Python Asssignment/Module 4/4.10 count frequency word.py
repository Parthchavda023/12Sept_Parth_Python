'''Write a Python program to count the frequency of words in a file.'''


# from collections import Counter
# fl=open('std.txt','w')

# fl.write("Hi...!")
# fl.write("\nMy Name Is Parth")
# fl.write("\nMy Name Is Parth")

# def word_count(std):
#     with open(std) as fl:
#         return Counter(fl.read().split())
    
# print("The frequency of word in the File:-",word_count("std.txt"))



# #===========================================================#
# from typing import Counter
# fl=open("std.txt",'r')

# sp=fl.read().split()
# print(Counter(sp))


#------User Input-------#
from typing import Counter

fl=open("std2.txt",'w')
n=int(input("Enter Number of Range:"))

for i in range(n):
    data=input("Enter File data:")
    fl.write(data +"\n")


fl=open("std2.txt",'r')
sp=fl.read().split()
print("The frequency of word in the File:-",Counter(sp))
