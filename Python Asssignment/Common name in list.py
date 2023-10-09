'''Write a Python function that takes two lists and returns true if they have
at least one common member. '''



p=['Parth','Sanjay','Vipul']
s=['Mehul','Pankaj','Parth']

for i in p:
    if i in s:
        print("True...")
        break
    else:
        print('False..')
        break