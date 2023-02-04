print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# contribution = (bill * (1 + (tip / 100))) / people
# print(f"Each person should pay: {round(contribution, 2)}")

contribution = "{:.2f}".format((bill * (1 + (tip / 100))) / people)
print(f"Each person should pay: {contribution}")


