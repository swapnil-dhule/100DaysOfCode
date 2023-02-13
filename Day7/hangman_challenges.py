import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Test - {chosen_word}")

guess = input("Guess a letter: ").lower()

display = []


for i in chosen_word:
    # if guess == i:
    #     print("Right")
    # else:
    #     print("Wrong")
    display.append("_")

# print(display)

while "_" not in display:
    index_display = 0
    for i in chosen_word:
        if guess == i:
            display[index_display] = i
        index_display += 1

print(display)