import random

# Small list of predefined words
word_list = ["apple", "tiger", "table", "green", "growth" , ]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Variables for game state
guessed_letters = []            # Letters guessed so far
max_attempts = 6                # Maximum incorrect guesses allowed
incorrect_guesses = 0           # Track how many wrong guesses made

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have {max_attempts} incorrect guesses allowed.\n")

# Main game loop
while True:
    # Display current progress of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word.strip())

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\n✅ Congratulations! You guessed the word:", secret_word)
        break

    # Check loss condition
    if incorrect_guesses >= max_attempts:
        print("\n❌ Out of guesses! The word was:", secret_word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.\n")
        continue

    # If letter already guessed
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.\n")
        continue

    # Add guess to guessed_letters list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}\n")
