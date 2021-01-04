import random
import string

def bubble_sort(L):
    swap = False
    counter = 0
    while not swap:
        print(counter, L)
        counter+=1
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


l = list(string.ascii_letters)
random.shuffle(l)
bubble_sort(l)

