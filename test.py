# import numpy as np
#
# arr = np.array([{}])
# arr = np.append(arr, [{'name': 'ami', 'age': 25}])
# arr = np.append(arr, [{'name': 'ami', 'age': 25}])
# print(arr)

# from numpy import random
# import numpy as np
#
# _card_set = np.array([
#     (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12),
#     (1, 13), (1, 14),
#     (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12),
#     (2, 13), (2, 14),
#     (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
#     (3, 13), (3, 14),
#     (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12),
#     (4, 13), (4, 14)])
# random.shuffle(_card_set)
# print(_card_set)

# --------------------------------choose partner test
# from game import *
# from player import *
#
# game = TarneebGame(5, 10, '123')
# p1 = Player('ibrahim', 0, 's1')
# game.add_player(p1)
# p2 = Player('mohammad', 1, 's1')
# game.add_player(p2)
# p3 = Player('alaa', 2, 's1')
# game.add_player(p3)
# p4 = Player('ali', 3, 's1')
# game.add_player(p4)
# [print(player) for player in game.players]
# game.choose_partner(2)
# print("----------------------------")
# [print(player) for player in game.players]

k = 'abcd'
d = {
   'abc': '123'
}
if d.get(k) is not None:
    print('exist')
else:
    d[k] = '123'
print(d)