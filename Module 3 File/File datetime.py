import datetime

fl=open('Datetime.txt','a')

n=int(input('Enter Number of Range:'))
for i in range(n):
    id=int(input('Enter Id:'))
    nm=str(input('Enter Name:'))
    dt=datetime.datetime.now()

    fl.write(f'{id}-{nm},{dt}\n')