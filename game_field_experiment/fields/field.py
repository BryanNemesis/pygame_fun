import pygame


class Field:
    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.sprite: pygame.image = None
        self.edible = False
        self.solid = False
        self.destructible = False
        self.exit = False

    def __str__(self):
        return f"{type(self).__name__} at ({int(self.pos.x)}, {int(self.pos.y)})"
