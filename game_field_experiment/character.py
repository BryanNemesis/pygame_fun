import pygame
from sprite_provider import SpriteProvider
from typing import TYPE_CHECKING
from fields.empty import Empty

if TYPE_CHECKING:
    from game_field_experiment.level import Cell, Level


class Character(pygame.Surface):
    direction_vectors = {
        "left": pygame.Vector2((-1, 0)),
        "right": pygame.Vector2((1, 0)),
        "up": pygame.Vector2((0, -1)),
        "down": pygame.Vector2((0, 1)),
    }

    def __init__(self, size_px):
        super().__init__((size_px, size_px))
        self.sprite = SpriteProvider.murphy

        self.moving = False
        self.direction = None

        # How many miliseconds it takes to cross 1 field
        self.mspd = 200

        self.win = False

    # Put the character onto a level on the given position
    def set_to_level(self, level: "Level", position=pygame.Vector2(0, 0)):
        self.level = level
        self.pos = position.copy()
        self.target_pos = position.copy()

    def _touching_border(self, direction: str) -> bool:
        match direction:
            case "up":
                return self.pos.y == 0
            case "down":
                return self.pos.y == self.level.size.y - 1
            case "left":
                return self.pos.x == 0
            case "right":
                return self.pos.y == self.level.size.y - 1
                
    def _move(self, direction: str):
        if not (self.moving or self._touching_border(direction)):
            target_pos = self.pos + self.direction_vectors[direction]
            target_cell: "Cell" = self.level.cells[int(target_pos.y)][int(target_pos.x)]

            if target_cell.field.exit:
                self.win = True

            if not target_cell.field.solid:
                self.moving = True
                self.direction = direction
                self.target_pos = target_pos

    def move_up(self):
        return self._move("up")
    
    def move_down(self):
        return self._move("down")
    
    def move_left(self):
        return self._move("left")

    def move_right(self):
        return self._move("right")

    # Move the character towards the target_position based on its move speed.
    def update_pos(self, dt: float):
        if self.moving:
            self.pos += Character.direction_vectors[self.direction] * dt / self.mspd

            # End movement when player has landed on the target_pos
            if (self.target_pos - self.pos).magnitude_squared() < 0.002:
                self.pos = self.target_pos.copy()
                self.moving = False
                self.direction = None

                current_cell = self.level.cells[int(self.pos.y)][int(self.pos.x)]
                if current_cell.field.edible:
                    current_cell.field = Empty(self.pos)

    def update_sprite(self, pressed):
        if (
            not self.direction
            and not pressed[pygame.K_UP]
            and not pressed[pygame.K_DOWN]
            and not pressed[pygame.K_LEFT]
            and not pressed[pygame.K_RIGHT]
        ):
            # TODO: let's not update it every frame when it's not moving
            self.sprite = SpriteProvider.murphy

        elif self.direction:
            # pretty good measure of progress of movement to the next cell
            progress = abs(self.direction_vectors[self.direction] * self.pos) % 1

            if self.direction in ["left", "up"]:
                self.sprite = SpriteProvider.murphy_moving_left[round(progress * 14)]

            elif self.direction in ["right", "down"]:
                self.sprite = SpriteProvider.murphy_moving_right[round(progress * 14)]
