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

a = int(input("What's the first number?: "))
print(f"+\n-\n*\n/")
operation = input("Pick an operation: ")
b = int(input("What's the next number?: "))
loop = "y"

while loop == "y":
    output = operations()
    print(f"{a} {operation} {b} = {output}")
    loop = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    if loop == "y":
        a = output
        operation = input("Pick an operation: ")
        b = int(input("What's the next number?: "))
        