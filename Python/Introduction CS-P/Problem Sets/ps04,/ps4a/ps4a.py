# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Started working 22.12.2020 19:30
# After working on the code for a week, and managing to succeed on a sequence of l = 3, but failing to succeed on a sequence of l = 4. I decided to check a pseudocode in order to optimize the code. pseudocode was chekced from https://en.wikipedia.org/wiki/Heap%27s_algorithm code is pasted in ps4a/drafts.ipynb. along with difference
# at 28.12.2020 I decided to look for a python implementation of heaps algorithm
# After reverse engieneering the python implementation, I reversed engineered the implementation from https://www.pythonpool.com/python-permutations/ to work backwards (i decrementing to 1), to make sure that I understand the concept of this function
# Finished working on 29.12.2020 16:46

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    answer=[]
    def perm(sequence, length,i):
        """
        Assumes
            sequence: list of singleton strings.
            length:integer length of list
            i: integer length of list
        Returns None
        """
        if i == 1:
            if not ''.join(sequence) in answer:
                answer.append(''.join(sequence))
        else:
            for j in range(i-1, -1, -1):
                sequence[j],sequence[i-1] = sequence[i-1],sequence[j]
                perm(sequence,length,i-1)
                sequence[j],sequence[i-1] = sequence[i-1],sequence[j]
    perm(list(sequence), len(sequence), len(sequence))

    return answer

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
    print('Input: abc')
    print('Expected Output: abc acb bac bca cab cba ')
    print('Actual Output:', get_permutations('abc'))

    print('Input: abcd')
    print('Expected Output: abcd abdc acbd acdb adbc adcb bacd badc bcad bcda bdac bdca cabd cadb cbad cbda cdab cdba dabc dacb dbac dbca dcab dcb')
    print('Actual Output:', get_permutations('abcd'))

    print('Input: bcd')
    print('Expected Output: bcd bdc cbd cdb dbc dcb ')
    print('Actual Output:', get_permutations('bcd'))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

