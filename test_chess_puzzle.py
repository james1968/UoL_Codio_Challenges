import pytest
from typing import *
from chess_puzzle import *


def test_locatio2index1():
    assert location2index("e2") == (5, 2)

    assert location2index("S8") == (19, 8)

    assert location2index("52") == "The first coordinate must be a letter"

    with pytest.raises(ValueError):
        location2index("aa")

    with pytest.raises(ValueError):
        location2index("a123")


def test_index2location1():
    assert index2location(5, 2) == "e2"

    assert index2location(10, 14) == "j14"

    assert index2location(23, 2) == "w2"

    with pytest.raises(ValueError):
        index2location("e", 5)

    with pytest.raises(ValueError):
        index2location(3, "d")


wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)

B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])

'''
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
'''


def test_is_piece_at1():
    assert is_piece_at(2, 2, B1) == False
    assert is_piece_at(1, 2, B1) == True
    assert is_piece_at(5, 4, B1) == True
    assert is_piece_at(2, 5, B1) == False
    assert is_piece_at(3, 5, B1) == True
    assert is_piece_at(4, 5, B1) == False


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1
    assert piece_at(2, 4, B1) == br2
    assert piece_at(3, 5, B1) == wk
    assert piece_at(1, 5, B1) == wr2
    assert piece_at(5, 4, B1) == br3



def test_can_reach1():
    assert wr2.can_reach(3, 2, B1) == False
    assert wr2.can_reach(3, 5, B1) == False
    assert wr2.can_reach(1, 1, B1) == False
    assert wr2.can_reach(1, 2, B1) == False
    assert wr2.can_reach(1, 3, B1) == True
    assert wr2.can_reach(4, 5, B1) == False
    assert br3.can_reach(1, 4, B1) == False
    assert wk.can_reach(3, 4, B1) == True
    assert bk.can_reach(2, 4, B1) == False
    assert wk.can_reach(3, 3, B1) == False
    assert bk.can_reach(2, 4, B1) == False
    assert bk.can_reach(1, 2, B1) == True
    assert bk.can_reach(5, 5, B1) == False
    assert wb2.can_reach(5, 5, B1) == False
    assert wb2.can_reach(4, 3, B1) == True
    assert wb2.can_reach(3, 4, B1) == True
    assert wb2.can_reach(3, 3, B1) == False
    assert wb1.can_reach(2, 2, B1) == True
    assert wb1.can_reach(3, 3, B1) == True
    assert wb1.can_reach(1, 5, B1) == False

    wb4 = Bishop(2, 2, True)
    B5 = (5, [wb1, wr1, wb4, bk, br1, br2, br3, wr2, wk])
    assert wb1.can_reach(3, 3, B5) == False



br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)


def test_can_move_to1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2, 4, B2) == False
    assert wr2a.can_move_to(1, 5, B2) == True
    assert wr2a.can_move_to(3, 5, B2) == False
    assert wr1.can_move_to(5, 2, B2) == False
    assert wr1.can_move_to(4, 2, B2) == True
    assert bk.can_move_to(1, 2, B1) == False
    assert bk.can_move_to(2, 4, B1) == False
    assert bk.can_move_to(3, 4, B1) == False
    B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wk.can_move_to(2, 5, B3) == False
    assert br2.can_move_to(1, 4, B2) == False
    bb1 = Bishop(2, 4, False)
    B4 = (5, [wb1, wr1, wb2, bk, br1, br2a, bb1, wr2a, wk])
    assert bb1.can_move_to(1, 3, B4) == False
    wr3 = Rook(3, 3, True)
    B4 = (5, [wb1, wr1, wr3, bk, br1, br2a, bb1, wr2a, wk])
    assert bb1.can_move_to(3, 3, B4) == False
    assert wb1.can_move_to(2, 2, B1) == True
    assert wb1.can_move_to(2, 1, B1) == False


def test_is_check1():
    wr2b = Rook(2, 4, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True
    assert is_check(False, B2) == True
    wr3b = Rook(5, 1, True)
    B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
    assert is_check(True, B3) == False
    assert is_check(False, B3) == True
    br2b = Bishop(1, 4, False)
    B4 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr3b, wk])
    assert is_check(False, B4) == False
    assert is_check(True, B4) == False



def test_is_checkmate1():
    br2b = Rook(4, 5, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True
    assert is_checkmate(False, B2) == False



def test_read_board1():
    with pytest.raises(IOError):
        read_board("d")

    with pytest.raises(IOError):
        read_board("board_examp1.txt")

    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  # we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side == piece1.side and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]:  # we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side == piece1.side and type(
                    piece) == type(piece1):
                found = True
        assert found


def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "

