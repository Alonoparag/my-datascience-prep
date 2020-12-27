

import pytest
from ps4a import get_permutations
from ps4c import *

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting Vegetarians'),'Converting Vegetarians', True),
    (SubMessage('Into the system!'),'Into the system!', True),
    (SubMessage('Converting Vegetarians'),'', False),
    (SubMessage('Into the system!'),'Into the system!', False)
    ])
@pytest.mark.skip
def test_get_message_text(input_value, return_value, expected):
    if expected:
        assert input_value == return_value
    else:
        assert input_value != return_value

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting Vegetarians'),['Converting',' Vegetarians'], True),
    (SubMessage('Into the system!'),['Into','the','system!'], True),
    (SubMessage('Converting Vegetarians'),'', False),
    (SubMessage('Into the system!'),'', False)
    ])

@pytest.mark.skip
def test_get_valid_words(input_value, return_value, expected):
    if expected:
        assert input_value == return_value
    else:
        assert input_value != return_value

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting Vegetarians'),{
    'A':"U",
    'E':"A",
    'I':"E",
    'O':"I",
    'U':"O",
    'a':"u",
    'e':"a",
    'i':"e",
    'o':"i",
    'u':"o"
}, True),
    (SubMessage('Into the system!'),{
    'A':"E",
    'E':"I",
    'I':"O",
    'O':"U",
    'U':"A",
    'a':"e",
    'e':"i",
    'i':"o",
    'o':"u",
    'u':"a"
}, True),
    (SubMessage('Converting Vegetarians'),'', False),
    (SubMessage('Into the system!'),'', False)
    ])

@pytest.mark.skip
def test_build_transpose_dict(input_value, return_value, expected):
    if expected:
        assert input_value == return_value
    else:
        assert input_value != return_value

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting Vegetarians'),'', True),
    (SubMessage('Into the system!'),'', True),
    (SubMessage('Converting Vegetarians'),'', False),
    (SubMessage('Into the system!'),'', False)
    ])

@pytest.mark.skip
def test_apply_transpose(input_value, return_value, expected):
    if expected:
        assert input_value == return_value
    else:
        assert input_value != return_value

# @pytest.mark.parametrize('',[])
@pytest.mark.skip
def test_decrypt_message(input_value, return_value, expected):
    if expected:
        assert input_value == return_value
    else:
        assert input_value != return_value