while input('continue\n>>>') == 'y':
    cube = int(input('enter cube\n>>>'))
    epsilon = float(input('enter float difference:\n>>>'))
    guess = 0.0
    increment = float(input('enter increment:\n>>>'))
    num_guesses = 0
    while abs(guess**3 - cube) >= epsilon and guess <= cube :
        guess += increment
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print('Failed on cube root of', cube)
    else:
        print(guess, 'is close to the cube root of', cube)