import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_field_experiment.level import Level
    from game_field_experiment.sprite_provider import SpriteProvider


class Character(pygame.Surface):
    direction_vectors = {
        "left": pygame.Vector2((-1, 0)),
        "right": pygame.Vector2((1, 0)),
        "up": pygame.Vector2((0, -1)),
        "down": pygame.Vector2((0, 1)),
    }

    def __init__(self, sprites: "SpriteProvider", size_px):
        super().__init__((size_px, size_px))
        self.sprite_provider = sprites
        self.sprite = sprites.murphy

        self.moving = False
        self.direction = None

        # How many miliseconds it takes to cross 1 field
        self.mspd = 200

    # Put the character onto a level on the given position
    def set_to_level(self, level: "Level", position=pygame.Vector2(0, 0)):
        self.level = level
        self.pos = position.copy()
        self.target_pos = position.copy()

    def move_up(self):
        if not self.moving and self.pos.y > 0:
            self.moving = True
            self.direction = "up"
            self.target_pos.y -= 1

    def move_down(self):
        if not self.moving and self.pos.y < self.level.size.y - 1:
            self.moving = True
            self.direction = "down"
            self.target_pos.y += 1

    def move_left(self):
        if not self.moving and self.pos.x > 0:
            self.moving = True
            self.direction = "left"
            self.target_pos.x -= 1

    def move_right(self):
        if not self.moving and self.pos.x < self.level.size.x - 1:
            self.moving = True
            self.direction = "right"
            self.target_pos.x += 1

    # Move the character towards the target_position based on its move speed.
    def update_pos(self, dt: float):
        if self.moving:
            self.pos += (
                Character.direction_vectors[self.direction] * dt / self.mspd
            )

            if (self.target_pos - self.pos).magnitude_squared() < 0.002:
                self.pos = self.target_pos.copy()
                self.moving = False
                self.direction = None

    def update_sprite(self, pressed):
        if (
            not self.direction
            and not pressed[pygame.K_UP]
            and not pressed[pygame.K_DOWN]
            and not pressed[pygame.K_LEFT]
            and not pressed[pygame.K_RIGHT]
        ):
            self.sprite = self.sprite_provider.murphy

        elif self.direction:
            # pretty good measure of progress of movement to the next cell
            progress = abs(self.direction_vectors[self.direction] * self.pos) % 1

            if self.direction in ["left", "up"]:
                self.sprite = self.sprite_provider.murphy_moving_left_list[round(progress * 14)]

            elif self.direction in ["right", "down"]:
                self.sprite = self.sprite_provider.murphy_moving_right_list[round(progress * 14)]
