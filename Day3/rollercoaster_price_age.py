height = int(input("What is your height in cm? "))

if height > 120:
    age = int(input("What is you age? "))
    if age > 18:
        print("You can ride and you need to pay $12.")
    elif age < 18 and age > 11:
        print("You can ride and you need to pay $7.")
    else:
        print("You can ride and you need to pay $5.")
else:
    print("Sorry kid! You can't ride.")