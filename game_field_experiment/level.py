import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_field_experiment.character import Character


class Level:
    def __init__(self, dimensions: pygame.Vector2, cell_size_px: int):
        self.size = dimensions
        self.surface = pygame.Surface(self.size * cell_size_px)
        self.cell_size_px = cell_size_px
        self._font = pygame.font.Font("../Bittypix Monospace.otf", 8)

        self.cells = [
            [
                pygame.Vector2(x * cell_size_px, y * cell_size_px)
                for x in range(int(dimensions.x))
            ]
            for y in range(int(dimensions.y))
        ]

    # Draw coordinates on each level cell
    def draw_coordinates(self):
        for x, row in enumerate(self.cells):
            for y, cell in enumerate(row):
                text = f"({x},{y})"
                text_surface = self._font.render(text, True, "#7c7c7c")
                text_rect = text_surface.get_rect()
                text_rect.center = [
                    cell.x + self.cell_size_px // 2,
                    cell.y + self.cell_size_px // 2,
                ]
                self.surface.blit(text_surface, text_rect)

    # calculate the offset of the level within a view, expressed in number of cells.
    # offset is based on the character's position within the level and its proximity to level borders.
    def get_offset(
        self, player: "Character", view_dimensions: pygame.Vector2
    ) -> pygame.Vector2:
        offset = pygame.Vector2()

        distance_from_border_x = view_dimensions.x // 2
        # When close to the left border, keep the left border on the left end of the view.
        if player.pos.x < distance_from_border_x:
            offset.x = 0
        # When between the borders, keep the player in the center.
        elif player.pos.x < self.size.x - distance_from_border_x:
            offset.x = player.pos.x - distance_from_border_x
        # When close to the right border, keep the right border on the right end of the view.
        else:
            offset.x = self.size.x - view_dimensions.x

        distance_from_border_y = view_dimensions.y // 2
        # When close to the top border, keep the top border on the top end of the view.
        if player.pos.y < distance_from_border_y:
            offset.y = 0
        # When between the borders, keep the player in the center.
        elif player.pos.y < self.size.y - distance_from_border_y:
            offset.y = player.pos.y - distance_from_border_y
        # When close to the bottom border, keep the bottom border on the bottom end of the view.
        else:
            offset.y = self.size.y - view_dimensions.y

        return offset
