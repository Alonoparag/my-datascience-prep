## finger exercise
def findAnEven(L):
    """
    Assumes L is a list of integers
        Possible exceptions:
            1. L is not a list
            2. L is empty
            3. the elment e in L is not of the value int
    Returns the first even number in L
    Raises ValueError if L doesn't contain an even number
    """
    if not isinstance(L, list): raise ValueError("Expecting argument of type 'list'")
    if len(L) == 0: raise ValueError("argument is empty"
    )
    for e in L:
        print 
        if not isinstance(e, int): raise ValueError('argument should contain only values of type int')
        if e%2 == 0: return e
    raise ValueError('argument doesn\'t contain an even number')

L = []
while input("continue?\n>>>") == 'y':
    try:
        L.append(int(input('enter an integer\n>>>')))
    except ValueError:
        print('Please enter a valid integer')
print(findAnEven(L))