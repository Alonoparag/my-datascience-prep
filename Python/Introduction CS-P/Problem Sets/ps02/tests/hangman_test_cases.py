is_word_guessed_case = {
    'case1':{
        'name':'no recurring letters_pass',
        'word': 'world',
        'letters':['a','b','w','o','r','l','d'],
        'result': True
    },
    'case2':{
        'name':'no recurring letters_fail',
        'word': 'world',
        'letters': ['a','b','w','r','l','d'],
        'result': False
    },
    'case3':{
        'name':'recurring_letters_pass',
        'word': 'hello',
        'letters':['b','h','e','l','l','a','o'],
        'result': True
    },
    'case4':{
        'name': 'recurring letters_fail',
        'word': 'hello',
        'letters': ['b','h','e','l','l','a'],
        'result': False
    }
}

get_guessed_word_case = {
    'case1':{
        'name':'no letters guessed',
        'word': 'world',
        'letters':['a','b'],
        'result': '_ _ _ _ _'
    },
    'case2':{
        'name':'1 letter guessed (not recurring)',
        'word': 'world',
        'letters':['a','b','r'],
        'result': '_ _ r_ _'
    },
    'case3':{
        'name':'1 letter guessed (recurring)',
        'word': 'essence',
        'letters':['a','b', 's'],
        'result': '_ ss_ _ _ _'
    },
    'case4':{
        'name':'2 letter guessed (not recurring)',
        'word': 'world',
        'letters':['a','b','r','w'],
        'result': 'w_ r_ _'
    },
    'case5':{
        'name':'2 letter guessed (recurring)',
        'word': 'essence',
        'letters':['a','b','n', 's'],
        'result': '_ ss_ n_ _'
    },
    'case6':{
        'name':'n letter guessed (not recurring)',
        'word': 'world',
        'letters':['a','b','r','w', 'd'],
        'result': 'w_ r_ d'
    },
    'case7':{
        'name':'n letter guessed (recurring)',
        'word': 'essence',
        'letters':['a','b','n', 's','e'],
        'result': 'essen_ e'
    }
}

get_available_letters_case = {
    'case1':{
        'name':'letters in letters_guessed: 0',
        'letters':[],
        'result': 'abcdefghijklmnopqrstuvwxyz'
    },
    'case2':{
        'name':'letters in letters_guessed: 1',
        'letters':['f'],
        'result': 'abcdeghijklmnopqrstuvwxyz'
    },
    'case3':{
        'name':'letters in letters_guessed: 5',
        'letters':['f', 'h', 'd', 'e', 'n'],
        'result': 'abcgijklmopqrstuvwxyz'
    }
}
case_win = {
    'round1':{
        'round': 'call_number 1',
        'guesses_left':6,
        'available_letters': 'abcdefghijklmnopqrstuvwxyz',
        'letter_guessed':'a',
        'response':'Good guess: _ a_ _'
        },
    'round2':{
        'round': 'call_number 2',
        'guesses_left':6,
        'available_letters': 'bcdefghijklmnopqrstuvwxyz',
        'letter_guessed':'a',
        'response':'Oops! You\'ve already guessed that letter. You have 2 warnings left: _ a_ _'
        },
    'round3':{
        'round': 'call_number 3',
        'guesses_left':6,
        'available_letters': 'bcdefghijklmnopqrstuvwxyz',
        'letter_guessed':'s',
        'response':'Oops! That letter is not in my word. Please guess a letter: _ a_ _'
        },
    'round4':{  
        'round': 'call_number 4',
        'guesses_left':5,
        'available_letters': 'bcdefghijklmnopqrtuvwxyz',
        'letter_guessed':'$',
        'response':'Oops! That is not a valid letter. You have 1 warnings left: _ a_ _'
        },
    'round5':{
        'round': 'call_number 5',
        'guesses_left':5,
        'available_letters': 'bcdefghijklmnopqrtuvwxyz',
        'letter_guessed':'t',
        'response':'Good guess: ta_ t',
        },
    'round6':{
        'round': 'call_number 6',
        'guesses_left':5,
        'available_letters': 'bcdefghijklmnopqrtuvwxyz',
        'letter_guessed':'e',
        'response':'Oops! That letter is not in my word: ta_ t',
        },
    'round7':{
        'round': 'call_number 7',
        'guesses_left':3,
        'available_letters': 'bcdfghijklmnopqrtuvwxyz',
        'letter_guessed':'e',
        'response':'Oops! You\'ve already guessed that letter. You have 0 warnings left: ta_ t'
        },
    'round8':{
        'round': 'call_number 8',
        'guesses_left':3,
        'available_letters': 'bcdfghijklmnopqrtuvwxyz',
        'letter_guessed':'e',
        'response':'Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ta_ t'
        },
    'round9':{
        'round': 'call_number 9',
        'guesses_left':2,
        'available_letters': 'bcdfghijklnopquvwxyz',
        'letter_guessed':'c',
        'response':'Good guess: tact'
        },
    'end':{
        'round': 'finish',
        'response': 'Congratulations, you won! Your total score for this game is: 6',
        'game_score': 6
        }
}

case_lost = {
    'round1':{
        'round': 'call_number1',
        'guesses_left':6,
        'available_letters': 'abcdefghijklmnopqrstuvwxyz',
        'letter_guessed':'a',
        'response':'Oops! That letter is not in my word: _ _ _ _',
        },
    'round2':{
        'round': 'call_number2',
        'guesses_left':4,
        'available_letters': 'bcdefghijklmnopqrstuvwxyz',
        'letter_guessed':'b',
        'response':'Oops! That letter is not in my word: _ _ _ _',
        },
    'round3':{
        'round': 'call_number3',
        'guesses_left':3,
        'available_letters': 'cdefghijklmnopqrstuvwxyz',
        'letter_guessed':'c',
        'response':'Oops! That letter is not in my word: _ _ _ _',
        },
    'round4':{
        'round': 'call_number4',
        'guesses_left':2,
        'available_letters': 'defghijklmnopqrstuvwxyz',
        'letter_guessed':'2',
        'response':'Oops! That is not a valid letter. You have 2 warnings left: _ _ _ _',
        },
    'round5':{
        'round':'call_number5',
        'guesses_left':2,
        'available_letters': 'defghijklmnopqrstuvwxyz',
        'letter_guessed':'d',
        'response':'Oops! That letter is not in my word: _ _ _ _',
        },
    'round6':{
        'round': 'call_number6',
        'guesses_left':1,
        'available_letters': 'efghijklmnopqrstuvwxyz',
        'letter_guessed':'e',
        'response':'Good guess: e_ _ e',
        },
    'round7':{
        'round': 'call_number7',
        'guesses_left':1,
        'available_letters': 'fghijklmnopqrstuvwxyz',
        'letter_guessed':'f',
        'response':'Oops! That letter is not in my word: e_ _ e',
        },
    'end':{
        'round': 'finish',
        'response':'Sorry, you ran out of guesses. The word was else.'
        }
}