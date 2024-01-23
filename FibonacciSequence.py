'''Print the first 10 numbers in the Fibonacci sequence.'''
def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2,n):
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence
    

n = int(input("Enter an Integer: "))

result = fibonacci(n)

print(f" The fibonacci sequence for first {n} numbers is : {result} ")