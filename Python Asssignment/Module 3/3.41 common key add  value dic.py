'''Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). '''


# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':400}

# print(d1)
# print(d2)

# for i in d1.keys():
#     if i in d2.keys():
#         d1[i]=d1[i]+d2[i]
#     d2[i]=d1[i]

# print('Counter:',d2)

# sp=dict(sorted(d2.items()))  #Dict ne sirt kri a-z ma print krva
# print('Counter(Sort):',sp)


#--------Impor Counter Modules-----------#

from collections import Counter

d1={'a':200,'b':800,'c':300}
d2={'a':300,'b':200,'d':400}

print(d1)
print(d2)
sp=Counter(d1)+Counter(d2)
print('Counter:',sp)

ps=dict(sorted(sp.items()))   #Dict ne sirt kri a-z ma print krva
print('Counter(sort):',ps)