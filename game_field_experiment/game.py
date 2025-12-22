import pygame
from character import Character
from level import Level
from utility import Position

pygame.init()

CELL_SIZE_PX = 70

# Must be odd numbers to be able to center the character within the view
VIEW_WIDTH, VIEW_HEIGHT = 9, 7
# Must be bigger than the view dimensions
LEVEL_WIDTH, LEVEL_HEIGHT = 20, 20
VIEW_OFFSET_TOP, VIEW_OFFSET = 50, 20
screen = pygame.display.set_mode(
    [
        (VIEW_WIDTH * CELL_SIZE_PX) + 2 * VIEW_OFFSET,
        (VIEW_HEIGHT * CELL_SIZE_PX) + VIEW_OFFSET_TOP + VIEW_OFFSET,
    ]
)
clock = pygame.time.Clock()
running = True

view = pygame.Surface((VIEW_WIDTH * CELL_SIZE_PX, VIEW_HEIGHT * CELL_SIZE_PX))
player = Character(
    "../kenney_animal-pack-redux/PNG/Round without details (Outline)/chicken.png",
    CELL_SIZE_PX,
)

level = Level(LEVEL_WIDTH, LEVEL_HEIGHT, CELL_SIZE_PX)
level_offset = Position(0, 0)

player.set_to_level(level, Position(12, 10))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()

    # Draw the level
    level.surface.fill("white")
    level.draw_coordinates()

    level.surface.blit(
        player.sprite, [player.pos.x * CELL_SIZE_PX, player.pos.y * CELL_SIZE_PX]
    )

    # Calculate the level's offset within the view
    distance_from_border_x = VIEW_WIDTH // 2
    if player.pos.x < distance_from_border_x:
        level_offset.x = 0
    elif player.pos.x < level.width - distance_from_border_x:
        level_offset.x = player.pos.x - distance_from_border_x
    else:
        level_offset.x = level.width - VIEW_WIDTH

    distance_from_border_y = VIEW_HEIGHT // 2
    if player.pos.y < distance_from_border_y:
        level_offset.y = 0
    elif player.pos.y < level.height - distance_from_border_y:
        level_offset.y = player.pos.y - distance_from_border_y
    else:
        level_offset.y = level.height - VIEW_HEIGHT

    # Draw the level within the view
    view.fill("black")
    view.blit(
        level.surface, [-level_offset.x * CELL_SIZE_PX, -level_offset.y * CELL_SIZE_PX]
    )
    pygame.draw.rect(view, "black", view.get_rect(), 1)

    # Draw the view within the screen
    screen.fill("#828282")
    screen.blit(view, (VIEW_OFFSET, VIEW_OFFSET_TOP))

    # Display the game
    pygame.display.flip()
    # dt = clock.tick(60) / 1000


pygame.quit()
