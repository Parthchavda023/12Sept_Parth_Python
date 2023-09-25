a=int(input("Enter Subject 1 marks:"))
b=int(input("Enter Subject 2 marks:"))
c=int(input("Enter Subject 3 marks:"))
d=int(input("Enter Subject 4 marks:"))

total=(a+b+c+d)
print("Total Marks=",total)

per=total/4
print("Percenage=",per)

if 70<=per:
    print("Result= Dis.")
elif 60<=per:
    print("Result=First Class")
elif 50<=per:
    print("Result=Second Class")
elif 40<=per:
    print("Result=Pass")
else :
    print("Result=Fail")