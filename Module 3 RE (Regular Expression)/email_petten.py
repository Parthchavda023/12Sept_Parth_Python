import re

email=input('Enter Email Address:')

email_mod="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,}$"

email_add=re.findall(email_mod,email)

if email_add:
    print('Valid email address')
else:
    print('Error !!!')