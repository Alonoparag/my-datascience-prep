# import unittest
from lib import hello
import pytest

def test_hello():
    assert hello('Alon') == 'Hello Allon'

# class Test(unittest.TestCase):
#     def test_hello(self):
#         self.assertEqual(hello('Alon'), 'Hello Allon')