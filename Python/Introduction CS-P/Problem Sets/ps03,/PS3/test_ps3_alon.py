import pytest_mock
import pytest
import ps3

word_list = ps3.load_words()

def count_vowels(hand):
    counter = 0
    for key in hand.keys():
        if key in ps3.VOWELS:
            counter +=1
    return counter

def count_consonants(hand):
    counter = 0
    for key in hand.keys():
        if key in ps3.CONSONANTS:
            counter +=1
    return counter

def test_substitute_hand_exists():
    assert callable(ps3.substitute_hand)

def test_substitute_hand_changes_letter():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    assert  not ps3.substitute_hand(hand, 'r').keys() == hand.keys(), 'Error, keys were not changed'

def test_substitute_hand_keeps_quantity():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    letter = 'r'
    changed_hand = ps3.substitute_hand(hand, 'r')
    replacing_letter = ''
    for key in changed_hand.keys():
        if not key in hand.keys():
            replacing_letter = key
            break
    assert hand[letter] == changed_hand[replacing_letter], 'Error, substitue_hand changed the quantity of the letter while changing'

def test_substitute_hand_keeps_other_letters():
    def hand_without_letter(hand, letter):
        """
        Assumes
            hand is a dict with alphabetic letters as keys
            letter is a str of a single alphabetic charachter
        Returns a list without the provided letter
        """
        list_keys = [*hand]
        list_keys.remove(letter)
        return list_keys

    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    letter = 'r'
    changed_hand = ps3.substitute_hand(hand, 'r')
    replacing_letter = ''
    for key in changed_hand.keys():
        if not key in hand.keys():
            replacing_letter = key
            break
    hand_keys = hand_without_letter(hand, letter)
    changed_hand_keys = hand_without_letter(changed_hand, replacing_letter)
    assert hand_keys == changed_hand_keys, 'Error, substitue_hand changed the quantity of the letter while changing'

def test_substitute_hand_valid_letter_consonant():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    assert  count_consonants(ps3.substitute_hand(hand, 'r')) == count_consonants(hand)


def test_substitute_hand_valid_letter_vowel():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    assert  count_vowels(ps3.substitute_hand(hand, 'a')) == count_vowels(hand) 
   

def test_substitute_hand_invalid_letter():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    assert hand == ps3.substitute_hand(hand, '*'), 'Error, Key was replaced with invalid input'
   

def test_substitute_hand_letter_not_in_hand():
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    assert hand == ps3.substitute_hand(hand, 'b'), 'Error, letter was replaced with a letter not in hand.keys()'
   

def test_play_game_exists():
    callable(play_game)

def test_play_game_no_substitute_no_replay():

    pass

def test_play_game_substitute_no_replay():
    pass

def test_play_game_no_substitute_replay():
    pass

def test_play_game_substitute_replay():
    pass
