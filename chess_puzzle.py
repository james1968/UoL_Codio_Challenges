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


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''


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
        # return abs(col_from - col_to)+abs(row_from - row_to) == 3

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

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
    board_piece_name = []
    for i in range(1, 3):
        if i == 1:
            count_B = 0
            count_R = 0
            for j in range(0, len(Board_arr[i])):
                Board_arr[i][j] = Board_arr[i][j].strip()
                xy_loc = location2index(Board_arr[i][j][1:])
                if Board_arr[i][j][0] == "B":
                    count_B += 1
                    name = "wb" + str(count_B)
                    board_piece_name.append(name)
                    pieces_arr.append(Bishop(xy_loc[0], xy_loc[1], True))
                if Board_arr[i][j][0] == "R":
                    count_R += 1
                    name = "wr" + str(count_R)
                    board_piece_name.append(name)
                    pieces_arr.append(Rook(xy_loc[0], xy_loc[1], True))
                if Board_arr[i][j][0] == "K":
                    name = "wk"
                    board_piece_name.append(name)
                    pieces_arr.append(King(xy_loc[0], xy_loc[1], True))
        if i == 2:
            count_B = 0
            count_R = 0
            for j in range(0, len(Board_arr[i])):
                Board_arr[i][j] = Board_arr[i][j].strip()
                xy_loc = location2index(Board_arr[i][j][1:])
                if Board_arr[i][j][0] == "B":
                    count_B += 1
                    name = "bb" + str(count_B)
                    name = Bishop(xy_loc[0], xy_loc[1], False)
                    pieces_arr.append(name)
                if Board_arr[i][j][0] == "R":
                    count_R += 1
                    name = "br" + str(count_R)
                    name = Rook(xy_loc[0], xy_loc[1], False)
                    pieces_arr.append(name)
                if Board_arr[i][j][0] == "K":
                    name = "bk"
                    name = King(xy_loc[0], xy_loc[1], False)
                    pieces_arr.append(name)
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
    print(board_matrix)
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

    for i in range(len(board_matrix)-1, -1, -1):
        for j in range(0, len(board_matrix[i])):
            print(board_matrix[i][j], end="")
        print()
def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''

    #filename = input("File name for initial configuration: ")
    read_board("board_examp.txt")

if __name__ == '__main__':  # keep this in
    main()

conf2unicode(read_board("board_examp.txt"))