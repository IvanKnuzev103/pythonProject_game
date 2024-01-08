import random




def drow_map():
    L = []
    for i in range(20):
        L.append((('.' + ' ') * 30).split())
    for elem in L:
        elem[random.randrange(0, 30)] = 'g'

    for elem in L:
        elem[random.randrange(0, 30)] = 'i'

    for elem in L:
        elem[random.randrange(0, 30)] = 'w'

    print()
    L[0] = (('#' + ' ' + 'U') + ('.' + ' ') * 28).split()
    L[19] = (('.' + ' ') * 28 + ('u' + ' ' + '@' + ' ')).split()

    file = open('map_game', 'w')
    for elem in L:
        file.write(''.join(elem) + '\n')


drow_map()



