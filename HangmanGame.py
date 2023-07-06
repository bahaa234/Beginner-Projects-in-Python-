from WordsForHangmanGame import word_list 


import random
from termcolor import cprint, colored  #to color the text
import sys


def get_word():
    """Arbitrarily chooses a word from a module and assign it 
       to the variable word.
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    The logic of Hangman game
    
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(colored("Let's play Hangman!", "yellow","on_white",attrs=["bold"]))
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0: 
        guess = input("Please guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(colored(f"You already guessed the letter {guess}", "white", "on_red"))
            elif guess not in word:
                print(colored(f"{guess}, is not in the word!", "white", "on_red"))
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(colored(f"Good job, { guess } is in the word!","white", "on_green"))
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] # to know the index and its letter in a word for each iteration
                for index in indices:   #to replace each underscore with guess
                    word_as_list[index] = guess 
                word_completion = "".join(word_as_list) #to convert word_as_list back to a string
                if "_" not in word_completion: #checks if the guess complets the word
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(colored(f"You already guessed the word {guess}", "white", "on_red"))
            elif guess != word:
                print(colored(f"{guess} is not the word!", "white", "on_red"))
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(colored("Not a valid guess!", "white", "on_red"))
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(colored("Congrats, you guessed the word! You win!", "white", "on_green"))
    else:
        print(colored(f"Sorry, you ran out of tries. The word was  { word } . Maybe next time!", "white", "on_red"))


def display_hangman(tries):

    """
     kinda animated hangman shapes that diplays
     when the game start and for every guess

    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return colored(stages[tries],"blue")


def main(): #puts every thing together
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__": #this fragemnt will run by running our script on the command line
    main()                 #so you dont need to write a manual code to make it work

    
     






