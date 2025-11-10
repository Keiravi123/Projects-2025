import random  # For random numbers

while True:
    magic_number = random.randint(1, 10)
    print("Hello! Let's play a game to guess the magic number between 1 and 10.")
    attempts = 0

    while True:
        guess = input("Type a number between 1 and 10: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            print("That is not a valid number. Please try again.")
            continue

        attempts += 1

        if guess == magic_number:
            print(f"Great! You guessed the number in {attempts} attempts.")
            break
        elif guess < magic_number:
            print("Too low, try a higher number.")
        else:
            print("Too high, try a lower number.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing! Goodbye!")
        break
