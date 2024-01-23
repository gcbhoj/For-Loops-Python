'''Write a program to multiply each element in an array by a given factor.'''

def array_multiplication(array, n):
    result =[]
    for element in array:
        result.append(element * n)
    return result


array = list(range(1, 20))
n = int(input("Enter a number to multiply the array with: "))

result = array_multiplication(array, n)

print(result)

