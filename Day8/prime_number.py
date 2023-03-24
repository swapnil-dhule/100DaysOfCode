#Write your code below this line 👇
def prime_checker(number):
    result = []
    for i in range(2,n):
        if n%i == 0:
            result.append(1)
        else:
            result.append(0)
    
    if n == 2:
        print("It's a prime number.")
    elif n == 1:
        print("It's not a prime number.")
    elif 1 in result:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
