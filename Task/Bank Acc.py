
def opac():
    global acnum,nm,actyp
    import random
    acnum=random.randint(100000000000,999999999999)
    print('Account Number:',acnum)
    nm=str(input("Enter Your Name:"))
    while True:
        print('Press S for Saving Account')
        print('Press C for Current Account')
        actyp=str(input('Select Account Type(S/C):'))
        if actyp.upper()=='S':
            print('Your account Type is Saving Acoount')
            break
        elif actyp.upper()=='C':
            print('Your account Type is Current Account')
            break
        else:
            print("Error!!! Please Press S/C ")
            
def dpam():
    global dp
    while True:
        dp=int(input('Enter Deposite Amount:'))
        if dp<2500:
           print('Please enter minimunm 2500/- amount')
        else:
            print(f'{dp}/- Rupees is successfully Deposited')
            break

def wdam():
    global wd
    t=dp
    print(f'You have {t}/- RS. in your account')
    while True:
        wd=int(input("Enter Amount You Want To Withdraw:"))
        cbal=t-wd
        wdbl=t-2500
        if cbal<2500:
            print(f'Your account balance is {t}/-, you cannot withdraw {wd} rupees because You have to keep at least 2500/- rupees in the account,You can withdraw up to {wdbl} rupees')
        else:
            print(f'{wd}/- RS. is Successfully Withdra')
            break

def st():
    print('Account Number:-',acnum)
    print("Account Holder Name:-",nm)
    if actyp.upper()=='S':
        typ=('Saving account')
    else:
        typ=('Current account')
    print('Account Type:-',typ)
    print('Total Balance:-',dp-wd)
    
opac()
dpam()
wdam()
st()