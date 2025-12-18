import pygame

pygame.init()

BASE_SIZE_PX = 150
HEIGHT, WIDTH = 5, 7
screen = pygame.display.set_mode([WIDTH * BASE_SIZE_PX, HEIGHT * BASE_SIZE_PX])
clock = pygame.time.Clock()
running = True


# there's gotta be a builtin class for this lol
class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

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
        self.target_pos = Position()
        self.should_move = False

    def set_to_grid(self, grid: Grid):
        self.grid = grid
        self.update_pos()

    def create_path(self):
        # over how many frames the movement will happen

        path_length = 10
        init_pos_px = grid.get_cell_center(self.pos)
        target_pos_px = grid.get_cell_center(self.target_pos)
        self.path = (
            [
                ((path_length - step) * init_pos_px[0] + step * target_pos_px[0]) // path_length,
                ((path_length - step) * init_pos_px[1] + step * target_pos_px[1]) // path_length,
            ] for step in range(1, path_length + 1)
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
        if not self.should_move and self.pos.y < HEIGHT - 1:
            self.target_pos.y += 1
            self.create_path()
            self.should_move = True

    def move_left(self):
        if not self.should_move and self.pos.x > 0:
            self.target_pos.x -= 1
            self.create_path()
            self.should_move = True

    def move_right(self):
        if not self.should_move and self.pos.x < WIDTH - 1:
            self.target_pos.x += 1
            self.create_path()
            self.should_move = True

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

    player.update_pos()
    grid.draw_as_dots()
    screen.blit(player.sprite, player.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()
