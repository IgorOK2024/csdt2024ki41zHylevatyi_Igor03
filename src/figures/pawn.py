from figures.figures import Figure, FigureColor, FigureCode


class Pawn(Figure):
    """Pawn"""
    img = ('♟', '♙')
    code = FigureCode.pawn

    def get_moves(self, board):
        """Get all pawn moves"""
        board = board.board
        moves = []

        # If pawn color is white
        if self.color == FigureColor.WHITE:
            if self.x > 0:
                if board[self.x - 1][self.y] == FigureColor.EMPTY:
                    moves.append([self.x - 1, self.y])

                if self.x > 1:
                    if board[self.x - 2][self.y] == FigureColor.EMPTY and board[self.x - 1][self.y] == FigureColor.EMPTY and self.x == 6:
                        moves.append([self.x - 2, self.y])

                if self.y > 0:
                    if board[self.x - 1][self.y - 1] != FigureColor.EMPTY:
                        if board[self.x - 1][self.y - 1].color != self.color:
                            moves.append([self.x - 1, self.y - 1])

                if self.y < 7:
                    if board[self.x - 1][self.y + 1] != FigureColor.EMPTY:
                        if board[self.x - 1][self.y + 1].color != self.color:
                            moves.append([self.x - 1, self.y + 1])

        # If pawn color is black
        elif self.color == FigureColor.BLACK:
            if self.x < 7:
                if board[self.x + 1][self.y] == FigureColor.EMPTY:
                    moves.append([self.x + 1, self.y])

                if self.x < 6:
                    if (board[self.x + 2][self.y] == FigureColor.EMPTY and
                            board[self.x + 1][self.y] == FigureColor.EMPTY and
                            self.x == 1):
                        moves.append([self.x + 2, self.y])

                if self.y > 0:
                    if board[self.x + 1][self.y - 1] != FigureColor.EMPTY:
                        if board[self.x + 1][self.y - 1].color != self.color:
                            moves.append([self.x + 1, self.y - 1])

                if self.y < 7:
                    if board[self.x + 1][self.y + 1] != FigureColor.EMPTY:
                        if board[self.x + 1][self.y + 1].color != self.color:
                            moves.append([self.x + 1, self.y + 1])

        return moves
