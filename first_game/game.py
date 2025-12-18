import pygame

pygame.init()

BASE_SIZE_PX = 150
HEIGHT, WIDTH = 5, 7
screen = pygame.display.set_mode([WIDTH * BASE_SIZE_PX, HEIGHT * BASE_SIZE_PX])
clock = pygame.time.Clock()
running = True

class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Grid:
    def __init__(self, width, height):
        # these are centers of each cell
        # is there a better way to do this? its kinda obscure
        self.rows = [
            [[x * BASE_SIZE_PX - BASE_SIZE_PX // 2, y * BASE_SIZE_PX - BASE_SIZE_PX // 2]
            for x in range(1, width + 1)] for y in range(1, height + 1)
        ]

    def get_cell_center(self, pos: Position):
        return self.rows[pos.y][pos.x]
    
    def draw_as_dots(self):
        for row in self.rows:
            for cell in row:
                pygame.draw.circle(screen, "grey", cell, 2)
    

class Character:
    def __init__(self, sprite):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.pos = Position()

    def set_to_grid(self, grid: Grid):
        self.grid = grid
        self.update_pos()
        
    def update_pos(self):
        self.rect.center = grid.get_cell_center(self.pos)

    def move_up(self):
        if self.pos.y > 0:
            self.pos.y -= 1
            self.update_pos()

    def move_down(self):
        if self.pos.y < HEIGHT - 1:
            self.pos.y += 1
            self.update_pos()

    def move_left(self):
        if self.pos.x > 0:
            self.pos.x -= 1
            self.update_pos()

    def move_right(self):
        if self.pos.x < WIDTH - 1:
            self.pos.x += 1
            self.update_pos()


grid = Grid(WIDTH, HEIGHT)
player = Character("../kenney_animal-pack-redux/PNG/Round (outline)/chicken.png")
player.set_to_grid(grid)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_up()
            elif event.key == pygame.K_s:
                player.move_down()
            elif event.key == pygame.K_a:
                player.move_left()
            elif event.key == pygame.K_d:
                player.move_right()

    screen.fill("white")
    pygame.key.set_repeat(500, 100)

    grid.draw_as_dots()
    screen.blit(player.sprite, player.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()
