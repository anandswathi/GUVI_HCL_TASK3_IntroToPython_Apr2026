"""
Guess the Number

Concept: The computer randomly selects a number within a range, and the player has to guess it.

Key Elements:
    Variables: Store the random number and the player’s guess.
    Conditions: Check if the guess is too high, too low, or correct.
    Loops: Allow multiple guesses until the correct number is found.
"""
import random # Import random module for random selection
# Define range globally
start_index = 0
end_index = 11

def random_num_generator():
    """
    Function to generate a random number between specific ranges.
    Input: None
    Output: random number between specific ranges(Int)
    """

    # Pick a random number between defined range
    random_num = random.randint(start_index, end_index)
    return random_num

# Game Logic method
def play_game():
    """
    Main function controlling the game flow and containing the game logic
    Input: None
    Output: None
    """
    # Select a random number
    random_num = random_num_generator()

    # Attempt count to calculate the no. of attempts until success
    attempt_count = 0

    print("Secret number has been selected")
    print("Guess number between {} and {}".format(start_index, end_index))

    # Get the player guess
    player_guess = int(input("Enter your guess: "))
    attempt_count += 1
    # while condition to check until user guesses the number correctly
    while player_guess != random_num:
        print("Sorry!!! Wrong guess. Try again")
        player_guess = int(input("Your guess: "))
        attempt_count += 1
    else:
        print("Yay! You guessed the number correctly in {} attempts!".format(attempt_count))


def main():
    print("\n\n        ***** Welcome to Guess The Number Game!*****         \n\n")
    play_game()
    print("\nExiting Game...")
    print("\n\n             Thanks for playing!...Goodbye                \n\n")

# Run the game
if __name__ == "__main__":
    main()
