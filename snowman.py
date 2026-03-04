import random
from snowman_stages import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the secret word with underscores for unguessed letters."""
    # Show current snowman stage
    print(STAGES[mistakes])

    # Build the word display: show letter if guessed, else underscore
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

        # Validate input
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

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"You won! The word was: {secret_word}")
            break
    else:
        # Game over — show final melted stage
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Game over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()