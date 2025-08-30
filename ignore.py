
TITLE = """
__        __  _                            _           _                                            
\ \      / / | |                          | |         | |                                           
 \ \ /\ / /__| | ___ ___  _ __ ___   ___  | |_ ___    | |__   __ _ _ __   __ _ _ __ ___   __ _ ___ 
  \ V  V / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` / __|
   \_/\_/  __/ | (_| (_) | | | | | |  __/ | || (_) |  | | | | (_| | | | | (_| | | | | | | (_| \__ \\
        \___|_|\___\___/|_| |_| |_|\___|  \__\___/   |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|___/
                                                                         __/ |                      
                                                                        |___/                       
"""


HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()


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


def main():
    print(TITLE)

    word = "castle"
    guessed_letters = []
    lives = 6

    while True:
        print(HANGMAN_PICS[6 - lives])
        print(display_progress(word, guessed_letters))

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}\n")


        if all(letter in guessed_letters for letter in word):
            print(display_progress(word, guessed_letters))
            print("Congratulations! You won!")
            break


        if lives <= 0:
            print(HANGMAN_PICS[6])
            print(f"You lost! The word was '{word}'.")
            break


if __name__ == "__main__":
    main()