''' Write python program that user to enter only odd numbers, else will raise an exception.'''


try:
    p=int(input('Enter Number:'))
    if p%2!=0:
        print(p)
    else :
        raise Exception
        
except:
    print('Error...!')