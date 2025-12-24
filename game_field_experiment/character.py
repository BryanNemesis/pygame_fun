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
        self.mspd = 5
        self.path = ()

    # Put the character onto a level on the given position
    def set_to_level(self, level: "Level", position=pygame.Vector2(0, 0)):
        self.level = level
        self.pos = position.copy()
        self.target_pos = position.copy()

    def move_up(self):
        if self.pos.y > 0:
            self.moving = True
            self.target_pos.y -= 1
            self.create_path()

    def move_down(self):
        if self.pos.y < self.level.size.y - 1:
            self.moving = True
            self.target_pos.y += 1
            self.create_path()

    def move_left(self):
        if self.pos.x > 0:
            self.moving = True
            self.target_pos.x -= 1
            self.create_path()

    def move_right(self):
        if self.pos.x < self.level.size.x - 1:
            self.moving = True
            self.target_pos.x += 1
            self.create_path()

    def create_path(self):
        weights = [i / (self.mspd) for i in range(self.mspd + 1)][1:]

        self.path = iter(
            [
                pygame.Vector2(
                    pygame.math.lerp(self.pos.x, self.target_pos.x, weight),
                    pygame.math.lerp(self.pos.y, self.target_pos.y, weight),
                )
                for weight in weights
            ]
        )

    def update_pos(self):
        if self.moving:
            try:
                new_pos = next(self.path)
                self.pos = new_pos
            except StopIteration:
                self.moving = False
                self.path = ()
