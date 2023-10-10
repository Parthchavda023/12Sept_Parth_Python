'''What is the purpose continue statement in python?'''

i=0

#Without Continue statement
# while(i<10):
#     i+=1
#     print(i)

#With Continue Statement
# while(i<10):
#     i+=1
#     if i==5:
#         continue
#     print(i)

# #===================================#
# #Without Continue statement
# for i in range(11):
#     print(i)

#With Continue Statement
for i in range(11):
    if i==5:
        continue
    print(i)