import re
import string
import bisect


def is_header_reached(line):
    if re.sub(u"\u200B" + u'\u200C' + u'\uFEFF' + u'\u2060' + u'\u200D', '', line.strip()) == 'Translated by William Whiston':
        return True

def is_foot_reached(line):
    if re.sub(u"\u200B" + u'\u200C' + u'\uFEFF' + u'\u2060' + u'\u200D', '', line.strip()) == 'Footnotes':
        return True

def generate_words(filename, is_word_list = False):
    pattern = re.compile('[^a-zA-Z]')
    
    inFile = open(filename, 'r')
    wordlist = []
    past_header = False
    before_foot = False
    if is_word_list:
        past_header = True
    for line in inFile:
        if is_header_reached(line): past_header = True
        if is_foot_reached(line): before_foot = True
        if past_header and not before_foot:
            for word in line.split(' '):
                word = re.sub(pattern, '', word.lower())
                if len(word) > 0:
                    wordlist.append(word)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

book_word_list = generate_words("on-josephus.txt")
sorted_words = sorted(book_word_list[:len(book_word_list)])

def word_counter(word_list):
    counted_words = []
    word_counter = 1
    current_word = ''
    for word in word_list:
        if word != current_word:
            if len(current_word)>0:counted_words.append((word_counter, current_word))
            current_word = word
            word_counter = 1
        else:
            word_counter += 1
    return counted_words

counted_words = sorted(word_counter(sorted_words), reverse = True)

def not_in_word_list(book_words_counted, word_list):
    missing_words = []
    for number, word in book_words_counted:
        if word not in word_list:
            missing_words.append(word)
    return missing_words

word_list_check = generate_words('words.txt',is_word_list = True)

print(not_in_word_list(counted_words, word_list_check))


import random
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        print(d)
        return d

def choose_rand(d):
    choice_set = []
    for k in d.keys():
        choice_set.append(k*d[k])
    print(choice_set)
    return random.choice(choice_set)


bisect.bisect(list(string.ascii_lowercase), 'b')

print(choose_rand(histogram('lkhwekabasdfwxc')))