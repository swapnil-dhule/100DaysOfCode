# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = 60 * 365 
wks = 60 * 52
mnths = 60 * 12

x = days - (int(age) * 365)
y = wks - (int(age) * 52)
z = mnths - (int(age) * 12)

print(f"You have {x} days, {y} weeks, and {z} months left.")