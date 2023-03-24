# Global

ui = '''
::::'######:::::'###::::'########::'######:::::'###::::'########:::
:::'##... ##:::'## ##::: ##.....::'##... ##:::'## ##::: ##.... ##::
::: ##:::..:::'##:. ##:: ##::::::: ##:::..:::'##:. ##:: ##:::: ##::
::: ##:::::::'##:::. ##: ######:::. ######::'##:::. ##: ########:::
::: ##::::::: #########: ##...:::::..... ##: #########: ##.. ##::::
::: ##::: ##: ##.... ##: ##:::::::'##::: ##: ##.... ##: ##::. ##:::
:::. ######:: ##:::: ##: ########:. ######:: ##:::: ##: ##:::. ##::
::::::......:::..:::::..::........:::......:::..:::::..::..:::::..:
::::::'######::'####:'########::'##::::'##:'########:'########:::::
:::::'##... ##:. ##:: ##.... ##: ##:::: ##: ##.....:: ##.... ##::::
::::: ##:::..::: ##:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::
::::: ##:::::::: ##:: ########:: #########: ######::: ########:::::
::::: ##:::::::: ##:: ##.....::: ##.... ##: ##...:::: ##.. ##::::::
::::: ##::: ##:: ##:: ##:::::::: ##:::: ##: ##::::::: ##::. ##:::::
:::::. ######::'####: ##:::::::: ##:::: ##: ########: ##:::. ##::::
::::::......:::....::..:::::::::..:::::..::........::..:::::..:::::'''

# Function Definitions

def coder(message, shift, operation):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    if operation == "decode":
        alphabets.reverse()

    for i in message:
        if i in alphabets:
            my_index = alphabets.index(i)
            calc = my_index + shift
            if calc >= 26:
                new_index = (calc%26)+1
                result += alphabets[new_index]
            else:
                new_index = calc%26
                result += alphabets[new_index]
        else:
            result += i

    print(f"Here's the encoded result: {result}")

# Calling Function

loop = "yes"

print(f"{ui}\n")

while loop == "yes":
    
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

    if user_input == "encode":
        coder(
                message = input(f"Type your message:\n").lower(),
                shift = int(input(f"Type shift number:\n")),
                operation = "encode"
                )
        loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    elif user_input == "decode":
        coder(
                message = input(f"Type your message:\n").lower(),
                shift = int(input(f"Type shift number:\n")),
                operation = "decode"
                )
        loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    else:
        print("\nYou entered an invalid input. \nType Type valid input.\n")