from chess_puzzle import *

#b = read_board("b.txt")
#conf2unicode(b)
#print(piece_at(6, 4, b).can_reach(3, 4, b))
#print(piece_at(6, 4, b).can_move_to(3, 4, b))

wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)
wb4 = Bishop(2, 2, True)
br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)
bb1 = Bishop(5, 5, False)
wr2b = Rook(2, 4, True)
wr3b = Rook(5, 1, True)
br2b = Bishop(1, 4, False)
br2c = Rook(4, 5, False)


B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk, bb1])
B4 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
B5 = (5, [wb1, wr1, wb4, bk, br1, br2, br3, wr2, wk])
B6 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
B7 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr3b, wk])
B8 = (5, [wb1, wr1, wb2, bk, br1, br2c, br3, wr2, wk])
B9 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
B10 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])


print(location2index("212b25"))
