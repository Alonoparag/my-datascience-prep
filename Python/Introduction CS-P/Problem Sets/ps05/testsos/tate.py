import pytest
import datetime
from ps05 import *

@pytest.mark.parametrize('NewsStory_object, output_attributes', [
    (NewsStory('abcd','testTitle','testDescription','https://example.com',datetime.now()), ('abcd','testTitle','testDescription','https://example.com',datetime))
    ])

def test_problem1(NewsStory_object, output_attributes):
    assert NewsStory_object.get_guid() == output_attributes[0]
    assert NewsStory_object.get_title() == output_attributes[1]
    assert NewsStory_object.get_description() == output_attributes[2]
    assert NewsStory_object.get_link() == output_attributes[3]
    assert NewsStory_object.get_pubdate() == output_attributes[4]