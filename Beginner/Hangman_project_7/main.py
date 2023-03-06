#Hangman game - Project 7
#import necessary modules
import random
from hangman_art import logo, stages
from hangman_words import word_list

def play_hangman():
    #count lives
    lives = 5

    #randomise choice of word in list
    word = random.choice(word_list)

    word_length = len(word)

    #list to store correctly guessed letters
    guessed_letters = []

    #adds underscore character to list for visuals 
    for i in range(word_length):
        guessed_letters.append("_")
    print(f"The letters are: \n\n{guessed_letters}\n")

    #testing print line, delete for real game
    print(f"There are {word_length} letters\n")


    #While the guessed_letters variable is not equal to the word, keep looping
    while guessed_letters != list(word):
        #input for letter
        while True:
            user_choice = input("Please enter a single letter: ")
            if not isinstance(user_choice, str):
                print("Invalid input: Please enter a letter")
            elif len(user_choice) != 1:
                print("Invalid input: Please enter a single letter")
            elif not user_choice.isalpha():
                print("Invalid input: Please enter a letter")
            else:
                break

        #logic to check if guessed letter is in the word, and if so replace the index in the list
        if user_choice in word:
            for position in range(word_length):
                if user_choice == word[position]:
                    guessed_letters[position] = user_choice
        #if guessed letter is not in the word, print hanged man and remove a life
        else:
            print(stages[lives])
            lives -= 1
        print(guessed_letters)
        #if you run out of lives, then the game ends
        if lives < 0:
            print("\n------------------")
            print("You lost, better luck next time!\n")
            print(f"The word was {word}")
            print("------------------\n")
            break
    #Game won if you guessed all letters correctly
    else:
        print("\n------------------")
        print("YOU WON!")
        print("------------------\n")

# Hangman game replay function
def replay():
    while True:
        # Ask player if they want to play again
        play_again = input("Do you want to play? (Y/N)\n").lower()
        
        # Check if player input is valid
        if play_again == 'y' or play_again == 'yes':
            # Return True to play again
            return True
        elif play_again == 'n' or play_again == 'no':
            # Return False to exit game
            return False
        else:
            # Invalid input, ask again
            print("Invalid input, please enter 'y' or 'n'.\n")
            continue

#Start game
game_status = True
while game_status:
    play_hangman()
    game_status = replay()
