from figures import FigureColor, Pawn, Rook, FigureCode


class Board:
    """Class of board"""

    def __init__(self):
        self.board = [[FigureColor.EMPTY for i in range(8)] for i in range(8)]  # Board creating

    def put_figure(self, figure):
        """Put figure to the board"""
        x, y = figure.x, figure.y

        if self.board[x][y] != FigureColor.EMPTY:  # If position is already busy
            raise ValueError

        self.board[x][y] = figure

    def move(self, figure, new_position):
        """Move figure to new position"""
        figure_moves = figure.get_moves(self)
        old_position = [figure.x, figure.y]

        if new_position in figure_moves:  # If figure can move to this position
            figure.x, figure.y = new_position[0], new_position[1]

            if figure.code == FigureCode.pawn and new_position[0] == 7 or new_position[0] == 0:
                self.board[new_position[0]][new_position[1]] = Rook(figure.color, new_position[0], new_position[1])
                self.board[old_position[0]][old_position[1]] = FigureColor.EMPTY  # Deleting figure from old position

            else:
                self.board[new_position[0]][new_position[1]] = self.board[old_position[0]][old_position[1]]
                self.board[old_position[0]][old_position[1]] = FigureColor.EMPTY  # Deleting figure from old position

        else:  # If figure hasn't this move in moves list
            raise ValueError

    def get_whites_figures(self):
        """Get whites figures"""
        whites = []

        for i in self.board:
            for y in i:
                if y != FigureColor.EMPTY:
                    if y.color == FigureColor.WHITE:
                        whites.append(y)

        return whites

    def get_blacks_figures(self):
        """Get blacks figures"""
        blacks = []

        for i in self.board:
            for y in i:
                if y != FigureColor.EMPTY:
                    if y.color == FigureColor.BLACK:
                        blacks.append(y)

        return blacks

    def __str__(self):
        result = ''

        counter = 8

        for i in self.board:
            result += f'{counter} | ' + '  '.join(map(str, i)) + '\n'
            counter -= 1

        result += '    a  b  c  d  e  f  g  h'

        return result
