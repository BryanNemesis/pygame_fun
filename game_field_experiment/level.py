import pygame


class Level:
    def __init__(self, width, height, cell_size_px):
        self.surface = pygame.Surface((width * cell_size_px, height * cell_size_px))
        self.width = width
        self.height = height
        self.cell_size_px = cell_size_px

        self.cells = [
            [
                (
                    (x * cell_size_px),
                    (y * cell_size_px),
                )
                for x in range(width)
            ]
            for y in range(height)
        ]

    def draw_coordinates(self):
        font = pygame.font.Font("../Bittypix Monospace.otf", 8)

        for x, row in enumerate(self.cells):
            for y, cell in enumerate(row):
                text = f"({x},{y})"
                text_surface = font.render(text, True, "#7c7c7c")
                text_rect = text_surface.get_rect()
                text_rect.center = [
                    cell[0] + self.cell_size_px // 2,
                    cell[1] + self.cell_size_px // 2,
                ]
                self.surface.blit(text_surface, text_rect)
