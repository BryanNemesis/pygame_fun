import pygame
from utility import Position
from level import Level

class Character:
    def __init__(self, sprite, size_px):
        sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(sprite, [size_px, size_px])
        self.rect = self.sprite.get_rect()

    def set_to_level(self, level: Level, position=Position(0, 0)):
        self.level = level
        self.pos = position

    def move_up(self):
        if self.pos.y > 0:
            self.pos.y -= 1

    def move_down(self):
        if self.pos.y < self.level.height - 1:
            self.pos.y += 1

    def move_left(self):
        if self.pos.x > 0:
            self.pos.x -= 1

    def move_right(self):
        if self.pos.x < self.level.width - 1:
            self.pos.x += 1
