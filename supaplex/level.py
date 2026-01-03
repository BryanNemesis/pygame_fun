import pygame
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supaplex.character import Character
    from supaplex.entities.entity import Entity


class Cell:
    def __init__(self, x: int, y=int, field: "Entity" = None):
        self.pos = pygame.Vector2(x, y)
        self.field = field


class Level:
    def __init__(self, dimensions: pygame.Vector2, cell_size_px: int):
        self.size = dimensions
        self.surface = pygame.Surface(self.size * cell_size_px)
        self.cell_size_px = cell_size_px

        self.cells = [
            [Cell(x, y) for y in range(int(dimensions.y))]
            for x in range(int(dimensions.x))
        ]

    # calculate the offset of the level within a view, expressed in number of cells.
    # offset is based on the character's position within the level and its proximity to level borders.
    def get_offset(
        self, player: "Character", view_dimensions: pygame.Vector2
    ) -> pygame.Vector2:
        offset = pygame.Vector2()

        # TODO: this doesn't have to be calculated each time.
        distance_from_border_x = math.floor(view_dimensions.x / 2)
        # When close to the left border, keep the left border on the left end of the view.
        if player.pos.x < distance_from_border_x:
            offset.x = 0
        # When between the borders, keep the player in the center.
        elif player.pos.x < self.size.x - distance_from_border_x - 1:
            offset.x = player.pos.x - distance_from_border_x
        # When close to the right border, keep the right border on the right end of the view.
        else:
            offset.x = self.size.x - view_dimensions.x

        # TODO: this doesn't have to be calculated each time.
        distance_from_border_y = math.floor(view_dimensions.y / 2)
        # When close to the top border, keep the top border on the top end of the view.
        if player.pos.y < distance_from_border_y:
            offset.y = 0
        # When between the borders, keep the player in the center.
        elif player.pos.y < self.size.y - distance_from_border_y - 1:
            offset.y = player.pos.y - distance_from_border_y
        # When close to the bottom border, keep the bottom border on the bottom end of the view.
        else:
            offset.y = self.size.y - view_dimensions.y

        return offset
    
