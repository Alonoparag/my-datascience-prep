import pytest
from ps4a import get_permutations
from ps4c import *

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting juice'),'Converting juice', True),
    (SubMessage('Into the system!'),'Into the system!', True),
    (SubMessage('Converting juice'),'', False),
    (SubMessage('Into the system!'),'Intro the system!', False)
    ])

def test_get_message_text(input_value, return_value, expected):
    if expected:
        assert input_value.get_message_text() == return_value
    else:
        assert input_value.get_message_text() != return_value

@pytest.mark.parametrize('input_value, return_value, expected',[
    (SubMessage('Converting juice'),['Converting','juice'], True),
    (SubMessage('Into the system!'),['Into','the','system!'], True),
    (SubMessage('Converting juice'),'', False),
    (SubMessage('Into the system!'),'', False)
    ])


def test_get_valid_words(input_value, return_value, expected):
    if expected:
        assert input_value.get_valid_words() == return_value
    else:
        assert input_value.get_valid_words() != return_value

@pytest.mark.parametrize('input_value,permutation, return_value, expected',[
    (SubMessage('Converting juice'),'uaeio',{'A':'U', 'B':'B', 'C':'C', 'D':'D', 'E':'A', 'F':'F', 'G':'G', 'H':'H', 'I':'E', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'I', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'O', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z','a':'u', 'b':'b', 'c':'c', 'd':'d', 'e':'a', 'f':'f', 'g':'g', 'h':'h', 'i':'e', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'i', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'o', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}, True),
    (SubMessage('Into the system!'),'eioua',{'A':'E', 'B':'B', 'C':'C', 'D':'D', 'E':'I', 'F':'F', 'G':'G', 'H':'H', 'I':'O', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'U', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'A', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z','a':'e', 'b':'b', 'c':'c', 'd':'d', 'e':'i', 'f':'f', 'g':'g', 'h':'h', 'i':'o', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'u', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'a', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}, True),
    (SubMessage('Converting juice'),'ueiao','', False),
    (SubMessage('Into the system!'),'ueiao','', False)
    ])

def test_build_transpose_dict(input_value,permutation, return_value, expected):
    if expected:
        assert input_value.build_transpose_dict(permutation) == return_value
    else:
        assert input_value.build_transpose_dict(permutation) != return_value

@pytest.mark.parametrize('input_value, permutation, return_value, expected',[
    (SubMessage('Converting juice'),'eauio','Cinvartung jouca', True),
    (SubMessage('Into the system!'),'eaiuo','Intu tha systam!', True),
    (SubMessage('Converting juice'),'eauio','', False),
    (SubMessage('Into the system!'),'eaiuo','', False)
    ])

def test_apply_transpose(input_value, permutation, return_value, expected):
    if expected:
        assert input_value.apply_transpose(input_value.build_transpose_dict(permutation)) == return_value
    else:
        assert input_value.apply_transpose(input_value.build_transpose_dict(permutation)) != return_value


@pytest.mark.parametrize('input_value, expected',[
    (isinstance(EncryptedSubMessage('Cinvartung jouca'), EncryptedSubMessage), True),
    (isinstance(EncryptedSubMessage('Intu tha systam!'), EncryptedSubMessage), True),
    (isinstance(EncryptedSubMessage('Cinvartung jouca'), EncryptedSubMessage), True),
    (isinstance(EncryptedSubMessage('Intu tha systam!'), EncryptedSubMessage), True)
])

def test_EncryptedSubMessage_exists(input_value, expected):
    if expected:
        assert input_value
    else:
        assert not input_value

@pytest.mark.parametrize('input_value, return_value, expected',[
    (EncryptedSubMessage('Cinvartung jouca'),'Converting juice', True),
    (EncryptedSubMessage('Intu tha systam!'),'Into the system!', True),
    (EncryptedSubMessage('Cinvartung jouca'),'', False),
    (EncryptedSubMessage('Intu tha systam!'),'', False)
])

def test_decrypt_message(input_value, return_value, expected):
    if expected:
        assert input_value.decrypt_message() == return_value
    else:
        assert input_value.decrypt_message() != return_value