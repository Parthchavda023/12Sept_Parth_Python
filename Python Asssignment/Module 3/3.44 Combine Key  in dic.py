'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd'''


p={'1': ['a','b'], '2': ['c','d']}

print(p)

for i in p['1']:
    for j in p['2']:
        print(i+j,end=' ')

