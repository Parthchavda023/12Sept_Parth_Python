'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''


s='Parth'
p='Chavda'
# Before Swap
print("Before Swap:",s+" "+p) #Parth Chavda

sp=p[:2]+s[2:]
ps=s[:2]+p[2:]
# After Swap
print("After Swap:-",sp+" "+ps)    #Chrth Paavda
