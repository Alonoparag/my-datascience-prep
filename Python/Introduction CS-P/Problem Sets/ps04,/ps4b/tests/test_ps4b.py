import pytest
from ps4b import *

word_list = load_words('./words.txt')
message_mock = Message('I\'m a test')
plaintext_mock = PlaintextMessage('I\'m a test', 5)



def test_message_get_message_text():
    """
    assumes no input message
    test the value of object of type Message method "get message text"
    """
    assert message_mock.get_message_text() == 'I\'m a test'
@pytest.mark.parametrize('messageObject, return_value, expected',[
    (Message('Hello'), ['Hello'], True),
    (Message('Hello dfghj'), ['Hello'], True),
    (Message('Hello dfghj'), ['Hello dfghj'], False),
    (Message('Hello dfghj'), ['Hello','dfghj'], False),    
])
def test_message_get_valid_words(messageObject, return_value, expected):
    """
    Tests message_object method get_valid words
    """
    if expected:
        assert messageObject.get_valid_words() == return_value
    else:
        assert messageObject.get_valid_words() != return_value

@pytest.mark.parametrize("shift, test_dict, expected",[
    (3,
     {'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W', 'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g', 'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'}, True),
     
    (5,
     {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E', 'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O', 'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U', 'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o', 'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u'}, True),
    (0,
     {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}, True),
     (6, {'A': 'U',    'B': 'V',    'C': 'W',    'D': 'X',    'E': 'Y',    'F': 'Z',    'G': 'A',    'H': 'B',    'I': 'C',    'J': 'D',    'K': 'E',    'L': 'F',    'M': 'G',    'N': 'H',    'O': 'I',    'P': 'J',    'Q': 'K',    'R': 'L',    'S': 'M',    'T': 'N',    'U': 'O',    'V': 'P',    'W': 'Q',    'X': 'R',    'Y': 'S',    'Z': 'T',    'a': 'u',    'b': 'v',    'c': 'w',    'd': 'x',    'e': 'y',    'f': 'z',    'g': 'a',    'h': 'b',    'i': 'c',    'j': 'd',    'k': 'e',    'l': 'f',    'm': 'g',    'n': 'h',    'o': 'i',    'p': 'j',    'q': 'k',    'r': 'l',    's': 'm',    't': 'n',    'u': 'o',    'v': 'p',    'w': 'q',    'x': 'r',    'y': 's',    'z': 't'}, True)])

def test_message_build_shift_dict(shift, test_dict,
 expected):
    """
    Tests message_object build shift dict method
    """
    if expected:
        assert message_mock.build_shift_dict(shift) == test_dict
    else:
        assert not message_mock.build_shift_dict(shift) == test_dict

@pytest.mark.parametrize("shift, test_str, expected",[
    (3, 'F\'j x qbpq', True),
    (5, 'D\'h v ozno', True),
    (9,' I\'m a test', False)
])

def test_message_apply_shift(shift,
 test_str,
 expected):
    """
    Tests message apply_shift method
    """
    if expected:
        assert message_mock.apply_shift(shift) == test_str
    else:
        assert message_mock.apply_shift(shift) != test_str

def test_plaintext_get_shift():

    assert plaintext_mock.get_shift() == 5

def tesT_plaintext_get_encryption_dict():
    test_dict =  {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E', 'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O', 'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U', 'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o', 'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u'}
    assert plaintext_mock.get_encryption_dict() == test_dict

def test_plaintext_get_message_text_encrypted():
    test_str = 'D\'h v ozno'
    assert plaintext_mock.get_message_text_encrypted() == 'D\'h v ozno'

def test_plaintext_change_shift():
    new_dict =  {'A': 'U',
        'B': 'V',
        'C': 'W',
        'D': 'X',
        'E': 'Y',
        'F': 'Z',
        'G': 'A',
        'H': 'B',
        'I': 'C',
        'J': 'D',
        'K': 'E',
        'L': 'F',
        'M': 'G',
        'N': 'H',
        'O': 'I',
        'P': 'J',
        'Q': 'K',
        'R': 'L',
        'S': 'M',
        'T': 'N',
        'U': 'O',
        'V': 'P',
        'W': 'Q',
        'X': 'R',
        'Y': 'S',
        'Z': 'T',
        'a': 'u',
        'b': 'v',
        'c': 'w',
        'd': 'x',
        'e': 'y',
        'f': 'z',
        'g': 'a',
        'h': 'b',
        'i': 'c',
        'j': 'd',
        'k': 'e',
        'l': 'f',
        'm': 'g',
        'n': 'h',
        'o': 'i',
        'p': 'j',
        'q': 'k',
        'r': 'l',
        's': 'm',
        't': 'n',
        'u': 'o',
        'v': 'p',
        'w': 'q',
        'x': 'r',
        'y': 's',
        'z': 't'}
    plaintext_mock.change_shift(6)
    assert plaintext_mock.get_shift() == 6
    assert plaintext_mock.get_encryption_dict() == new_dict
    assert plaintext_mock.get_message_text_encrypted() == 'C\'g u nymn'

@pytest.mark.parametrize('cipherTextObject, return_value, expected',[
    (CiphertextMessage('jgnnq'), (24, 'hello'), True), 
    (CiphertextMessage('V xpxphwzm rdoc hzydxdivg kmjkzmodzn'), (5, 'A cucumber with medicinal properties'), True),
    (CiphertextMessage('Kzgml, kzgml, dwl al sdd gml'), (8, 'Shout, shout, let it all out'), True),
    (CiphertextMessage('jgnnq'), (5, 'hello'), False), 
    (CiphertextMessage('V xpxphwzm rdoc hzydxdivg kmjkzmodzn'), (9, 'A cucumber with medicinal properties'), False),
    (CiphertextMessage('Kzgml, kzgml, dwl al sdd gml'), (5, 'Shout, shout, let it all out'), False)
])

def test_ciphertext_decrypt_message(cipherTextObject, return_value, expected):
    if expected:
        assert cipherTextObject.decrypt_message() == return_value
    else:
        assert cipherTextObject.decrypt_message() != return_value