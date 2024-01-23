'''Calculate and print the sum of squares of numbers from 1 to 5.'''

sum_of_squares = 0

for numbers in range(1, 6):
    square = numbers ** 2
    sum_of_squares += square

    print("The Sum of squares is : ", sum_of_squares)