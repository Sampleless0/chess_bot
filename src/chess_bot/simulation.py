import chess
import chess.engine
import random
import torch



def play_one_game():

    # fresh board
    board = chess.Board()


    for move in range(400):

        # grab legal moves
        legal_moves = list(board.legal_moves)

        # bot plays at random

        choice = random.choice(legal_moves)

        board.push(choice)

        print(choice)

        if board.is_game_over():
            print('yay game ended')
            break

play_one_game()