import os
import random
import time

import board
import figures


class Game:
    MOVE_SPEED = 0.7

    def __init__(self):
        self.chess_board = board.Board()
        self.fill(self.chess_board)

    @staticmethod
    def fill(chess_board):
        # Blacks
        rook = figures.Rook(figures.FigureColor.BLACK, 0, 0)
        rook2 = figures.Rook(figures.FigureColor.BLACK, 0, 7)
        pawn = figures.Pawn(figures.FigureColor.BLACK, 1, 0)
        pawn2 = figures.Pawn(figures.FigureColor.BLACK, 1, 1)
        pawn3 = figures.Pawn(figures.FigureColor.BLACK, 1, 2)
        pawn4 = figures.Pawn(figures.FigureColor.BLACK, 1, 3)
        pawn5 = figures.Pawn(figures.FigureColor.BLACK, 1, 4)
        pawn6 = figures.Pawn(figures.FigureColor.BLACK, 1, 5)
        pawn7 = figures.Pawn(figures.FigureColor.BLACK, 1, 6)
        pawn8 = figures.Pawn(figures.FigureColor.BLACK, 1, 7)

        # Whites
        rook3 = figures.Rook(figures.FigureColor.WHITE, 7, 0)
        rook4 = figures.Rook(figures.FigureColor.WHITE, 7, 7)
        pawn9 = figures.Pawn(figures.FigureColor.WHITE, 6, 0)
        pawn10 = figures.Pawn(figures.FigureColor.WHITE, 6, 1)
        pawn11 = figures.Pawn(figures.FigureColor.WHITE, 6, 2)
        pawn12 = figures.Pawn(figures.FigureColor.WHITE, 6, 3)
        pawn13 = figures.Pawn(figures.FigureColor.WHITE, 6, 4)
        pawn14 = figures.Pawn(figures.FigureColor.WHITE, 6, 5)
        pawn15 = figures.Pawn(figures.FigureColor.WHITE, 6, 6)
        pawn16 = figures.Pawn(figures.FigureColor.WHITE, 6, 7)

        chess_board.put_figure(rook)
        chess_board.put_figure(rook2)
        chess_board.put_figure(pawn)
        chess_board.put_figure(pawn2)
        chess_board.put_figure(pawn3)
        chess_board.put_figure(pawn4)
        chess_board.put_figure(pawn5)
        chess_board.put_figure(pawn6)
        chess_board.put_figure(pawn7)
        chess_board.put_figure(pawn8)

        chess_board.put_figure(rook3)
        chess_board.put_figure(rook4)
        chess_board.put_figure(pawn9)
        chess_board.put_figure(pawn10)
        chess_board.put_figure(pawn11)
        chess_board.put_figure(pawn12)
        chess_board.put_figure(pawn13)
        chess_board.put_figure(pawn14)
        chess_board.put_figure(pawn15)
        chess_board.put_figure(pawn16)

    def run(self):
        whose_move = 0

        while True:
            if whose_move == 0:
                whites_figures = self.chess_board.get_whites_figures()
                moves = []

                for i in whites_figures:
                    figure_moves = i.get_moves(self.chess_board)

                    if figure_moves:
                        move = random.choice(figure_moves)
                        moves.append([i, move])

                    else:
                        continue

                if moves:
                    move = random.choice(moves)
                    self.chess_board.move(move[0], move[1])
                    os.system('clear')
                    print(self.chess_board)
                    blacks_figures = self.chess_board.get_blacks_figures()
                    print(f'Whites: {len(whites_figures)}')
                    print(f'Blacks: {len(blacks_figures)}')
                    whose_move = 1
                    time.sleep(self.MOVE_SPEED)

                else:
                    if whites_figures:
                        print('Stalemate')

                    else:
                        print('Black won!')

                    break

            if whose_move == 1:
                blacks_figures = self.chess_board.get_blacks_figures()
                moves = []

                for i in blacks_figures:
                    figure_moves = i.get_moves(self.chess_board)

                    if figure_moves:
                        move = random.choice(figure_moves)
                        moves.append([i, move])

                    else:
                        continue

                if moves:
                    move = random.choice(moves)
                    self.chess_board.move(move[0], move[1])
                    os.system('clear')
                    print(self.chess_board)
                    whites_figures = self.chess_board.get_whites_figures()
                    print(f'Whites: {len(whites_figures)}')
                    print(f'Blacks: {len(blacks_figures)}')
                    whose_move = 0
                    time.sleep(self.MOVE_SPEED)

                else:
                    if blacks_figures:
                        print('Stalemate')

                    else:
                        print('White won!')

                    break


game = Game()
game.run()
