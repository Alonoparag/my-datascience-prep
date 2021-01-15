
def remove_zero_width(str_arg):
    return str_arg.strip(u"\u200B"+ u'\u200C'+ u'\uFEFF'+ u'\u2060'+ u'\u200D')
    
def mapper(map_func, tomap_list):
    mapped = []
    for element in tomap_list:
        mapped.append(map_func(element))
    return mapped

def generate_words(filename):
    inFile = open(filename, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_anagram(word1, word2):
    for char in word1:
        if char not in word2: return False
    for char in word2:
        if char not in word1: return False
    return True


def anagram_set(base_word, words_list):
    return_set = []
    for word in words_list:
        if is_anagram(base_word, word): return_set.append(word)
    return return_set


def generate_sets(words_list):
    def word_anagramed(word, list):
        for anagram in list:
            if is_anagram(word, anagram): return True
        return False
    return_set = []
    anagramed = []
    for word in word_list:
        if word in anagramed: continue
        an_set=anagram_set(word, words_list)
        return_set.append(an_set)
        anagramed.extend(an_set)
    return sorted(return_set, key=len,reverse = True)

def is_metatheasis(word1, word2):
    flag1 = False
    flag2 = False
    flag3 = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if not flag1:
                flag1 = True
            elif not flag2:
                flag2 = True
            elif not flag3:
                flag3 = True
        if flag1 and flag2 and flag3: return False  #more than one swap
    return True
        

# word_list = ['carded', 'cradle', 'credal', 'reclad','stoat','toast','aspire','generating', 'greatening', 'resmelts', 'smelters', 'termless']
word_list = mapper(remove_zero_width, generate_words('words.txt'))

# anagram_set('smelters', word_list)

ansets = generate_sets(word_list)

for anlist in ansets:
    print(anlist)


