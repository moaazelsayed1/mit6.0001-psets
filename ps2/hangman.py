# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, true if all the letters of secret_word are in letters_guessed;
      false otherwise
    '''
    #secret_word = 'apple'
    #letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # fill in your code here and delete "pass"
    found = 0
    for char in secret_word:
        for i in range(len(letters_guessed)):
            if char == letters_guessed[i]:
                found += 1
                break
    return found == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    so_far = list(secret_word)
    for j in range(len(secret_word)):
        found = False
        for i in range(len(letters_guessed)):
            if secret_word[j] == letters_guessed[i]:
                found = True
        if found == False:
            so_far[j] = "_ "
    return ''.join(so_far)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remain = list(string.ascii_lowercase)
    for i in letters_guessed:
        for j in remain:
            if i == j:
                remain.remove(j)
                break
    return ''.join(remain)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    #secret_word = 'else'
    print("""Welcome to the game Hangman!
I am thinking of a word that is {0} letters long.""".format(len(secret_word)))
    guessed = list()
    #warned = list()
    left_guesses = 6
    warnings = 3

    while left_guesses > 0:
        print("""-------------
You have {0} guesses left.
Available letters: {1}""".format(left_guesses, get_available_letters(guessed)))

        char = input("Please guess a letter: ").lower()

        # validate user input and penalize invalid inputs
        # if char in warned:
        #    if warnings < 0:
        #        print(
        #            "Oops! You've already guessed that letter. You have no warnings left")
        #    else:
        #        print("oops! that is not a valid letter. you have {0} warnings left: {1}".format(
        #            warnings, get_guessed_word(secret_word, guessed)))
        #    continue

        if char.isalpha() == False:
            # warned.append(char)
            warnings -= 1
            if warnings < 0:
                left_guesses -= 1
                print(
                    "Oops! that is not a valid letter. You have no warnings left so you lose one guess: {0}".format(get_guessed_word(secret_word, guessed)))
            else:
                print("oops! that is not a valid letter. you have {0} warnings left: {1}".format(
                    warnings, get_guessed_word(secret_word, guessed)))
            continue

        if char in guessed:
            # warned.append(char)
            warnings -= 1
            if warnings < 0:
                left_guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {0}".format(
                    get_guessed_word(secret_word, guessed)))
            else:
                print("Oops! You've already guessed that letter. You have {0} warnings left: {1}".format(
                    warnings, get_guessed_word(secret_word, guessed)))
            continue

        guessed.append(char)
        if guessed[-1] in secret_word:
            print("Good guess: {0}".format(
                get_guessed_word(secret_word, guessed)))
        else:
            print("Oops! That letter is not in my word: {0}".format(
                get_guessed_word(secret_word, guessed)))
            left_guesses -= 1
            if guessed[-1] in "aeiou":
                left_guesses -= 1
        if is_word_guessed(secret_word, guessed) == True:
            print("""------------
Congratulations, you won!
Your total score for this game is: {0}""".format(left_guesses*len(set(secret_word))))
            break
    else:
        print("""-----------
Sorry, you ran out of guesses. The word was {0}.""".format(secret_word))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == "_" and other_word[i] in my_word:
            return False
        elif my_word[i] == "_":
            continue
        elif my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    counter = 0
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            counter += 1
            print(word)
    if counter == 0:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #secret_word = "apple"
    print("""Welcome to the game Hangman!
I am thinking of a word that is {0} letters long.""".format(len(secret_word)))
    guessed = list()
    #warned = list()
    left_guesses = 6
    warnings = 3

    while left_guesses > 0:
        print("""-------------
You have {0} guesses left.
Available letters: {1}""".format(left_guesses, get_available_letters(guessed)))

        char = input("Please guess a letter: ").lower()

        # validate user input and penalize invalid inputs
        # if char in warned:
        #    if warnings < 0:
        #        print(
        #            "Oops! You've already guessed that letter. You have no warnings left")
        #    else:
        #        print("oops! that is not a valid letter. you have {0} warnings left: {1}".format(
        #            warnings, get_guessed_word(secret_word, guessed)))
        #    continue

        # showing matches to make it easier
        if char == "*":
            show_possible_matches(get_guessed_word(secret_word, guessed))
            continue

        if char.isalpha() == False:
            # warned.append(char)
            warnings -= 1
            if warnings < 0:
                left_guesses -= 1
                print(
                    "Oops! that is not a valid letter. You have no warnings left so you lose one guess: {0}".format(get_guessed_word(secret_word, guessed)))
            else:
                print("oops! that is not a valid letter. you have {0} warnings left: {1}".format(
                    warnings, get_guessed_word(secret_word, guessed)))
            continue

        if char in guessed:
            # warned.append(char)
            warnings -= 1
            if warnings < 0:
                left_guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {0}".format(
                    get_guessed_word(secret_word, guessed)))
            else:
                print("Oops! You've already guessed that letter. You have {0} warnings left: {1}".format(
                    warnings, get_guessed_word(secret_word, guessed)))
            continue

        guessed.append(char)
        if guessed[-1] in secret_word:
            print("Good guess: {0}".format(
                get_guessed_word(secret_word, guessed)))
        else:
            print("Oops! That letter is not in my word: {0}".format(
                get_guessed_word(secret_word, guessed)))
            left_guesses -= 1
            if guessed[-1] in "aeiou":
                left_guesses -= 1
        if is_word_guessed(secret_word, guessed) == True:
            print("""------------
Congratulations, you won!
Your total score for this game is: {0}""".format(left_guesses*len(set(secret_word))))
            break
    else:
        print("""-----------
Sorry, you ran out of guesses. The word was {0}.""".format(secret_word))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
