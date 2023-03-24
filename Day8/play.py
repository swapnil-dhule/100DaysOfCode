def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}?")


# greet_with(
#     name = "Swapnil",
#     location = "Pune"
# )

n = input("What's your name?")
l = input("What's your location?")
greet_with(location = l, name = n)