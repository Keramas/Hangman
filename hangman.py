#!/usr/bin/python3

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():

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

    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:
        if i not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):

    guessString = ""
    for c in secretWord:
        if c in lettersGuessed:
            guessString += c
        else:
            guessString += "_ "

    return guessString


def getAvailableLetters(lettersGuessed):

    letterstring = 'abcdefghijklmnopqrstuvwxyz'
    letterlist = []

    availableLetters = ""

    for i in letterstring:
        letterlist.append(i)

    for i in lettersGuessed:
        if i in letterlist:
            letterlist.remove(i)

    for i in letterlist:
        availableLetters += i

    return availableLetters
    

def hangman(secretWord):

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-----------")
    lettersGuessed = []
    round = 8
    gameActive = True
    while gameActive and not isWordGuessed(secretWord, lettersGuessed):
        availableLetters = getAvailableLetters(lettersGuessed)
        print("You have " + str(round) + " guesses left.")
        print("Available letters:", availableLetters)
        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            round -= 1
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))

        print("-----------")

        if getGuessedWord(secretWord, lettersGuessed) == secretWord and round > 0:
            print("Congratulations, you won!")
        elif round == 0:
            gameActive = False
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")



secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
