WELCOME_WORD = """
__        __   _                            _         
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
"""
print(WELCOME_WORD)
hangman_word = """
 _    _          _   _  _____ __  __          _   _ 
| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
"""
print(hangman_word)
word = "cat"
def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if not len(guess) == 1:
            print("single letter pls")
            continue
        if not guess.isalpha():
            print("no number only a single letter")
            continue
        return guess
print(f"that is a letter {get_guess()}")