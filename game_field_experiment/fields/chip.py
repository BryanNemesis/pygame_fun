import pygame
from fields.field import Field
from sprite_provider import SpriteProvider


class Chip(Field):
    def __init__(self, pos: pygame.Vector2, variant="normal"):
        super().__init__(pos)
        self.solid = True

        match variant:
            case "normal":
                self.sprite = SpriteProvider.chip_normal
