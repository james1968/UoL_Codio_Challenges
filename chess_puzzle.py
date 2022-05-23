from typing import *
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
    print(str_coord)
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
    board_length = B[0]
    try:
        if pos_X > board_length or pos_Y > board_length:
            print("X and Y coordinates must be less than length of the board")
    except ValueError:
        raise V

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
    board_length = B[0]
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
        #get from 1, 5 to 4, 5.  Check piece at 2,5 and 3,5

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
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            for i in range(1, len(B)):
                for j in range(0, len(B[i])):
                    if self.pos_X == B[i][j].pos_X and self.pos_Y == B[i][j].pos_Y:
                        B[i][j].pos_X = pos_X
                        B[i][j].pos_Y = pos_Y
                    return True
        elif self.can_reach(pos_X,pos_Y,B) and is_piece_at(pos_X, pos_Y,B):
            cap_piece = piece_at(pos_X, pos_Y,B)
            print(type(cap_piece), cap_piece.pos_X, cap_piece.pos_Y, cap_piece.side)
            for i in range(1, len(B)):
                for j in range(0, len(B[i])):
                    if self.pos_X == B[i][j].pos_X and self.pos_Y == B[i][j].pos_Y:
                        B[i][j].pos_X = pos_X
                        B[i][j].pos_Y = pos_Y
                    return True
        else:
            return False

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

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

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
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            return True
        elif self.can_reach(pos_X,pos_Y,B) and is_piece_at(pos_X, pos_Y,B):
            cap_piece = piece_at(pos_X, pos_Y,B)
            print(cap_piece.side)
            return True
        else:
            print(False)
            return False


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


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints:
    - use is_check
    - use can_reach
    '''


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
    Board1 = tuple()
    Board_arr = []
    board = []
    run = True
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
    pieces_arr = []
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
    size = B[0]
    board_matrix = []

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
    board_string = ""


    for i in range(len(board_matrix)-1, -1, -1):
        for j in range(0, len(board_matrix[i])):
            board_string += board_matrix[i][j]
        if i > 0:
            board_string += "\n"
    print(board_string)
    return board_string

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

conf2unicode(read_board("board_examp2.txt"))

wr2 = Rook(2, 5, True)
wr2.can_move_to(1, 5, (read_board("board_examp2.txt")))

