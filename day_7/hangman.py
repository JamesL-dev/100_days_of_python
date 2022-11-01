import random
from hangman_art import stages, logo
from hangman_words import word_list

display = []
player_lives = len(stages) - 1
end_of_game = False

# Randomly choose a word from the word_list and assign
# assign it a variable called chosen_word
random_word = random.choice(word_list)
word_length = len(random_word)

# Fill display with blanks
for letter in random_word:
    display.append("_")
print(random_word)
print(display)

# Game Loop
while(end_of_game == False):
# Ask the user to guess a letter and assign their answer to a varaible called guess. Make guess
# lowercase
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in random_word:
        print(f"You guess {guess}, that's not in the word. You lose a life.")
        player_lives -= 1
        if player_lives == 0:
            end_of_game = True
            print("You Lose.")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[player_lives])

