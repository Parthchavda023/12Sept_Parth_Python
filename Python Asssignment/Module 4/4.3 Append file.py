'''Write a Python program to append text to a file and display the text.'''

# #Append
# print('Append Data:')
# fl=open('Append.txt','a')
# fl.write('Hello Friends\n')
# fl.write("I'm Parth Chavda\n")
# fl.write('How are you?\n')
# #Display
# print('Display Data:')
# fl=open('Append.txt','r')
# print(fl.read())


#-------User input-------#
fl=open('Append2.txt','a')
n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    fl.write(f'{id}-{nm}\n')

print('Display Data:')
fl=open('Append2.txt','r')
print(fl.read())
