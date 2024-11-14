# Name:         Sofia Mancini
# Class:        CSC 110 - Spring 2024
# Assignment:   Programming Project Design
# Due Date:     03/29/2024

# Program Title: Wordle Design

# Program Description: 
# ---------------------
# This program will generate a random 5 letter word and then the player will make guesses based on clues provided by the program.
# The program will keep track of the score and provide clues to the user.

# General Solution:
# -----------------
# Continuously compare the users guesses ot a randomly generated 5 letter word.
# Provide clues to the user based on their guesses and keep track of the score.

# Pseudocode:
# ----------
# Have the program generate a random 5 letter word
# Ask the user for their first guess
# Check that the word is in the list
# Check that the word hasn't been guessed before
# Keep track of the guesses and provide clues
#  - If the letter is in the word, in the correct location, return a 'G'
#  - If the letter is in the word, but in the wrong location, return a 'Y'
#  - If the letter is not in the word, display a 'X'
# Display the clues
# Keep track of the number of guesses
# If the word is not guessed in 6 tries print 'Word not found' and the word
# If the word is guessed print 'Nice Job'
# Display the score and ask the user if they would like to play again
# Scoring scheme: score = number of guesses
# If not guessed score = 10
# ** Make sure score does not reset until user stops playing **


# Function Design:
# ----------------

# Function to open the file and check the given file name
def openFile():
    # Open the file and check the given file name
    return dataFile

# Function to read in the data from the file and store in a list
def getData ():
    # Read in the data from the file and store in a list
    return wordList

# Function to generate a random 5 letter word
def generateWord():
    # Generate a random 5 letter word
    return word

# Function to get the user's guess
def getGuess():
    # Ask the user for their guess
    # If the word is not in the list, ask the user to try again, this is not counted as a guess
    # If the word has been guessed before, ask the user to try again, this is not counted as a guess
    # Store the first good guess in an empty list and count it as a guess
    return guess

# Function to keep track of the guesses and provide clues
def computeClues(word, guess):
    # Create an empty string to store the clues
    # If the letter is in the word, in the correct location, return a 'G'
    # If the letter is in the word, but in the wrong location, return a 'Y'
    # If the letter is not in the word, display a 'X'
    # Display the clues
    return clue

# Function to keep track of the score
def computeScore(guesses):
    # Keep track of the number of guesses
    # Display the score and ask the user if they would like to play again
    # Scoring scheme: score = number of guesses
    # If not guessed score = 10
    # Score counts until user stops playing (can go multiple rounds)
    return score

# Function to print the results of the game
def printResults(word, guess):
    # If the word is not guessed print 'Sorry, you did not guess the word: + word'
    # If the word is guessed print 'Congratulations, your wordle score for this game is: + score'
    # Display the score and ask the user if they would like to play again
    return

# Main Function:
def main ():
    # Call the other functions
    return