"""
Word Scramble

Concept: The player has to unscramble a jumbled word from the words given in a list format as:

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

Key Elements:
    String Manipulations: Scramble and unscramble words.
    Conditions: Check if the player’s guess matches the original word.
    Loops: Allow multiple attempts to guess the word.
"""
import random # Import random module for selecting and shuffling words

# Word list
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

def computer_guess():
    """
    Function to select random word from list of words
    Input: None
    Output: word_to_be_guessed(String)
    """
    words_list = words # Global value words assigned in local scope
    word_to_be_guessed = random.choice(words) # Pick random word from list of words
    return word_to_be_guessed

def scramble_word(word):
    """
    Function to create scrambled word from a given word
    Input: word(String)
    Output: scrambled_word(String)
    """
    word_list = list(word) # Converting word to list of char
    random.shuffle(word_list) # Shuffle elements randomly in word_list
    scrambled_word = "".join(word_list) # Join char to generate scrambled word
    return scrambled_word

def play_game():
    """
    Main Function to play the game flow
    Input: None
    Output: None
    """
    # Select a random word from the list
    unscrambled_word = computer_guess()

    # Scramble the selected word
    scrambled_word = scramble_word(unscrambled_word)

    # Attempt count to calculate the no. of attempts until success
    attempt_count = 0

    # Allowed attempt limit
    attempt_limit = 3

    print("Scrambled word: ", scrambled_word)
    print("Attempts Allowed: {}".format(attempt_limit))

    # while condition to check user guesses the word correctly within limited attempts
    while attempt_count < attempt_limit:

        # Get the player guess
        player_guess = input("\nYour turn to guess: ").lower()
        attempt_count += 1
        if player_guess == unscrambled_word:
            print("Yay! You guessed the word correctly in {} attempts!".format(attempt_count))
            break
        else:
            print("OOPS!!! Wrong guess. Try again")
            player_guess = input("Your guess: ").lower()
            attempt_count += 1
            attempt_limit = attempt_limit - 1
    else:
        print("\n You Lost!!!...Better luck next time! ")

    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == "y":

        # Recursive call if the player wants to play again
        play_game()
    else:
        print("\nExiting Game...")
        print("\n\n             Thanks for playing!...Goodbye                \n\n")

def main():
    print("\n\n         **********Welcome to Word Scramble Game!**********          \n\n")
    play_game()

# Run the game
if "__main__" == __name__:
    main()

