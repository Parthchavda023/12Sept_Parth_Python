'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''


p=input("Enter String:")

c=p.find('not')
s=p.find('poor')

if c<s:
    print(p[:c]+'good')