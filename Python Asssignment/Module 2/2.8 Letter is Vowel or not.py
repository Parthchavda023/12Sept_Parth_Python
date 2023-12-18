'''Write a Python program to test whether a passed letter is a vowel or not.'''


p=input("Enter Letter:")
p.lower()

if  p=="a" or p=="e" or p=="i" or p=="o" or p=="u":
    print(f"Letter {p} is Vowel")
else :
    print(f"Letter {p} is not Vowel")