'''Write a program to reverse the elements of an array and count the number of elements that does not match the original array.'''


my_array = [5,1,2,3,10,25,65,99,50]

sorted_my_array = sorted(my_array)

print(sorted_my_array)

reversed = my_array[::-1]

print(reversed)
count =0
for i in range(len(my_array)):
    if my_array[i] != sorted_my_array[i]:
        count += 1

print(f"{count}")