import pygame


class Entity:
    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.sprite: pygame.image = None

    def __str__(self):
        return f"{type(self).__name__} at ({int(self.pos.x)}, {int(self.pos.y)})"
