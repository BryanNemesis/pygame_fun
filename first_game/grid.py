import pygame
from position import Position


class Grid:
    def __init__(self, width, height, base_size_px):
        # these are centers of each cell
        # is there a better way to do this? its kinda obscure
        self.width = width
        self.height = height
        self.rows = [
            [
                (
                    x * base_size_px - base_size_px // 2,
                    y * base_size_px - base_size_px // 2,
                )
                for x in range(1, width + 1)
            ]
            for y in range(1, height + 1)
        ]

    def get_cell_center(self, pos: Position):
        return self.rows[pos.y][pos.x]

    def draw_as_dots(self, screen: pygame.Surface):
        for row in self.rows:
            for cell in row:
                pygame.draw.circle(screen, "grey", cell, 2)
