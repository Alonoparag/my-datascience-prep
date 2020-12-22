import pytest
from lib.hangman import *
from .hangman_test_cases import *


def assertion(f_return, case_result):
    print('function returns', f_return)
    print('case result is', case_result)
    print('==V==')
    return 'PASSED' if f_return == case_result else 'FAILED<<<<<<<<<<<<!!!!!!!!!!!'

def test_is_word_guessed(case: dict):
    print('======\nTesting function: is_word_guessed\n=====')
    cases = case.values()
    for i in cases:
        print('Asserting is_word_guess with', i['name'],
        '\nword is:', i['word'],
        '\nletters are:', i['letters'],
         '\nresult should be:', i['result'],
         '\n test', assertion(is_word_guessed(i['word'],i['letters']), i['result']),
         '\n=======')


def test_get_guessed_word(case: dict):
    print('======\nTesting function: get_guessed_word\n=====')
    cases = case.values()
    for i in cases:
        print('Asserting get_guessed_word with', i['name'],
        '\nword is:', i['word'],
        '\nletters are:', i['letters'],
         '\nresult should be:', i['result'],
         '\n test', assertion(get_guessed_word(i['word'],i['letters']), i['result']),
         '\n=======')

def test_get_available_letters(case: dict):
    print('======\nTesting function: get_available_letters\n=====')
    cases = case.values()
    for i in cases:
        print('Asserting get_available_letters with', i['name'],
        '\nletters are:', i['letters'],
         '\nresult should be:', i['result'],
         '\n test', assertion(get_available_letters(i['letters']), i['result']),
         '\n=======')


test_is_word_guessed(is_word_guessed_case)
test_get_guessed_word(get_guessed_word_case)
test_get_available_letters(get_available_letters_case)