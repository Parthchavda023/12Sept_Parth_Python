firstnm=input("Enter First Name:")
lastnm=input("Enter Last Name:")

if firstnm.isalpha() and lastnm.isalpha():
    print("Done ! Enter Your Username and Password")
    usnm=input("Enter Your Username:")

    if usnm.isalnum():

        pas=input("Enter Your Password:")

        if pas.isalnum() and len(pas)<=8:
            mn=input("Enter Your Mobile Number: +91 ")

            if mn.isdigit() and len(mn)==10:
                    print("\nYour Form has been successfully Submited...")
                    print("Thank you!!!")
            else :
                print("Error, plz check your Mobile Number and try again...")

        else :
            print("Error, Plz Enter Valid Password...")

    else :
        print("Error, Plz enter Valid username...")

else :
    print("Error, plz enter valid Name...")