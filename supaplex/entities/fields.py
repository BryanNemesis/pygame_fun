import pygame
from entities.entity import Entity
from sprite_provider import SpriteProvider


# Fields are elements of the environment.
# They only ever occupy 1 cell and never move to a different cell.
class Field(Entity):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.edible = False
        self.solid = False
        self.destructible = False


class Empty(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.sprite = SpriteProvider.empty


class Base(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.sprite = SpriteProvider.base
        self.edible = True


class Chip(Field):
    def __init__(self, pos: pygame.Vector2, variant="normal"):
        super().__init__(pos)
        self.solid = True

        match variant:
            case "normal":
                self.sprite = SpriteProvider.chip_normal


class Hardware(Field):
    def __init__(self, pos: pygame.Vector2, variant="normal"):
        super().__init__(pos)
        self.solid = True

        match variant:
            case "normal":
                self.sprite = SpriteProvider.hw_normal


class Exit(Field):
    def __init__(self, pos: pygame.Vector2):
        super().__init__(pos)
        self.solid = True
        self.sprite = SpriteProvider.exit
