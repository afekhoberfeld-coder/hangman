import os

# Hangman ASCII art (welcome)
welcome_art = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(welcome_art)
print("Welcome to Hangman!")

# Ask for the file path
file_input = input("Enter the path (without .txt): ").strip()
file_path = file_input + ".txt"

# Check if file exists
if not os.path.exists(file_path):
    print(f"File '{file_path}' not found!")
    exit()

# Load words from the file
with open(file_path, "r") as f:
    words = [line.strip() for line in f if line.strip()]

if not words:
    print("The file is empty!")
    exit()

# Ask player to choose a word number
print(f"\nThe file contains {len(words)} words.")
while True:
    try:
        choice = int(input(f"Choose a number between 1 and {len(words)}: "))
        if 1 <= choice <= len(words):
            break
        else:
            print("Number out of range. Try again.")
    except ValueError:
        print("Please enter a valid number.")

# Pick the chosen word
word = words[choice - 1].lower()
guessed = set()
lives = 6

print(f"\nYou chose word #{choice}. Let's play!")
print("It has", len(word), "letters.")

# Game loop
while lives > 0:
    display_word = " ".join([letter if letter in guessed else "_" for letter in word])
    print("\nWord:", display_word)
    print("Lives left:", lives)
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct!")
        if all(letter in guessed for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("Wrong!")
        lives -= 1

else:
    print("\n💀 Game Over! The word was:", word)
