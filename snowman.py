from game_logic import play_game, ask_replay

if __name__ == "__main__":
    while True:
        play_game()
        if not ask_replay():
            print("Thanks for playing. Goodbye!")
            break
