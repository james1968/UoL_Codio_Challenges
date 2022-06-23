import pytest
from chess_puzzle import *

def test_locatio2index1():
    assert location2index("e2") == (5, 2)

    assert location2index("S8") == (19, 8)

    assert location2index("Z26") == (26, 26)

    assert location2index("z27") == "Invalid y value is larger than board size."

    assert location2index("52") == "The first coordinate must be a letter"

    assert location2index("a123") == "Invalid y value is larger than board size."

    assert location2index("aa") == "Second item must be an integer."


def test_index2location1():
    assert index2location(5, 2) == "e2"

    assert index2location(10, 14) == "j14"

    assert index2location(23, 2) == "w2"

    assert index2location(26, 26) == "z26"

    with pytest.raises(ValueError):
        index2location("e", 5)

    with pytest.raises(ValueError):
        index2location(3, "d")


# pieces to be used in test cases
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
br2d = Rook(1, 1, False)
wr64 = Rook(6, 4, True)
wb32 = Bishop(3, 2, True)
wr41 = Rook(4, 1, True)
wk31 = King(3, 1, True)
wb63 = Bishop(6, 3, True)
bk58 = King(5, 8, False)
br48 = Rook(4, 8, False)
br86 = Rook(8, 6, False)
br57 = Rook(5, 7, False)
bb34 = Bishop(3, 4, False)
bb77 = Bishop(7, 7, False)
wr68 = Rook(6, 8, True)


# boards to be used in test cases
B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk, bb1])
B4 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
B5 = (5, [wb1, wr1, wb4, bk, br1, br2, br3, wr2, wk])
B6 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
B7 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr3b, wk])
B8 = (5, [wb1, wr1, wb2, bk, br1, br2c, br3, wr2, wk])
B9 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
B10 = (1, [wb1])
B11 = (1, [br2d])
B12 = (8, [wb1, wr64, wb32, wr41, wk31, wb63, bk58, br48, br86, br57, bb34, bb77])
B12_check = (8, [wb1, wr64, wb32, wr41, wk31, wb63, bk58, br48, br86, br57, bb34, bb77, wr68])


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
    assert is_piece_at(7, 7, B12) == True
    assert is_piece_at(5, 5, B12) == False
    assert is_piece_at(12, 12, B12) == False


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1
    assert piece_at(2, 4, B1) == br2
    assert piece_at(3, 5, B1) == wk
    assert piece_at(1, 5, B1) == wr2
    assert piece_at(5, 4, B1) == br3
    assert piece_at(8, 8, B1) == False
    assert piece_at(5, 5, B1) == False
    assert piece_at(6, 3, B12) == wb63
    assert piece_at(5, 8, B12) == bk58
    assert piece_at(8, 8, B12) == False
    assert piece_at(12, 12, B12) == False


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
    assert wb1.can_reach(3, 3, B5) == False
    assert wr64.can_reach(6, 7, B12) == True
    assert wb63.can_reach(7, 4, B12) == True
    assert wr64.can_reach(6, 8, B12_check) == False
    assert wb63.can_reach(6, 2, B12) == False


def test_can_move_to1():
    assert wr2a.can_move_to(2, 4, B2) == False
    assert wr2a.can_move_to(1, 5, B2) == True
    assert wr2a.can_move_to(3, 5, B2) == False
    assert wr1.can_move_to(5, 2, B2) == False
    assert wr1.can_move_to(4, 2, B2) == True
    assert bk.can_move_to(1, 2, B1) == False
    assert bk.can_move_to(2, 4, B1) == False
    assert bk.can_move_to(3, 4, B1) == False
    assert wk.can_move_to(2, 5, B2) == False
    assert br2.can_move_to(1, 4, B2) == False
    assert br2.can_move_to(1, 4, B1) == True
    assert wb1.can_move_to(2, 1, B1) == False
    assert wb1.can_move_to(2, 2, B1) == True
    assert wb2.can_move_to(4, 3, B1) == True
    assert wb2.can_move_to(3, 4, B1) == True
    assert bb1.can_move_to(4, 4, B3) == False
    assert bb1.can_move_to(3, 3, B3) == False
    assert bb1.can_move_to(2, 2, B3) == False
    assert bb1.can_move_to(4, 5, B3) == False
    assert wr64.can_move_to(6, 7, B12) == True
    assert wb63.can_move_to(7, 4, B12) == True
    assert wr64.can_move_to(6, 8, B12_check) == False
    assert wb63.can_move_to(6, 2, B12) == False


def test_is_check1():
    assert is_check(True, B2) == False
    assert is_check(False, B2) == True
    assert is_check(True, B4) == True
    assert is_check(False, B4) == True
    assert is_check(True, B6) == True
    assert is_check(False, B6) == False
    assert is_check(False, B7) == False
    assert is_check(True, B7) == False
    assert is_check(True, B12) == False
    assert is_check(False, B12_check) == True
    assert is_check(True, B12_check) == False


def test_is_checkmate1():

    assert is_checkmate(True, B2) == False
    assert is_checkmate(False, B2) == False
    assert is_checkmate(True, B1) == False
    assert is_checkmate(True, B1) == False
    assert is_checkmate(False, B9) == False
    assert is_checkmate(True, B9) == True
    assert is_checkmate(False, B12_check) == True
    assert is_checkmate(True, B12_check) == False


def test_read_board1():
    with pytest.raises(IOError):
        read_board("d")

    B = read_board("board_examp1.txt")
    assert B[0] == 5

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

def test_is_stalemate():
    assert is_stalemate(True, B10) == True
    assert is_stalemate(False, B10) == True
    assert is_stalemate(True, B1) == False
    assert is_stalemate(False, B1) == False
    assert is_stalemate(True, B8) == True