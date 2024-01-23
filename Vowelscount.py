'''Given a string, count and print the number of vowels (a, e, i, o, u) in it.'''
my_string = "Hello World"
vowels = "aeiouAEIOU"
vowels_count = 0

for char in my_string:
    if char in vowels:
        vowels_count += 1

print("The NUmber of vowels: ", vowels_count)


my_vowel = "Hello Everyone Good Morning. How is everyone doing today."
vowels ="aeiouAEIOU"
vowel_count = 0

for char in my_vowel:
        if char in vowels:            
            vowel_count += 1

print(f"The number of ocurances of {vowels}: {vowel_count}  ")
