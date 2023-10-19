fl=open('StudentInfo.txt','a')

n=int(input("Enter Number Of Student:"))

for i in range(n):
    id=int(input("Enter Id="))
    nm=str(input('Enter Name='))
    fl.write(f'Id={id}\nName={nm}\n')

#-------Using Function------#
# def stdinf():
#     fl=open('StudentInfo.txt','a')

#     n=int(input("Enter Number Of Student:"))
#     for i in range(n):
#         id=int(input("Enter Id="))
#         nm=str(input('Enter Name='))
#         fl.write(f'Id={id}\nName={nm}\n')
    
# stdinf()