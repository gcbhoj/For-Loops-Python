'''Write a program to count the number of odd numbers in an array.'''


    
count = 0
for numbers in range(1, 10):
        if numbers % 2 == 1:
            count += 1

print(f"{count}")