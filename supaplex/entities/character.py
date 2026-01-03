import pygame
from sprite_provider import SpriteProvider
from typing import TYPE_CHECKING
from entities.fields import Empty, Exit
from entities.objects import Object

if TYPE_CHECKING:
    from supaplex.level import Cell, Level
    from supaplex.entities.fields import Field


class Character(Object):
    _direction_vectors = {
        "left": pygame.Vector2((-1, 0)),
        "right": pygame.Vector2((1, 0)),
        "up": pygame.Vector2((0, -1)),
        "down": pygame.Vector2((0, 1)),
    }

    def __init__(self, pos: pygame.Vector2, level: "Level"):
        super().__init__(pos, level)
        self.sprite = SpriteProvider.murphy
        self.moving = False
        self.direction = None

        # How many miliseconds it takes to cross 1 field
        self.mspd = 200
        self.win = False

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
            target_pos = self.pos + self._direction_vectors[direction]
            target_cell: "Cell" = self.level.cells[int(target_pos.x)][int(target_pos.y)]

            if isinstance(target_cell.entity, Exit):
                self.win = True

            # Initiate movement
            if not target_cell.entity.solid:
                self.moving = True
                self.direction = direction
                self.last_pos = self.pos.copy()
                self.target_pos = target_pos
                # Until the end of the movement, Murhpy will occupy 2 cells on the level
                target_cell.entity = self

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
            self.pos += Character._direction_vectors[self.direction] * dt / self.mspd

            # End movement when player has landed on the target_pos
            if (self.target_pos - self.pos).magnitude_squared() < 0.002:
                self.pos = self.target_pos.copy()
                self.moving = False
                self.direction = None

                # Free the previously occupied cell
                previous_cell: Cell = self.level.cells[int(self.last_pos.x)][int(self.last_pos.y)]
                previous_cell.entity = Empty(self.last_pos)


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
            progress = abs(self._direction_vectors[self.direction] * self.pos) % 1

            if self.direction in ["left", "up"]:
                self.sprite = SpriteProvider.murphy_moving_left[round(progress * 14)]

            elif self.direction in ["right", "down"]:
                self.sprite = SpriteProvider.murphy_moving_right[round(progress * 14)]
