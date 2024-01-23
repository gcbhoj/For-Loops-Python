'''Write a program to calculate the factorial of a given number.'''

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a Positive Intiger: "))
if n < 0:
    print("Please Enter a Positive Intiger")
else:
    result = factorial(n)
    print(f'The factorial of {n} is {result} ')