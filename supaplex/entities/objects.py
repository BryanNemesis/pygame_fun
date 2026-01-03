import pygame
from entities.entity import Entity
from entities.fields import Empty
from sprite_provider import SpriteProvider
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supaplex.level import Cell, Level

# Objects (what a name!) are entities that can move,
# and therefore they have to be accept a Level as a parameter.
class Object(Entity):
    def __init__(self, pos: pygame.Vector2, level: "Level"):
        super().__init__(pos)
        self.target_pos = pos.copy()
        self.last_pos = pos.copy()
        self.level = level
        self.level.cells[int(pos.x)][int(pos.y)].entity = self

    def update_pos(self, dt):
        raise NotImplementedError


class Stone(Object):
    down_vector = pygame.Vector2((0, 1))

    def __init__(self, pos: pygame.Vector2, level: "Level"):
        super().__init__(pos, level)
        # TODO: this parameter should be for fields
        self.solid = True
        self.sprite = SpriteProvider.stone

        self.falling = False
        # How many miliseconds it takes to fall 1 field
        self.fall_speed = 200

    def update_pos(self, dt: float):
        # Continue the fall
        if self.falling:
            diff = Stone.down_vector * dt / self.fall_speed
            self.pos += diff

            # End movement when stone has landed on the target_pos
            if (self.target_pos - self.pos).magnitude_squared() < 0.002:
                self.pos = self.target_pos.copy()
                self.falling = False

                current_cell = self.level.cells[int(self.pos.x)][int(self.pos.y)]
                current_cell.entity = self

                above_pos = self.pos - Stone.down_vector
                cell_above: Cell = self.level.cells[int(above_pos.x)][int(above_pos.y)]
                cell_above.entity = Empty(above_pos)

        if not self.falling:
            # See what's below
            below_pos = self.pos + Stone.down_vector
            cell_below: Cell = self.level.cells[int(below_pos.x)][int(below_pos.y)]

            # Begin the fall
            if isinstance(cell_below.entity, Empty):
                self.falling = True
                self.target_pos = below_pos
                cell_below.entity = self
