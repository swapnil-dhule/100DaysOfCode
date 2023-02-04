# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name_u = name.upper()

count1 = name_u.count("T") + name_u.count("R") + name_u.count("U") + name_u.count("E")
count2 = name_u.count("L") + name_u.count("O") + name_u.count("V") + name_u.count("E")


count1 = count1 * 10
score = count1 + count2


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

