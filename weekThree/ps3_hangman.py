# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret_list = list(secretWord)
    for letter in secret_list:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret_list = list(secretWord)
    secret_string = ""
    for letter in secret_list:
        if letter not in lettersGuessed:
            secret_string += "_ "
        else:
            secret_string += letter + " "
    return secret_string



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_string = ""
    available_letters = list(string.ascii_lowercase)
    for letter in available_letters:
        if letter not in lettersGuessed:
            available_string += letter
    return available_string


    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    remaining_guesses = 8
    lettersGuessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    while remaining_guesses > 0:
        print("-------------")
        print("You have", remaining_guesses, "left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        available_letters = list(getAvailableLetters(lettersGuessed))
        user_guess = input("Please guess a letter: ").lower()
        lettersGuessed.append(user_guess)

        if user_guess in available_letters and user_guess in list(secretWord):
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))

        elif user_guess not in available_letters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            remaining_guesses -= 1

        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break

        elif remaining_guesses == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secretWord + ".")
            break

        else:
            continue






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = "cake"
#chooseWord(wordlist).lower()
hangman(secretWord)
