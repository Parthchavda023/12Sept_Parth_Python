'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''


p=input("Enter String:")

if p.find('not')==p.replace('good') or p.find('poor')==p.replace('good') or p.find('not poor')==p.replace('good'):
    print(p)
else:
    not_idx = p.find('not')
    poor_idx = p.find('poor')
    if not_idx != -1 and poor_idx != -1 and poor_idx > not_idx:
        p = p.replace(p[not_idx:(poor_idx+4)], 'good')
    print(p)

# c=p.find('not')
# s=p.find('poor')

# if c<s:
#     print(p[:c]+'good')