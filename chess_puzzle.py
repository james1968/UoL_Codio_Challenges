from typing import *
import copy
def location2index(loc: str) -> Tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    # tuple called coords to hold co-ordinates in x,y format
    coords = ()
    # check the first coordinate is a letter from a - z
    if loc[0].isalpha() == False:
        return "The first coordinate must be a letter"
    # Populate tuple with x, y coordinates.  Check that second coordinte is an integer no longer than the length of the board.
    try:
        int(loc[1:])
        if int(loc[1:]) > 26:
            raise ValueError
            print("Invalid y value is larger than board size.")
        coords = ((int(ord(loc[0].lower())) - 96), int(loc[1:]))
    except Exception as e:
        raise ValueError
        print("Second item must be an integer: ", e)

    return coords


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    # Check for invalid string coordinates and return ValueError
    if type(x) != int or type(y) != int:
        raise ValueError
        print("x or y coordinate must be an integer")
    if x > 26 or y > 26:
        raise ValueError
        print("x or y coordinate must be less than maximum board length")

    str_coord = (chr(x + 96) + str(y))
    return str_coord


class Piece:
    pos_X: int
    pos_Y: int
    side: bool  # True for White and False for Black

    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side = side


Board = Tuple[int, List[Piece]]


def is_piece_at(pos_X: int, pos_Y: int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    board_length: int = B[0]
    try:
        if pos_X > board_length or pos_Y > board_length:
            print("X and Y coordinates must be less than length of the board")
    except ValueError:
        raise ValueError

    for i in range(1, len(B)):
        for j in range(0, len(B[i])):
            X = B[i][j].pos_X
            Y = B[i][j].pos_Y
            if X == pos_X and Y == pos_Y:
                return True
        return False


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    board_length: int = B[0]
    try:
        if pos_X > board_length or pos_Y > board_length:
            print("X and Y coordinates must be less than length of the board")
    except ValueError as V:
        raise V

    if is_piece_at(pos_X, pos_Y, B):
        for i in range(1, len(B)):
            for j in range(0, len(B[i])):
                if pos_X == B[i][j].pos_X and pos_Y == B[i][j].pos_Y:
                    return B[i][j]


class Rook(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)


    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at
        '''

        if self.pos_X != pos_X and self.pos_Y != pos_Y:
            return False

        if is_piece_at(pos_X, pos_Y, B) and piece_at(pos_X, pos_Y, B).side == self.side:
            return False

        if pos_X > self.pos_X:
            X = pos_X - self.pos_X
            for i in range(X, self.pos_X, -1):
                if is_piece_at(i, pos_Y, B):
                    return False
            return True
        if pos_Y > self.pos_Y:
            Y = pos_Y - self.pos_Y
            for j in range(Y, self.pos_Y, -1):
                if is_piece_at(pos_X, j, B):
                    return False
            return True
        if self.pos_X > pos_X:
            for i in range(pos_X+1, self.pos_X):
                if is_piece_at(i, pos_Y, B):
                    return False
            return True
        if self.pos_Y > pos_Y:
            for j in range(pos_Y+1, self.pos_Y):
                if is_piece_at(pos_X, j, B):
                    return False
            return True


    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules

        Hints:
        - firstly, check [Rule2] and [Rule4] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule5], use is_check on new board
        '''

        size: int = B[0]
        if self.can_reach(pos_X, pos_Y, B) == False:
            return False
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            r_moved_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            r_check_side: bool = not self.side
            r_new_list_pieces: list[Piece] = B[1]
            for i in r_new_list_pieces:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    r_new_list_pieces.remove(i)
            r_new_list_pieces.append(r_moved_piece)
            r_temp_board: Board = (size, r_new_list_pieces)
            if is_check(r_check_side, r_temp_board):
                return False
            else:
                return True

        if self.can_reach(pos_X,pos_Y,B) and is_piece_at(pos_X, pos_Y,B):
            r_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            r_side_check: bool = r_cap_piece.side
            r_moved_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            r_new_list_pieces: list[Piece] = B[1]
            r_new_list_pieces.remove(r_cap_piece)
            for i in r_new_list_pieces:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    r_new_list_pieces.remove(i)
            r_new_list_pieces.append(r_moved_piece)
            r_temp_board: Board = (B[0], r_new_list_pieces)
            if is_check(r_side_check, r_temp_board):
                return False
            else:
                return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''
        if ((self.pos_X - pos_X) - (self.pos_Y - pos_Y)) == 0:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                if pos_X > self.pos_X and pos_Y > self.pos_Y:
                    for i in range(1, pos_X):
                        if is_piece_at(self.pos_X+i, self.pos_Y+i, B) and piece_at(self.pos_X+i, self.pos_Y+i, B).side == self.side:
                            print("False")
                            return False
                    return True
                if pos_X < self.pos_X and pos_Y < self.pos_Y:
                    for i in range(1, self.pos_X):
                        if is_piece_at(self.pos_X-i, self.pos_Y-i, B) and piece_at(self.pos_X-i, self.pos_Y-i, B) == self.side:
                            return False
                    return True

        if ((self.pos_X - pos_X) + (self.pos_Y - pos_Y)) == 0:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                if pos_X < self.pos_X and pos_Y > self.pos_Y:
                    for i in range(1, pos_Y):
                        if is_piece_at(self.pos_X-i, self.pos_Y+i, B) and piece_at(self.pos_X-i, self.pos_Y+i, B) == self.side:
                            return False
                    return True
                if pos_X > self.pos_X and pos_Y < self.pos_Y:
                    for i in range(1, self.pos_Y):
                        if is_piece_at(self.pos_X+i, self.pos_Y-i, B) and piece_at(self.pos_X+i, self.pos_Y-i, B) == self.side:
                            return False
                    return True
        return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        if self.can_reach(pos_X, pos_Y, B) == False:
            return False

        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            b_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            b_check_side: bool = not self.side
            b_new_list: list[Piece] = copy.deepcopy(B[1])
            for i in b_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    b_new_list.remove(i)
            b_new_list.append(b_move_piece)
            b_temp_board: Board = (B[0], b_new_list)
            if is_check(b_check_side, b_temp_board):
                print("False1")
                return False
            else:
                return True


        if self.can_reach(pos_X, pos_Y, B) and is_piece_at(pos_X, pos_Y, B):
            b_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            b_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            b_check_side: bool = not self.side
            b_new_list: List[Piece] = copy.deepcopy(B[1])
            for i in b_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    b_new_list.remove(i)
                if i.pos_X == b_cap_piece.pos_X and i.pos_Y == b_cap_piece.pos_Y and type(i) == type(b_cap_piece) and i.side == b_cap_piece.side:
                    b_new_list.remove(i)
            b_new_list.append(b_move_piece)
            b_temp_board: Board = (B[0], b_new_list)
            if is_check(b_check_side, b_temp_board):
                print("False2")
                return False
            else:
                return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''
        if abs(self.pos_X - pos_X) + abs(self.pos_Y - pos_Y) <= 1:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                return True
            else:
                return False

        if abs(self.pos_X - pos_X) == 1 and abs(self.pos_Y - pos_Y) == 1:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                return True
            else:
                return False
        return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        # needs to be updated to capture the piece and check if the move results in check
        if self.can_reach(pos_X, pos_Y, B) == False:
            return False

        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            k_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            k_check_side: bool = not self.side
            k_new_list: List[Piece] = copy.deepcopy(B[1])
            for i in k_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    k_new_list.remove(i)
            k_new_list.append(k_move_piece)
            k_temp_board: Board = (B[0], k_new_list)
            if is_check(k_check_side, k_temp_board):
                return False
            else:
                return True


        if self.can_reach(pos_X, pos_Y, B) and is_piece_at(pos_X, pos_Y, B):
            k_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            k_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
            k_check_side: bool = not self.side
            k_new_list: List[Piece] = copy.deepcopy(B[1])
            for i in k_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    k_new_list.remove(i)
                if i.pos_X == k_cap_piece.pos_X and i.pos_Y == k_cap_piece.pos_Y and type(i) == type(k_cap_piece) and i.side == k_cap_piece.side:
                    k_new_list.remove(i)
            k_new_list.append(k_move_piece)
            k_temp_board: Board = (B[0], k_new_list)
            if is_check(k_check_side, k_temp_board):
                return False
            else:
                return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    # this method checks if the side used in the argument has check over the other side
    # i.e if False is used in the argument and Black has white in check then true is returned.
    king_x: int = 0
    king_y: int = 0
    for i in range(0, len(B[1])):
        if type(B[1][i]) == King and B[1][i].side != side:
            king_x = B[1][i].pos_X
            king_y = B[1][i].pos_Y

    for j in range(0, len(B[1])):
        if B[1][j].side == side:
            if B[1][j].can_reach(king_x, king_y, B):
                return True
    return False

def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints:
    - use is_check
    - use can_reach - NOTE: THIS HINT IS WRONG IT SHOULD BE USE "can_move_to" as that checks if move results in check.
    '''
    # this method is written such that True is returned if the the side entered in as the argument has the opposition in check mate
    # i.e. if False is used in the argument and Black has checkmate then True is returned.
    king_X: int = 0
    king_Y: int = 0

    check_side = not side

    if is_check(check_side, B):
        print("Side that has check: ", check_side)
        for i in B[1]:
            if type(i) == King and i.side == side:
                king: Piece = type(i)(i.pos_X, i.pos_Y, side)
                print(king.pos_X, king.pos_Y)
        for j in range(1, B[0]+1):
            for k in range(1, B[0]+1):
                if king.can_move_to(j, k, B):
                    print("False")
                    return False
        print("True")
        return True
    else:
        print("False")
        return False

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints:
    - use is_check
    - use can_move_to
    '''

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    Board1: Board = tuple()
    Board_arr: List[int, str] = []
    board: List[str] = []
    run: bool = True
    while run == True:
        try:
            infile = open(filename, "r")
            lines = infile.readlines()
            if len(lines) != 3:
                infile.close()
                filename = input("This is not a valid file. File name for initial configuration: ")
        except IOError:
            filename = input("This is not a valid file. File name for initial configuration: ")
        else:
            infile = open(filename, "r")
            line = infile.readline()
            while line != "":
                board.append(line.rstrip())
                line = infile.readline()
            Board_arr = [int(board[0]), board[1].split(","), board[2].split(",")]
            run = False
    Board1 += (Board_arr[0], )
    pieces_arr: List[Piece] = []
    for i in range(1, 3):
        if i == 1:
            for j in range(0, len(Board_arr[i])):
                Board_arr[i][j] = Board_arr[i][j].strip()
                xy_loc = location2index(Board_arr[i][j][1:])
                if Board_arr[i][j][0] == "B":
                    pieces_arr.append(Bishop(xy_loc[0], xy_loc[1], True))
                if Board_arr[i][j][0] == "R":
                    pieces_arr.append(Rook(xy_loc[0], xy_loc[1], True))
                if Board_arr[i][j][0] == "K":
                    pieces_arr.append(King(xy_loc[0], xy_loc[1], True))
        if i == 2:
            for j in range(0, len(Board_arr[i])):
                Board_arr[i][j] = Board_arr[i][j].strip()
                xy_loc = location2index(Board_arr[i][j][1:])
                if Board_arr[i][j][0] == "B":
                    pieces_arr.append(Bishop(xy_loc[0], xy_loc[1], False))
                if Board_arr[i][j][0] == "R":
                    pieces_arr.append(Rook(xy_loc[0], xy_loc[1], False))
                if Board_arr[i][j][0] == "K":
                    pieces_arr.append(King(xy_loc[0], xy_loc[1], False))
            Board1 += (pieces_arr,)

    return Board1


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    file = open(filename,"w")
    file.write(str(B[0]) + "\n")
    file_line_1 = ""
    for i in range(1, len(B)):
        for j in range(0, len(B[1])):
            if B[i][j].side == True:
                if type(B[i][j]) == Rook:
                    file_line_1 += "R" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == King:
                    file_line_1 += "K" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == Bishop:
                    file_line_1 += "B" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
        file.write(file_line_1[:-2])
        file.write("\n")
    file_line_2 = ""
    for i in range(1, len(B)):
        for j in range(0, len(B[1])):
            if B[i][j].side == False:
                if type(B[i][j]) == Rook:
                    file_line_2 += "R" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == King:
                    file_line_2 += "K" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == Bishop:
                    file_line_2 += "B" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
        file.write(file_line_2[:-2])
    file.close()

def find_black_move(B: Board) -> Tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules
    assumes there is at least one black piece that can move somewhere

    Hints:
    - use methods of random library
    - use can_move_to
    '''


def conf2unicode(B: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    size: int = B[0]
    board_matrix: List[List] = []

    for i in range(0, size):
        board_matrix.append([])
        for j in range(0, size):
            board_matrix[i].append("\u2001")
    for i in range(1, len(B)):
        for j in range(0, len(B[i])):
            X = B[i][j].pos_X-1
            Y = B[i][j].pos_Y-1
            if type(B[i][j]) == Bishop and B[i][j].side == True:
                board_matrix[Y][X] = "\u2657"
            if type(B[i][j]) == Rook and B[i][j].side == True:
                board_matrix[Y][X] = "\u2656"
            if type(B[i][j]) == King and B[i][j].side == True:
                board_matrix[Y][X] = "\u2654"
            if type(B[i][j]) == Bishop and B[i][j].side == False:
                board_matrix[Y][X] = "\u265D"
            if type(B[i][j]) == Rook and B[i][j].side == False:
                board_matrix[Y][X] = "\u265C"
            if type(B[i][j]) == King and B[i][j].side == False:
                board_matrix[Y][X] = "\u265A"
    board_string: str = ""


    for i in range(len(board_matrix)-1, -1, -1):
        for j in range(0, len(board_matrix[i])):
            board_string += board_matrix[i][j]
        if i > 0:
            board_string += "\n"
    print(board_string)
    return board_string

def print_board(B: Board) -> str:
    for i in range(0, len(B[1])):
        print(f"{type(B[1][i])}, {B[1][i].pos_X}, {B[1][i].pos_Y}, {B[1][i].side}.")

def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''

    #filename = input("File name for initial configuration: ")
    read_board("board_examp2.txt")

if __name__ == '__main__':  # keep this in
    main()


wr2b = Rook(2, 4, True)
wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)
br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)
br2b = Rook(4, 5, False)
bb1 = Bishop(2, 4, False)
wr3 = Rook(3, 3, True)
wr3b = Rook(5, 1, True)
B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr3b, wk])
B4 = (5, [wb1, wr1, wr3, bk, br1, br2a, bb1, wr2a, wk])
print("Board 2")
conf2unicode(B3)
print("------")
#print("Board 1")
#conf2unicode(B1)
#print("------")
#print("Board 3")
#conf2unicode(B3)
#print("------")
#print("Board 4")
#conf2unicode(B4)

is_checkmate(True, B3)
#true
is_checkmate(False, B3)
#false





