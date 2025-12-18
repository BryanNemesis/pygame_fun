import pygame
from grid import Grid
from character import Character
from utility import OffsetBox

pygame.init()

CELL_SIZE_PX = 68
GRID_HEIGHT, GRID_WIDTH = 8, 12
OFFSET_TOP, OFFSET = 100, 20
screen = pygame.display.set_mode(
    [
        (GRID_WIDTH * CELL_SIZE_PX) + 2 * OFFSET,
        (GRID_HEIGHT * CELL_SIZE_PX) + OFFSET_TOP + OFFSET,
    ]
)
clock = pygame.time.Clock()
running = True

grid = Grid(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE_PX, OFFSET, OFFSET_TOP)
player = Character("../kenney_animal-pack-redux/PNG/Round without details (Outline)/chicken.png", CELL_SIZE_PX)
player.set_to_grid(grid)

title = pygame.image.load("./logo.png")
title_rect = title.get_rect()
title_rect.center = [screen.get_width() // 2, OFFSET_TOP // 2]


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

    screen.fill("#92A2F7")
    pygame.key.set_repeat(200, 200)

    player.update_pos()
    grid.draw_bg(screen)
    grid.draw_as_dots(screen)
    # supposedly using convert makes it render quicker
    screen.blit(player.sprite.convert(screen), player.rect)
    screen.blit(title, title_rect)
    grid.draw_borders(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
