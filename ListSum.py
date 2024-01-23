'''Calculate and print the sum of elements in a list.'''
def sum_of_list():

    my_list = (2,3,4,5,6)

    sum_of_list = 0

    for elements in my_list:
        sum_of_list += elements

    print(" The Sum of elements of the list is : ", sum_of_list)

sum_of_list()