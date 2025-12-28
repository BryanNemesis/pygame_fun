import pygame
from fields.field import Field
from fields.empty import Empty
from sprite_provider import SpriteProvider

class Base(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.sprite = SpriteProvider.base
        self.edible = True
