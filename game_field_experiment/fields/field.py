import pygame

class Field:
    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.edible = False
        self.sprite: pygame.image = None
