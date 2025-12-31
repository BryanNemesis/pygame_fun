import pygame
from fields.field import Field
from sprite_provider import SpriteProvider


class Exit(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.exit = True
        self.solid = True
        self.sprite = SpriteProvider.exit

