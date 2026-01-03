import pygame
from fields.field import Field
from fields.empty import Empty
from sprite_provider import SpriteProvider
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from supaplex.level import Cell, Level

class Stone(Field):
    down_vector = pygame.Vector2((0, 1))

    def __init__(self, pos: pygame.Vector2, level: "Level"):
        super().__init__(pos)
        self.solid = True
        self.has_weight = True
        self.sprite = SpriteProvider.stone

        self.level = level
        self.target_pos = pos.copy()
        self.falling = False

        # How many miliseconds it takes to fall 1 field
        self.mspd = 2000

    def update_pos(self, dt: float):
        # Continue the fall
        if self.falling:
            diff = Stone.down_vector * dt / self.mspd
            self.pos += diff


            # End movement when stone has landed on the target_pos
            if (self.target_pos - self.pos).magnitude_squared() < 0.002:
                self.pos = self.target_pos.copy()
                self.falling = False

                current_cell = self.level.cells[int(self.pos.x)][int(self.pos.y)]
                current_cell.field = self

                above_pos = self.pos - Stone.down_vector
                cell_above: Cell = self.level.cells[int(above_pos.x)][int(above_pos.y)]
                cell_above.field = Empty(above_pos)

        else:
            # See what's below
            below_pos = self.pos + Stone.down_vector
            cell_below: Cell = self.level.cells[int(below_pos.x)][int(below_pos.y)]

            # Begin the fall
            if isinstance(cell_below.field, Empty):
                print("Start falling")
                print(f'Set target pos to {below_pos}')
                self.falling = True
                self.target_pos = below_pos
                cell_below.field = self
