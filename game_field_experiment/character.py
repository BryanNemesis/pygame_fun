import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_field_experiment.level import Level


class Character:
    def __init__(self, sprite, size_px):
        sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(sprite, [size_px, size_px])
        self.rect = self.sprite.get_rect()
        self.moving = False
        # 1 is slow as fuck, 10 is fast as shit
        # TODO: make this unit mean something
        self.mspd = 5

    # Put the character onto a level on the given position
    def set_to_level(self, level: "Level", position=pygame.Vector2(0, 0)):
        self.level = level
        self.pos = position.copy()
        self.target_pos = position.copy()

    def move_up(self):
        if not self.moving and self.pos.y > 0:
            self.moving = True
            self.target_pos.y -= 1

    def move_down(self):
        if not self.moving and self.pos.y < self.level.size.y - 1:
            self.moving = True
            self.target_pos.y += 1

    def move_left(self):
        if not self.moving and self.pos.x > 0:
            self.moving = True
            self.target_pos.x -= 1

    def move_right(self):
        if not self.moving and self.pos.x < self.level.size.x - 1:
            self.moving = True
            self.target_pos.x += 1

    # Move the character towards the target_position based on its move speed.
    def update_pos(self, dt: float):
        if self.moving:
            direction = (self.target_pos - self.pos).normalize()
            self.pos += (direction * dt * self.mspd) / 1000
            if (self.target_pos - self.pos).normalize() != direction:
                self.pos = self.target_pos.copy()
                self.moving = False
