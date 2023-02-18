import random

word_list = [ "POOL", "MAMA", "EGG", "FIRE", "ARM", "SUN", "DINNER", "FREE", "HORSE", "BOOK", "ICE", "SEA", "HOME", "CROSS", "FUNNY" ]

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 7

chosen_word = random.choice(word_list)

print(f"Test - {chosen_word}")

display = []

for i in chosen_word:
    display.append("_")

print(display)

counter = 0

while "_" in display:
    index_display = 0
    guess = input("Guess a letter: ").lower()
    for i in chosen_word:
        if guess == i:
            display[index_display] = i
        index_display += 1
    
    if guess not in chosen_word:
        lives -= 1
        counter += 1
        print(f"Counter is {counter}")

    if counter > 0:
        print(hangmanpics[counter-1])

    if lives == 0:
        print("You lose!")
        exit()
    
    print(display)

print(f"You win!")