def gpay():
    #----- login step
    print("Press 1 for login New account")
    import random       # For OTP
    print('Press 2 for you have already login account')
    choice=int(input("Enter your Choice(1/2):- "))

    #---- Login new account
    if choice==1:
         
        # Mobile Nuber
        while True:
           mnum=(input("Enter Your Mobile Number: +91"))
           if mnum.isdigit() and len(mnum)==10:
               print(f"sent OPT in your Mobile Number +91{mnum}")
               break
           else:
               print('Please Enter Valiad Mobile Number')
            
        while True:
           #OTP Number
           opt=random.randint(1000,9999)
           print('OTP Number:-',opt)
           eotp=int(input(f'Ente OTP Number if sent your Mobile Number +91{mnum}/nEnter OTP:-'))    
           if eotp==opt:
               print('Your Mobile Number Login Successfuly in G-Pay')
               break
           else:
               print("Please enter valid OTP Number")

    #---Already login Account
    elif choice==2:
            
            mnm=int(input("Enter Mobile Number: +91"))
            if mnm==9328553159:
                while True:
                    pas=int(input('Enter Password:-'))

                    if pas==2204:
                        print("Account Holder Name:-Mr. Parth Hasmukhbhai Chavda")
                        print('Account Number:-12345678910')
                        print('IFSC Code:- SBIN0124523')
                        print("Clear Balance: 50012.35")
                        break

                    else:
                        print("Password is Uncorrect")
                        print('Please try again!!!')

            else:
                print(f'No account available from this Mobile Number +91{mnm}')
                print("Please create a new account")
                print('Tahnk You !!!')
 
gpay()
