def read_board(filename):
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    Board_arr = []
    board = []
    infile = open(filename, "r")
    while True:

read_board("board_examp.txt")
