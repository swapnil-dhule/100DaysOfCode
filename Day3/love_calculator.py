# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

count1 = 0
count2 = 0

for i in name1.upper():
    if i == "T" or i == "R" or i == "U" or i == "E":
        count1 = count1 + 1
for i in name2.upper():
    if i == "T" or i == "R" or i == "U" or i == "E":
        count1 = count1 + 1

for i in name1.upper():
    if i == "L" or i == "O" or i == "V" or i == "E":
        count2 = count2 + 1
for i in name2.upper():
    if i == "L" or i == "O" or i == "V" or i == "E":
        count2 = count2 + 1

count1 = count1 * 10

score = count1 + count2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

