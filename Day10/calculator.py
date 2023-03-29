def operations():
    if operation == "+":
        result = a+b
        return result
    elif operation == "-":
        result = a-b
        return result
    elif operation == "*":
        result = a*b
        return result
    elif operation == "/":
        result = a/b
        return result

import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

a = int(input("What's the first number?: "))
print(f"+\n-\n*\n/")
operation = input("Pick an operation: ")
b = int(input("What's the next number?: "))


while True:
    output = operations()
    print(f"{a} {operation} {b} = {output}")
    loop = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    
    if loop == "y":
        a = output
        operation = input("Pick an operation: ")
        b = int(input("What's the next number?: "))
    elif loop == "n":
        os.system('cls')
        print(logo)
        a = int(input("What's the first number?: "))
        print(f"+\n-\n*\n/")
        operation = input("Pick an operation: ")
        b = int(input("What's the next number?: "))



