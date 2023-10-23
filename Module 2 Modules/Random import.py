import random

# p=random.random()   # 0 to 1 only float value
# p=random.randint(1,1000)   # je te range ni value
# p=random.randrange(1111,9999,140)   #je te value thi je te range mate

# print(p)

# p=['Parth','Sanjay','Vipul','Prakash','Mehul','Pankaj']
# s=random.choice(p)    #list mathi random value choice krva
# print(s)

p=['Parth','Sanjay','Vipul','Prakash','Mehul','Pankaj']
random.shuffle(p)   # list na value ne shuffle krva like index change krva
print(p)
