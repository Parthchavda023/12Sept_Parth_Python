try:
    id=int(input("Enter Id:"))
    nm=str(input('Enter Name:'))
    print(f'{ID}-{nm}')
except Exception as p:
    print(p)