# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
else:
    print("ERROR: Enter the correct size!")

if size == "S" and add_pepperoni == "Y":
    bill = bill + 2
elif size != "S" and add_pepperoni == "Y":
    bill = bill + 3
else:
    bill = bill + 0

if extra_cheese == "Y":
    bill = bill + 1
elif extra_cheese == "N":
    bill = bill + 0
else:
    print("ERROR: Enter only 'Y' or 'N' for Extra Cheese!")

print(f"Your final bill is: ${bill}.")