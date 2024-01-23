import random

random_number = random.randint(1, 100)

fortune_number = random.randint(1,3)
fortune_text = ""

if(fortune_number == 1):
    fortune_text = "You will have a great day"
if(fortune_number == 2):
    fortune_text = "You will have a tough day"
if(fortune_number == 3):
    fortune_text = "YOu will be happy today"

print(f"{fortune_text}\n Your Lucky Number is: {random_number}")



