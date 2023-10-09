'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''


square=[i**2 for i in range(1,31)]
    
print("First elements:",square[:5])  # First 5 elements
print("Last elements:",square[-5:])  # Last 5 elements