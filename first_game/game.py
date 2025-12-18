import pygame
from grid import Grid
from character import Character

pygame.init()

BASE_SIZE_PX = 150
HEIGHT, WIDTH = 5, 7
screen = pygame.display.set_mode([WIDTH * BASE_SIZE_PX, HEIGHT * BASE_SIZE_PX])
clock = pygame.time.Clock()
running = True


grid = Grid(WIDTH, HEIGHT, BASE_SIZE_PX)
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
    grid.draw_as_dots(screen)
    screen.blit(player.sprite, player.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()
