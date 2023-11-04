'''Write a Python program to read last n lines of a file.'''


# fl=open('Readlines2.txt','w')
# fl.write('101-Parth\n')
# fl.write('102-Sanjay\n')
# fl.write('103-Prakash\n')
# fl.write('104-Raj\n')
# fl.write('105-Om\n')
# fl.write('106-Rajveer\n')
# fl.write('107-Mehul\n')

# fl=open('Readlines2.txt','r')
# n=int(input('Enter Number of Last N Lines:'))
# s=(fl.readlines()[-n:])
# for i in s:
#     print(i)


#-----User input------#
fl=open('Readlinesuser.txt','w')
n=int(input('Enter Number Of range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    fl.write(f'{id}-{nm}\n')

fl=open('Readlinesuser.txt','r')
N=int(input('Enter Number of Last N Lines:'))
s=(fl.readlines()[-N:])
for i in s:
    print(i)