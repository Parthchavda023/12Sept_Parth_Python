print("\nWith Temporary Variable:")
a=10
b=20

print("Before swap:")
print("A=",a)
print("B=",b)

# c=a
# a=b
# b=c
# print("Aftter swap with Temporary Variable:")
# print("A=",a)
# print("B=",b)

#=====================
print("\nAfter swap Without Temporary Variable:")
a,b=b,a
print("A=",a)
print("B=",b)