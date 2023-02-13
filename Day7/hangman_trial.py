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

# Logic

word = random.choice(word_list)

alpha_list = []
for i in word:
    alpha_list.append(i)

print(alpha_list) 

count = 0

while(count < 7):

    letter = input("Guess a letter: ").upper()

    if letter not in alpha_list:
        print(f"\nYou guessed {letter}, that's not in the word. You lose a life.\n")
        count += 1
    
    else:
        for item in alpha_list.copy():
            if item == letter:
                alpha_list.remove(item)

        print(f"\nYou guessed {letter}, that's in the word. Good going!.\n")
        if len(alpha_list) == 0:
            count = 7

    if count == 1:
        print(hangmanpics[0])
    elif count == 2:
        print(hangmanpics[1])
    elif count == 3:
        print(hangmanpics[2])
    elif count == 4:
        print(hangmanpics[3])
    elif count == 5:
        print(hangmanpics[4])
    elif count == 6:
        print(hangmanpics[5])
    elif count == 7 and len(alpha_list) != 0:
        print(hangmanpics[6])


if len(alpha_list) > 0:
    print("\nYou lose!")

else:
    print("\nYou won!")