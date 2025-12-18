import pygame
from utility import Position
from grid import Grid


class Character:
    def __init__(self, sprite, size_px):
        sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(sprite, [size_px, size_px])
        self.rect = self.sprite.get_rect()
        self.pos = Position()
        self.target_pos = Position()
        self.should_move = False
        # how many frames it takes to move
        self.mspd = 5

    def set_to_grid(self, grid: Grid):
        self.grid = grid
        self.rect.center = self.grid.get_cell_center(self.pos)

    def create_path(self):
        init_pos_px = self.grid.get_cell_center(self.pos)
        target_pos_px = self.grid.get_cell_center(self.target_pos)
        self.path = (
            [
                ((self.mspd - step) * init_pos_px[0] + step * target_pos_px[0])
                // self.mspd,
                ((self.mspd - step) * init_pos_px[1] + step * target_pos_px[1])
                // self.mspd,
            ]
            for step in range(1, self.mspd + 1)
        )

    def update_pos(self):
        if self.should_move:
            try:
                target_pos_px = next(self.path)
                self.rect.center = target_pos_px
            except StopIteration:
                self.pos.x = self.target_pos.x
                self.pos.y = self.target_pos.y
                self.should_move = False

    def move_up(self):
        if not self.should_move and self.pos.y > 0:
            self.target_pos.y -= 1
            self.create_path()
            self.should_move = True

    def move_down(self):
        if not self.should_move and self.pos.y < self.grid.height - 1:
            self.target_pos.y += 1
            self.create_path()
            self.should_move = True

    def move_left(self):
        if not self.should_move and self.pos.x > 0:
            self.target_pos.x -= 1
            self.create_path()
            self.should_move = True

    def move_right(self):
        if not self.should_move and self.pos.x < self.grid.width - 1:
            self.target_pos.x += 1
            self.create_path()
            self.should_move = True
