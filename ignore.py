# -------------------------
# Hangman Game
# -------------------------

# Function to display the word progress
def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()

# Function to get a valid guess from the player
def get_guess(previous_guesses):
    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue

        if guess in previous_guesses:
            print("You already guessed that letter.")
            continue

        return guess

# Main function
def main():
    word = "castle"          # The secret word
    guessed_letters = []     # List of letters the player guessed
    lives = 6                # Number of allowed wrong guesses

    print("Welcome to Hangman!")
    print(display_progress(word, guessed_letters))

    while True:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        print(display_progress(word, guessed_letters))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won!")
            break

        # Check lose condition
        if lives <= 0:
            print(f"You lost! The word was '{word}'.")
            break

# Run the game
if __name__ == "__main__":
    main()