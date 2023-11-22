import re

unm=input('Enter Username:')
sp="[A-Z]+[a-z]+[0-9]"

unm_mod=re.findall(sp,unm)

if unm_mod:
    print('Valid Username...')
else:
    print('Error!!!')