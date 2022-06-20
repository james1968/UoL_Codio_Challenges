from typing import *
import copy
import random
import pytest
from typing import *
from chess_puzzle import *

def run() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    '''
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    blue_text = '\033[96m'
    blue_text_end = '\033[0:0m'
    filename: str = input(bold_start + "File name for " + bold_end + "initial configuration: ")
    run: bool = True
    # First while loop checks the file is present in the directory and if so creates board to play on.
    while run == True:
        try:
            open(filename, "r")
        except IOError:
            filename = input(
                "This " + bold_start + "is not " + bold_end + "a valid " + bold_start + "file. File name for " + bold_end + "initial configuration: ")
        else:
            board_in_play: Board = copy.deepcopy(read_board(filename))
            print("The initial " + bold_start + "configuration is: " + bold_end)
            conf2unicode(board_in_play)
            run = False
    # main game loop, starts with white move or saving file if quit is entered.

    white_move = input("Next " + blue_text + "move " + blue_text_end + "of White: ")

    if white_move.strip().lower() == "quit":
        filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
        save_board(filename_store, board_in_play)
        print("The game configuration saved.")
        return False
    while True:
        str_len_half = int(len(white_move) / 2)
        white_x_loc = white_move[:str_len_half]
        white_y_loc = white_move[str_len_half:]
        white_piece_move_from: Tuple[int, int] = location2index(white_x_loc)
        white_piece_move_to: Tuple[int, int] = location2index(white_y_loc)
        white_to_X: int = white_piece_move_to[0]
        white_to_Y: int = white_piece_move_to[1]
        white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)

        if white_piece.can_move_to(white_to_X, white_to_Y, board_in_play):
            board_in_play = white_piece.move_to(white_to_X, white_to_Y, board_in_play)
            print("The " + bold_start + "configuration after " + bold_end + "White's move is: ")
            conf2unicode(board_in_play)

            if is_checkmate(False, board_in_play):
                print("Game " + bold_start + "over. " + bold_end + "White wins.")
                return False

            if is_stalemate(True, board_in_play):
                print("Game " + bold_start + "over. " + bold_end + "Draw")
                return False

            return False
        else:
            white_move = input("This " + bold_start + "is not " + bold_end + "a valid move. " + bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "White: ")
             if white_move.strip().lower() == "quit":
                filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
                save_board(filename_store, board_in_play)
                print("The game configuration saved.")
                return False

                white_piece_move_from: Tuple(int) = location2index(white_move[:2])
                white_piece_move_to: Tuple(int) = location2index(white_move[2:])
                white_to_X: int = white_piece_move_to[0]
                white_to_Y: int = white_piece_move_to[1]
                white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)

                if not white_piece.can_move_to(white_to_X, white_to_Y, board_in_play) or not piece_at(
                        white_piece_move_from[0], white_piece_move_from[1], board_in_play):
                    white_move = input(
                        "This " + bold_start + "is not " + bold_end + "a valid move. " + bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "White: ")
                    if white_move.strip().lower() == "quit":
                        filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
                        save_board(filename_store, board_in_play)
                        print("The game configuration saved.")
                        return False
                    white_piece_move_from: Tuple(int) = location2index(white_move[:2])
                    white_piece_move_to: Tuple(int) = location2index(white_move[2:])
                    white_to_X: int = white_piece_move_to[0]
                    white_to_Y: int = white_piece_move_to[1]
                    white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)
                else:
                    white_input = False




            # creates black move and creates new board if valid
        black_piece_move = find_black_move(board_in_play)
        black_to_move: Piece = black_piece_move[0]
        black_X: int = black_piece_move[1]
        black_Y: int = black_piece_move[2]
        black_to_move.move_to(black_X, black_Y, board_in_play)
        black_orig_loc: str = index2location(black_to_move.pos_X, black_to_move.pos_Y)
        black_loc: str = index2location(black_X, black_Y)
        print(
            bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "Black " + bold_start + "is " + bold_end + f"{black_orig_loc + black_loc}. The " + bold_start + "configuration after " + bold_end + "Black's move " + bold_start + "is:" + bold_end)
        board_in_play = black_to_move.move_to(black_X, black_Y, board_in_play)
        conf2unicode(board_in_play)

        if is_checkmate(True, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "Black wins.")
            return False

        if is_stalemate(False, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "Draw")
            return False

        # creates white piece to move and checks that the move is valid and creates new board it it is.






        if is_checkmate(False, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "White wins.")
            return False

        if is_stalemate(True, board_in_play):
            print("Game " + bold_start + "over. " + bold_end +  "Draw")
            return False

        # creates black move and creates new board if valid
        black_piece_move = find_black_move(board_in_play)
        black_to_move: Piece = black_piece_move[0]
        black_X: int = black_piece_move[1]
        black_Y: int = black_piece_move[2]
        black_to_move.move_to(black_X, black_Y, board_in_play)
        black_orig_loc: str = index2location(black_to_move.pos_X, black_to_move.pos_Y)
        black_loc: str = index2location(black_X, black_Y)
        print(bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "Black " + bold_start + "is " + bold_end + f"{black_orig_loc + black_loc}. The " + bold_start + "configuration after " + bold_end + "Black's move " + bold_start + "is:" + bold_end)
        board_in_play = black_to_move.move_to(black_X, black_Y, board_in_play)
        conf2unicode(board_in_play)


        if is_checkmate(True, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "Black wins.")
            return False

        if is_stalemate(False, board_in_play):
            print("Game " + bold_start + "over. " + bold_end +  "Draw")
            return False

run()