import re
import string

def is_header_reached(line):
    if re.sub(u"\u200B" + u'\u200C' + u'\uFEFF' + u'\u2060' + u'\u200D', '', line.strip()) == 'Translated by William Whiston':
        return True

def is_foot_reached(line):
    if re.sub(u"\u200B" + u'\u200C' + u'\uFEFF' + u'\u2060' + u'\u200D', '', line.strip()) == 'Footnotes':
        return True

def generate_words(filename):
    pattern = re.compile('[^a-zA-Z]')
    
    inFile = open(filename, 'r')
    wordlist = []
    past_header = False
    before_foot = False
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
word_list = generate_words("on-josephus.txt")
sorted_words = sorted(word_list[:len(word_list)])

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

# def word_counter(word_list, counted_words=[]):
# # Take a sorted list of words
#     if len(word_list) == 0:
#         return counted_words
# # iterate through the list counting the index
#     for i in range(len(word_list)):
# # when the iterated word is different from the first word or when index = len - 1
#         if i == len(word_list) - 1 or word_list[i] != word_list[0]:
# # count the section of the list until the current index and add it to a list of words as tuple(count, word)
#             if word_list[i] != word_list[0]:
#                 counted_words.append((len(word_list[:i]), word_list[0]))
#                 return word_counter(word_list[i:], counted_words)
#             elif i == len(word_list) - 1:
#                 print('should enter end condition')
#                 counted_words.append((len(word_list), word_list[0]))
#                 return counted_words
# recall the function with the section of the list not iterated through yet
counted_words = sorted(word_counter(sorted_words), reverse = True)

print(counted_words)