import pytest
import unittest.mock as mock
from lib.hangman import *
from .hangman_test_cases import *

def test_is_word_guessed_():
    cases = is_word_guessed_case.values()
    for i in cases:
        assert is_word_guessed(i['word'], i['letters'])==i['result'] 

def test_is_word_guessed_tact():
    assert is_word_guessed('tact', ['a','s','t'])

def test_get_guessed_word_():
    cases = get_guessed_word_case.values()
    for i in cases:
        assert get_guessed_word(i['word'],i['letters']) == i['result']

def test_get_available_letters_():
    cases = get_available_letters_case.values()
    for i in cases:
         assert get_available_letters(i['letters'])==i['result']

# def test_win():
#     rounds = case_win.values()
#     for r in rounds:
#         if not r['round'] == 'finish':
#             assert guesses_left == r['guesses_left'], 'Error wrong number of left guesses in ' + r['round']
#             assert available_letters == r['available_letters'], 'Error, wrong string of available letters in ' + r['round']
#             with mock.patch.object(__builtins__, 'input', lambda: r['letter_guessed']):
#                 assert output == r['response'], 'Error, wrong response in ' + r['round']
#         else:
#             assert is_word_guessed, 'Error, word should be guessed'
#             assert calculate_score == r['game_score'], 'Error, wrong game score'

# def test_lost():
#     rounds = case_lost.values()
#     for r in rounds:
#         if not r['round'] == 'finish':
#             assert guesses_left == r['guesses_left'], 'Error wrong number of left guesses in ' + r['round']
#             assert available_letters == r['available_letters'], 'Error, wrong string of available letters in ' + r['round']
#             with mock.patch.object(__builtins__, 'input', lambda: r['letter_guessed']):
#                 assert output == r['response'], 'Error, wrong response in ' + r['round']
#         else:
#             assert output == r['response']

