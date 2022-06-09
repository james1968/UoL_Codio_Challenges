from chess_puzzle import *
from typing import *
import copy
import random

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    filename: str = input(bold_start + "File name for " + bold_end + "initial configuration: ")
    board_in_play: Board = copy.deepcopy(read_board(filename))

    print("The initial " + bold_start + "configuration is: " + bold_end)
    conf2unicode(read_board(filename))
    board_play: Board = Tuple[int, List[Piece]]
    board_arr: List[int, str] = []
    board: List[str] = []
    run: bool = True
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    while run == True:
        try:
            infile = open(filename, "r")
        except IOError:
            filename = input(
                "This " + bold_start + "is not " + bold_end + "a valid " + bold_start + "file. File name for " + bold_end + "initial configuration: ")
            run = False

