'''Write a program to find the maximum element in an array..'''

def maximum_element():
    
    my_array = [1,5,10,2,15,25,3,150,8]

    maximum_element = my_array[0]
    for element in my_array:
        if element > maximum_element:
            maximum_element = element

    return maximum_element

result = maximum_element()

print(f"The maximum element in the given array is : {result}")
        