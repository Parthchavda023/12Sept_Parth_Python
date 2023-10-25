
def gpay():
    
    #----- login step
    print("Press 1 for login New account")
    import random       # For OTP
    print('Press 2 for you have already login account')
    while True:
        choice=int(input("Enter your Choice(1/2):- "))

        #---- Login new account
        if choice==1:

            # Mobile Nuber
            while True:
               mnum=(input("Enter Your Mobile Number: +91"))
               if mnum.isdigit() and len(mnum)==10:
                   print(f"sent OPT in your Mobile Number +91{mnum}")
                   break    #Your Mobile Numbe
               else:
                   print('Please Enter Valiad Mobile Number')

            while True:
               #OTP Number
               opt=random.randint(1000,9999)
               print('OTP Number:-',opt)
               eotp=int(input(f'Ente OTP Number if sent your Mobile Number +91{mnum}/nEnter OTP:-'))    
               if eotp==opt:
                   print('Your Mobile Number Login Successfuly in G-Pay')
                   break    #OTP Numbe
               else:
                   print("Please enter valid OTP Number")

        #---Already login Account
        elif choice==2:


                mnm=int(input("Enter Mobile Number: +91"))
                if mnm==1234567890:
                    while True:
                        pas=int(input('Enter Password:-'))

                        if pas==2204:
                            global bal
                            bal=5005.24

                            print('\n----More Option----\n')
                            print('Press 1 for Bank Profile Details')
                            print('Press 2 for Check Bank Balance & Show Transaction History')
                            print('Press 3 for Transfer Money')
                            print('Press 4 for Show QR Code')

                            while True:
                                op=int(input('Enter your option:'))

                                if op==1:   #Bank Profile Details
                                    print("Account Holder Name:-Mr. Parth Chavda")
                                    print('Account Number:-12345678910')
                                    print('IFSC Code:- SBIN0124523')
                                    print('UPI ID:- 1234567890@xyz')
                                    print("Clear Balance:",bal)

                                elif op==2: #Check Bank Balance & Show Transaction History
                                    print('Bank Balance=',bal)
                                    print('----Transaction History----')
                                    fl=open('bank.txt','r')
                                    th=fl.read()
                                    print(th)

                                elif op==3: #Transfer Money
                                    print('Press 1 for Transfer Money to UPI')
                                    print('Press 2 for Transfer Money to Bank Details')
                                    tm=int(input('How do you want to transfer money?:'))

                                    if tm==1:   #Transfer Money to UPI
                                        import datetime

                                        dta=datetime.datetime.now()
                                        up=input('Enter UPI ID:')
                                        am=int(input('Enter Amout:'))
                                        unm=str(input('Enter Name:'))

                                        while True:
                                            pin=int(input('Enter UPI Pin:'))
                                            if pin==2204:
                                                print(f'{am}/- is successfuly Transfer.')
                                                fl=open('bank.txt','a')
                                                fl.write(f'Name:{unm}\tRS.{am}\t{dta}-With UPI={up}\n')
                                                break   # UPI Pin:
                                            else:
                                                print('Incorrect UPI PIN, Please Enter Correct PIN')
                                    
                                    elif tm==2: #Transfer Money to Bank Details
                                       
                                        bn=int(input('Enter Bank Account Number:'))
                                        while True:
                                            en=int(input('Re-enter Bank Account Number:'))
                                            if bn==en:
                                                ifsc=input('Enter IFSC code:')
                                                nm=str(input('Enter Bank Holder Name:'))
                                                tam=int(input('Enter Amount:'))
                                                while True:
                                                    import datetime
                                                    dt=datetime.datetime.now()
                                                    pn=int(input('Enter G-Pay Pin:'))
                                                    if pn==2204:
                                                        print(f'{tam}/- is successfuly Transfer')
                                                        fl=open('bank.txt','a')
                                                        fl.write(f'Name:{nm}\tRS.{tam},{dt}-With Bank account number={en}\n')
                                                        break
                                                    else:
                                                        print('Enter Correct Pin')
                                                        
                                                break   #Re-enter Bank Account Number
                                            else:
                                                print('Bank account number does not match')

                                elif op==4: #Show QR Code
                                    import pyqrcode
                                    link='upi://pay?pa=chavdaparth022@oksbi&pn=carry ff&aid=uGICAgICLwtuHCg'
                                    sp=pyqrcode.create(link)
                                    sp.png('G-PAY QR.png')  #btw You can pay😁😅
                                    print('G-PAY QR.png is saved in your folder.')
                                    print('Scan And Pay!!!')
                                    break   # your option
                                else:
                                    print('Invalid Option Choice,Please try Again...')
                                    
                            
                            break   # Password
                        else:
                            print("Password is Uncorrect")
                            print('Please try again!!!')
                            

                else:
                    print(f'No account available from this Mobile Number +91{mnm}')
                    print("Please create a new account")
                    print('Tahnk You !!!')
                
                # break   # your Choice(1/2)

        else:
            print('Please Enter Valiad Choice...')
            print('Try again !!!')


gpay()