# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Alon Parag
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*':0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    def firstComponent(word):
        lowerWord = str.lower(word)
        score = 0
        for letter in lowerWord:
            score+= SCRABBLE_LETTER_VALUES[letter]
        return score
    def secondComponent(word, n):
        score1 = (7*len(word)-3*(n-len(word)))
        score2 = 1
        return score1 if score1>score2 else score2
    
    try:
        total_score=firstComponent(word)*secondComponent(word, n)
        assert total_score>= 0
    except AssertionError:
        print('Error, score is negative')
    except:
        print('unexpected error has occured')
    else:
        return total_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    hand_str = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
             hand_str +=letter+' '      # print all on the same line
    return hand_str

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    assert n>=0, ('Error, Integer must be non negative')
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*'] = 1
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    assert isinstance(hand, dict), ('Error, hand must be instance of dict')
    calculating_hand = dict.copy(hand)
    new_hand = {}
    word = str.lower(word)
    for letter in word:
        if letter in calculating_hand:
            if calculating_hand[letter] <= 0:
                continue
            else:
                calculating_hand[letter] -= 1
    for key in calculating_hand.keys():
        if calculating_hand[key]>0:
            new_hand[key] = calculating_hand[key]
    return dict.copy(new_hand)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    
    word_lower = ''
    for letter in word:
        try:
            word_lower+=str.lower(letter)
        except:
            word_lower+=letter

    def wildWordMatch(wildWord, otherWord):
        if len(wildWord) != len(otherWord): return False
        flag = True
        for i in range(len(wildWord)):
            if not wildWord[i] == '*':
                if not wildWord[i] == otherWord[i]:
                    flag = False
                    break
            elif wildWord[i] == '*':
                if not otherWord[i] in VOWELS:
                    flag = False
                    break
        return flag

    def wildWordInWorldList(wildWord,word_list):
        flag = False
        for word in word_list:
            if wildWordMatch(wildWord, word):
                flag = True
                break
        return flag

    def isInHand(word, hand):
        handCheck = dict.copy(hand)
        for letter in word:
            if not letter in handCheck.keys():
                print(letter, 'is not in the hand', handCheck.keys())
                return False
            elif handCheck[letter] == 0:
                return False
            else:
                handCheck[letter]-=1
        
        return True

    def isInWordList(word, word_list):
        if '*' in word:
            return wildWordInWorldList(word, word_list)
        else:
            return word in word_list

    return isInHand(word_lower, hand) and isInWordList(word_lower, word_list)

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    total = 0
    for val in hand.values():
        total+=val
    return total

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print('Current hand:', display_hand(hand))
        # Ask user for input
        user_word = input('Enter word, or "!!" to indicate that you are finished: ')
        # If the input is two exclamation points:
        if user_word == "!!":
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_word, hand, word_list):
                # Tell the user how many points the word earned,
                round_score = get_word_score(user_word, calculate_handlen(hand))
                print('"'+user_word+'" earned',round_score , 'points')

                # and the updated total score
                total_score += round_score
            # Otherwise (the word is not valid):
            elif not is_valid_word(user_word, hand, word_list):
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print('Total score for this hand:',total_score)
    # Return the total score as result of function
    return total_score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # 1. ask the user which letter the user wants to replace
    letter_to_replace = letter
    try:
    # 2. make sure that the user inputs
        #2a a valid letter
        assert str.isalpha(letter_to_replace)
        #2b of valid length
        assert len(letter_to_replace) == 1
        #2c and in hand
        assert str.lower(letter_to_replace) in hand.keys()
    except:
        return hand
    else:
        # 3. transform the case of the letter to lowercase
        letter_to_replace = str.lower(letter_to_replace)
        # 5. save the replaced letter and the quantity
        quantity = hand[letter_to_replace]
        #6. select a letter at random
        replacing_letter = ''
        if letter_to_replace in VOWELS: replacing_letter = random.choice(VOWELS)
        else: replacing_letter = random.choice(CONSONANTS)
        #7. while a replacing letter is in the current hand:
        while replacing_letter in hand.keys():
            #7a. select a letter at random
            if letter_to_replace in VOWELS: replacing_letter = random.choice(VOWELS)
            else: replacing_letter = random.choice(CONSONANTS)
        #8 remove the replaced letter
        new_hand = dict.copy(hand)
        del new_hand[letter_to_replace]
        #9 insert the replacing letter in the same quantity as the replaced letter
        new_hand[replacing_letter] = quantity
        #10 return the hand
        return new_hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # .1   ask the user to input a total number of hands and assign it to a variable
    #     .1a   check that the input is an int larger than 0
    rounds = 0
    while True:
        try:
            rounds = int(input('Enter total number of hands:'))
            if rounds < 1: raise ValueError
            break
        except:
            print('Error, please enter a positive integer.')
    # .2   assign a score counter for the game and initialize it to 0
    game_score = 0
    # .3   assign a flag for hand substitution to false
    is_hand_substitute = False
    # .4   assign a flag for hand replay to false
    is_hand_replay = False
    # .5   assign a current hand
    for i in range(rounds):
        hand = deal_hand(HAND_SIZE)
        print('Current hand:', display_hand(hand))
        print('is_hand_substitute:', is_hand_substitute)
        if not is_hand_substitute:
    # .6   ask the user if they want to substitute one letter
            if input('Would you like to substitute a letter? ') == 'yes':
    #     .6a   if the input is 'yes':
    #     .6b   ask the user for a letter to replace
                hand = substitute_hand(hand, input('Which letter would you like to replace:'))
    #     .6c   replace letter and assign it to the hand
    #     .6d   assign replace flag to True
                print('Hand')
                is_hand_substitute = True
    # .7   assign a round score with play_hand()
                print('is_hand_substitute: after', is_hand_substitute)

        round_score = play_hand(hand, word_list)
    # .8   ask the user if he would like to replay the hand
        print('is_hand_replay:', is_hand_replay)
        if not is_hand_replay:
    #     .8a   if input is 'yes'
            if input('Would you like to replay the hand? ') == 'yes':
    #     .8b   assign replay flag to True
                is_hand_replay = True
    #     .8c   assign a replay score with play_hand()
                replay_score = play_hand(hand, word_list)
    #     .8d   if replay_score is more than round_score:
                if replay_score > round_score:
    #         .8d1   assign round_score to replay score
                    round_score = replay_score
    # .9   add the hand score to the total score
        print('is_hand_replay after:', is_hand_replay)
        game_score += round_score
    # .10   return the total score
    print('Total score over all hands:', game_score)
    return game_score


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
