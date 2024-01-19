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
    L[0] = (("#[['hp',10],['opportunities','left'],['resurs_players',[('gold',100),('wood',100),('iron',100)]]]]" + ' ' + 'U[10,5] ') + ('.' + ' ') * 28).split()
    L[19] = (('.' + ' ') * 28 + 'u[10,5]' + " @[['hp',10],['opportinities','right'],['resirs_players',[('gold',100),('wood',100),('iron',100)]]]]").split()
    file = open('map_game', 'w')
    for elem in L:
        file.write(' '.join(elem) + '\n')


drow_map()


