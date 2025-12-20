import pygame
from utility import Position
from grid import Grid


class Chick:
    def __init__(self, sprite, size_px):
        sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(sprite, [size_px - 12, size_px - 12])
        self.rect = self.sprite.get_rect()
        self.pos = Position()
        self.dead = False

    def set_to_grid(self, grid: Grid, pos: Position):
        self.grid = grid
        self.pos = pos
        self.rect.center = self.grid.get_cell_center(self.pos)

    def die(self):
        self.dead = True
        self.pos = Position(-1, -1)
        del self.sprite