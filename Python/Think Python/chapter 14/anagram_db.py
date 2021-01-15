import anagram_sets
import os
import shelve

def store_anagrams(d):
    """
    Assume d a dictionary
    storesd in a shelf
    """
    db = shelve.open('anagrams_db')
    for key in list(d.keys()):
        db[key] = d[key]
    db.close()

def read_anagrams(word):
    """
    Assumes word strings
    returns a list of its anagrams
    """
    try:
        db.open('anagrams_db')
        l = db[word]
        db.close()
        return l
    except as e:
        e
        print('Error reading word from database')
        db.close()