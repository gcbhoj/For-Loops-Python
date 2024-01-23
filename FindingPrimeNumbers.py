'''Write a program to identify and print all prime numbers in an array.'''
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num **0.5)+1):
        if num % i == 0:
            return False
        
    return True
    
def finding_prime_numbers(array):
    prime_array = [element for element in array if is_prime(element)]
    return prime_array

array = list(range(1, 20))

result = finding_prime_numbers(array)

print(result)
            