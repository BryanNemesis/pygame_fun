import pygame
from fields.field import Field
from sprite_provider import SpriteProvider


class Empty(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.sprite = SpriteProvider.empty
        self.edible = False
