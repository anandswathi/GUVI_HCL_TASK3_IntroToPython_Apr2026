# Importing all files required for Python Task-3
import guess_the_number_game
import word_scramble_game

# Main file containing main function calls for all required modules
def main():
    print("--------------------------------------------------------------------")
    print("                     TASK 3 - GUESS THE NUMBER GAME                    ")
    print("--------------------------------------------------------------------")
    guess_the_number_game.main() # Calling main from guess_the_number_game module
    print("-----------------------------xxxxxxxxxx-----------------------------\n\n")

    print("--------------------------------------------------------------------")
    print("                     TASK 3 - WORD SCRAMBLE GAME                    ")
    print("--------------------------------------------------------------------")
    word_scramble_game.main() # Calling main from word_scramble_game module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

if __name__ == "__main__":
    main()