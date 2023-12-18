'''Write a Python program to count the occurrences of each word in a given sentence'''


str=input("Enter your String:-")
l=input("Enter Word:-")
str.split()
count=0
for i in range(len(str)):
    if (l==str[i]):
        count+=1
print("count of word is:- ",str.count(l))