import pygame
from utility import Position


class Grid:
    def __init__(self, width, height, cell_size_px, offset, offset_top):
        # these are centers of each cell
        # is there a better way to do this? its kinda obscure
        self.width = width
        self.height = height
        self.cell_size_px = cell_size_px
        self.offset = offset
        self.offset_top = offset_top
        self.rect: pygame.Rect = [
            self.offset,
            self.offset_top,
            self.width * self.cell_size_px,
            self.height * self.cell_size_px,
        ]

        self.rows = [
            [
                (
                    (x * cell_size_px - cell_size_px // 2) + offset,
                    (y * cell_size_px - cell_size_px // 2) + offset_top,
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
                pygame.draw.circle(screen, "black", cell, 1)

    def draw_borders(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "black", self.rect, 1)

    def draw_bg(self, screen: pygame.Surface):
        screen.fill("#343434", self.rect)

    
