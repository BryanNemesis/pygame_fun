import pygame
from grid import Grid
from character import Character
from fields.chick import Chick
from utility import Position

pygame.init()

CELL_SIZE_PX = 70
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

chicken_left = 1

grid = Grid(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE_PX, OFFSET, OFFSET_TOP)
player = Character(
    "../kenney_animal-pack-redux/PNG/Round without details (Outline)/chicken.png",
    CELL_SIZE_PX,
)
player.set_to_grid(grid)

title = pygame.image.load("./logo.png")
title_rect = title.get_rect()
title_rect.top = OFFSET
title_rect.right = screen.get_width() - OFFSET

chick = Chick(
    "../kenney_animal-pack-redux/PNG/Round without details (Outline)/chick.png",
    CELL_SIZE_PX,
)
chick.set_to_grid(grid, Position(2, 2))

font = pygame.font.Font(None, 36)

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
    if player.pos == chick.pos:
        chick.die()
        chicken_left -= 1

    # Draw shit

    grid.draw_bg(screen)
    grid.draw_as_dots(screen)

    # supposedly using convert makes it render quicker

    if not chick.dead:
        screen.blit(chick.sprite.convert(screen), chick.rect)
    screen.blit(player.sprite.convert(screen), player.rect)

    chicken_left_text = f"{chicken_left} chicken remaining"
    text_surface = font.render(chicken_left_text, True, "black")
    screen.blit(text_surface, (OFFSET, OFFSET))

    screen.blit(title, title_rect)
    grid.draw_borders(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()
