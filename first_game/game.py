import pygame

pygame.init()

BASE_SIZE_PX = 150
HEIGHT, WIDTH = 5, 7
screen = pygame.display.set_mode([WIDTH * BASE_SIZE_PX, HEIGHT * BASE_SIZE_PX])
clock = pygame.time.Clock()
running = True


class Grid:
    def __init__(self, width, height):
        # these are centers of each cell
        self.rows = [
            [[x * BASE_SIZE_PX - BASE_SIZE_PX // 2, y * BASE_SIZE_PX - BASE_SIZE_PX // 2]
            for x in range(1, width + 1)] for y in range(1, height + 1)
        ]

    def get_cell_center(self, player_pos):
        return self.rows[player_pos[0]][player_pos[1]]

class Character:
    def __init__(self, sprite):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        
    def set_pos(self, pos):
        # uhh
        self.rect.center = [pos[0], pos[1]]

    def get_pos(self):
        return self.rect.center
    
    def x(self):
        return self.rect.center[0]
    
    def y(self):
        return self.rect.center[1]

grid = Grid(WIDTH, HEIGHT)
player = Character("../kenney_animal-pack-redux/PNG/Round (outline)/chicken.png")

# this should be a class attribute too
player_pos = [0, 0]
player.set_pos(grid.get_cell_center(player_pos))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos[0] -= 1
                if player_pos[0] < 0:
                    player_pos[0] = 0
                player.set_pos(grid.get_cell_center(player_pos))
            if event.key == pygame.K_s:
                player_pos[0] += 1
                if player_pos[0] > HEIGHT - 1:
                    player_pos[0] = HEIGHT - 1
                player.set_pos(grid.get_cell_center(player_pos))
            if event.key == pygame.K_a:
                player_pos[1] -= 1
                if player_pos[1] < 0:
                    player_pos[1] = 0
                player.set_pos(grid.get_cell_center(player_pos))
            if event.key == pygame.K_d:
                player_pos[1] += 1
                if player_pos[1] > WIDTH - 1:
                    player_pos[1] = WIDTH - 1
                player.set_pos(grid.get_cell_center(player_pos))

    screen.fill("white")
    pygame.key.set_repeat(500, 100)

    screen.blit(player.sprite, player.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()
