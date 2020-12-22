def app():
    posCount = 0
    def fibonaci(pos, posCount):
        '''
            Assumes a position is given as integer such as pos >=1 which represents a position of a term
            in the fibonaci sequence defined as  a(1) = 1, a(2) =  1... a(n) = a(n)-2 + a(n)-1.
            Returns the term a(pos) in the type integer
        '''
        if pos == 2:
            posCount +=1
        print('current pos: ', pos)
        if pos == 0 or pos == 1:
            return 1
        else:
            # pos-=2
            # for i in range(pos):
            #     currentPos = pos1+pos2
            #     pos2 = pos1
            #     pos1 = currentPos
            return fibonaci(pos-1) + fibonaci(pos-2)
    print(fibonaci(int(input('Enter a positive integer\n>>>')), posCount))
    print(posCount)

again = True
while again:
    app()

    if input("continue?\n>>>") == "y":
        continue
    else:
        again = False
        print("should break here")
        break