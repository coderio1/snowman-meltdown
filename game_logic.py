import random
from ascii_art import STAGES

# List of secret words
WORDS = ["waffles", "pancake", "snowball", "snowman", "skiing", "backpack", "sunglasses", "headphones", "orange", "melon"]


def get_random_word():
    """Selects a random word from the WORDS list"""

    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and underscores for secret word"""

    # show current snowman stage
    print(STAGES[mistakes])

    # build the word display: show letter if guessed, else underscore
    word_display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print(f"Word: {word_display}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Mistakes: {mistakes} / {len(STAGES) - 1}")
    print()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = set()

    # Game loop
    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # validation for a single letter input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}', try again!\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"'{guess}' is in the word!\n")
        else:
            print(f"'{guess}' is not in the word!\n")
            mistakes += 1

        # win condition check
        if all(letter in guessed_letters for letter in secret_word):
            print(f"You won! The word was: {secret_word}")
            break
    else:
        # Game over
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Game Over!\nThe secret word was: {secret_word}")


def ask_replay():
    """prompts user to repeat the game"""

    while True:
        answer = input("Do you want to play again? (yes/no): ").lower().strip()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please enter yes or no.")