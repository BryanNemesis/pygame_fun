import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_field_experiment.level import Level

class Character:
    def __init__(self, sprite, size_px):
        sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(sprite, [size_px, size_px])
        self.rect = self.sprite.get_rect()

    # Put the character onto a level on the given position
    def set_to_level(self, level: "Level", position=pygame.Vector2(0, 0)):
        self.level = level
        self.pos = position

    def move_up(self):
        if self.pos.y > 0:
            self.pos.y -= 1

    def move_down(self):
        if self.pos.y < self.level.size.y - 1:
            self.pos.y += 1

    def move_left(self):
        if self.pos.x > 0:
            self.pos.x -= 1

    def move_right(self):
        if self.pos.x < self.level.size.x - 1:
            self.pos.x += 1
