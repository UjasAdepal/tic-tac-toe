print("Let's start the GAME ")
name1 = input('Enter your name player 1 : ')
name2 = input('Enter your name player 2 : ')
mark1 = input(name1 + ' enter your mark (X or O): ')
m2 = ''
if mark1 == 'X' or mark1 == 'x':
    m2 = 'O'
else:
    m2 = 'X'
mark2 = input(name2 + ' your mark is : ' + m2)
print('')
print('CHOOSE POSTION BETWEEN 1 T0 9.')
print('IF U CHOOSE WORNG POSTION YOUR TURN WILL BE SKIPPED')
print('')
print('')

ab = '1'
ac = '2'
ad = '3'
ai = '4'
aj = '5'
ak = '6'
ao = '7'
ap = '8'
aq = '9'

def tic_tac():
    a = ('     |     |     ')
    b = ('  {}  |  {}  |  {}  '.format(ab, ac, ad))
    c = ('_____|_____|_____')
    d = ('     |     |     ')
    e = ('  {}  |  {}  |  {}  '.format(ai, aj, ak))
    f = ('_____|_____|_____')
    g = ('     |     |     ')
    h = ('  {}  |  {}  |  {}  '.format(ao, ap, aq))
    i = ('     |     |     ')

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)

tic_tac()
k = 0
for j in range(5):
    print('')
    x = int(input(name1 + ' choose your position (from 1 to 9): '))
    print('')
    if x == 1:
        ab = 'X'
    elif x == 2:
        ac = 'X'
    elif x == 3:
        ad = 'X'
    elif x == 4:
        ai = 'X'
    elif x == 5:
        aj = 'X'
    elif x == 6:
        ak = 'X'
    elif x == 7:
        ao = 'X'
    elif x == 8:
        ap = 'X'
    elif x == 9:
        aq = 'X'
    k += 1
    if k == 9:
        print("  It's  tie   ")
        break

    tic_tac()

    if ab == ac == ad or ai == aj == ak or ao == ap == aq or ab == ai == ao or ac == aj == ap or ad == ak == aq or ad == aj == ao or ab == aj == aq:
        print('')
        print('congratulations! ' + name1 +' is winner')
        print('')
        break

    print('')
    O = int(input( name2+ ' choose your position (from 1 to 9): '))
    print('')
    if O == 1:
        ab = 'O'
    elif O == 2:
        ac = 'O'
    elif O == 3:
        ad = 'O'
    elif O == 4:
        ai = 'O'
    elif O == 5:
        aj = 'O'
    elif O == 6:
        ak = 'O'
    elif O == 7:
        ao = 'O'
    elif O == 8:
        ap = 'O'
    elif O == 9:
        aq = 'O'

    tic_tac()

    if ab == ac == ad or ai == aj == ak or ao == ap == aq or ab == ai == ao or ac == aj == ap or ad == ak == aq or ad == aj == ao or ab == aj == aq:
        print('')

        print('congratulations! ' +name1 +' is winner')
        print('')

        break

    k += 1

