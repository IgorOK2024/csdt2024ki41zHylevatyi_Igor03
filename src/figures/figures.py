class FigureColor:
    """
    Colors of figures
    EMPTY: Empty field
    WHITE: Field with white-color figure
    BLACK: Field with black-color figure
    """
    EMPTY = '·'
    WHITE = 0
    BLACK = 1


class FigureCode:
    """Codes of figures"""
    pawn = 'pawn'
    rook = 'rook'


class Figure:
    """Base class of all figures"""
    color = ...
    x: int
    y: int
    img: tuple
    code: str

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return self.img[self.color]
