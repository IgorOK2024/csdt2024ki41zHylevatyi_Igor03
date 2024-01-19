from figures.figures import Figure, FigureColor, FigureCode


class Rook(Figure):
    """Rook"""
    img = ('♜', '♖')
    code = FigureCode.rook

    def x_moves(self, board, moves_list):
        """Moves on horizontal"""
        now_position = [self.x, self.y]
        counter = now_position[0] - 1

        while counter >= 0:
            field_pos = [counter, self.y]
            field = board[counter][self.y]

            if field != FigureColor.EMPTY:
                if field.color != self.color:
                    moves_list.append(field_pos)
                    break

                else:
                    break

            else:
                moves_list.append(field_pos)

            counter -= 1

        counter = now_position[0] + 1

        while counter <= 7:
            field_pos = [counter, self.y]
            field = board[counter][self.y]

            if field != FigureColor.EMPTY:
                if field.color != self.color:
                    moves_list.append(field_pos)
                    break

                else:
                    break

            else:
                moves_list.append(field_pos)

            counter += 1

    def y_moves(self, board, moves_list):
        """Moves on vertical"""
        now_position = [self.x, self.y]
        counter = now_position[1] - 1

        while counter >= 0:
            field_pos = [self.x, counter]
            field = board[field_pos[0]][field_pos[1]]

            if field != FigureColor.EMPTY:
                if field.color != self.color:
                    moves_list.append(field_pos)
                    break

                else:
                    break

            else:
                moves_list.append(field_pos)

            counter -= 1

        counter = now_position[1] + 1

        while counter <= 7:
            field_pos = [self.x, counter]
            field = board[field_pos[0]][field_pos[1]]

            if field != FigureColor.EMPTY:
                if field.color != self.color:
                    moves_list.append(field_pos)
                    break

                else:
                    break

            else:
                moves_list.append(field_pos)

            counter += 1

    def get_moves(self, board):
        """Get all rook moves"""
        board = board.board
        moves = []

        self.x_moves(board, moves)
        self.y_moves(board, moves)

        return moves
