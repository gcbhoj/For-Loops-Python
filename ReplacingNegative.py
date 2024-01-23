'''Write a program to replace negative numbers in an array with 0.'''

def replacing_negative_numbers():
    for element in array:
        if element >= 0 :
            my_array.append(element)
        else:
            my_array.append(0)

    return my_array

array = [-1,2,3,-5,4,3,-8]
my_array = []

result = replacing_negative_numbers()

print(result)