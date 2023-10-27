fl=open('Datetime.txt','r')
# print(fl.read())
# print(fl.readline())
# print(fl.readlines())
# print(fl.readlines()[1:2])

# n=1
# for i in fl:
#     # print(i)
#     print(f"Line:[{n}]={i}")
#     n+=1

# if fl.readable():
#     print("Yes...File is readable...")
# else:
#     print("No...File is not readable!")


fl=open('Datetime.txt','r+')
fl.write("\nHello Python!")