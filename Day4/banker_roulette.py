# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count = len(names)
lucky = random.randint(1, count)

print(f"{names[lucky-1]} is going to buy the meal today!")