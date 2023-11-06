ui=0
nm=''

try:
    def signup():
        global ui,nm
        
        fl=open('signup.txt','w')
        ui=input('Enter User Id:')
        nm=input('Enter Name:')
        ct=input('Enter City Name:')
        mn=input('Enter Mobile Number:')

        fl.write(f'ID={ui}\nName={nm}\nCity Name={ct}\nMobile Number={mn}\n')

    def login():
        print('\nEnter Your Login Details:-')
        Ui=input('Enter Your User ID=')
        Nm=input('Enter Your Name=')

        if ui==Ui and nm==Nm:
            fl=open('signup.txt','r')
            print('\n')
            print(fl.read())
        else:
            print('Invalid Data... plz try again ')

    signup()
    login()
except Exception as e:
    print(e)
