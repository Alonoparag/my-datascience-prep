import re
import string
import random
from bisect import bisect_left

def generate_lines(filename):
    in_file = open(filename, 'r')
    pattern = re.compile(r'[!"#$%&\'()*+,-.\/:;<=>?@\[\\\]^_`{|}~]')
    line_list = []
    for line in in_file:
        line = re.sub(pattern, '', line)
        line_list.append(line.strip().split(' '))
    return line_list

def generate_markov_dict(line_list):
    markov_dict = {}
    for line in line_list:
        
        if line[-1] not in markov_dict:
            markov_dict[line[-1]] = [False]
        else:
            markov_dict[line[-1]].append(False)
        for seq_ind in range(len(line)-1):
            if line[seq_ind] not in markov_dict:
                markov_dict[line[seq_ind]] = [line[seq_ind+1]]
            else:
                markov_dict[line[seq_ind]].append(line[seq_ind + 1])
    return markov_dict

def make_rand_sentence(filename):

    markov_dict = generate_markov_dict(generate_lines(filename))
    rand_string = ''
    rand_word = random.choice(list(markov_dict.keys()))

    while rand_word:
        rand_string += rand_word + ' '
        rand_word = random.choice(markov_dict[rand_word])
    rand_string = rand_string[:-1]
    return rand_string



def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        print(d)
        return d

# def rand_word_from_dict(d):
#     def cumsum_list(d):
#         l = []
#         for k in d.keys():
#             l.append(d[k]+l[-1])

def choose_rand(d):
    choice_set = []
    for k in d.keys():
        choice_set.append(k*d[k])
    print(choice_set)
    return random.choice(choice_set)
