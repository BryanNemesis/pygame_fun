from pygame import Surface

# TODO: there's gotta be a builtin class for this lol
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
class OffsetBox:
    def __init__(self, screen: Surface, top=0, left=0, right=0, bottom=0):

        # TODO: make these private?
        self.top = top
        self.left = left
        self.right = screen.get_width() - right
        self.bottom = screen.get_height() - bottom

        self.top_left = Position(self.top, self.left)
        self.top_right = Position(self.top, self.right)
        self.bottom_left = Position(self.bottom, self.left)
        self.bottom_right = Position(self.bottom, self.right)