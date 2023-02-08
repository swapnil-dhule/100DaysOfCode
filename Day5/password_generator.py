import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(nr_letters):
    j = random.randint(0, len(letters)-1)
    password += letters[j]

for i in range(nr_symbols):
    j = random.randint(0, len(symbols)-1)
    password += symbols[j]

for i in range(nr_numbers):
    j = random.randint(0, len(numbers)-1)
    password += numbers[j]

# print(password)

final_password = ""

for i in range(0, len(password)):
    if i%2 != 0:
        final_password += password[i]

for i in range(0, len(password)):
    if i%2 == 0:
        final_password += password[i]

print(f"Here is your password: {final_password}")
