'''Write a Python function that checks whether a passed string is palindrome or not '''


def pelindrome():
    p=input("Enter Data:")
    s=p.lower()
    
    if s[0]==s[-1]:
        print("String is Pelindrome")
    else:
        print("String is not Palindrome")

pelindrome()