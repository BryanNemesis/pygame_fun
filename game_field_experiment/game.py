import pygame
from character import Character
from level import Level

pygame.init()


# Define constants

# Size of a level cell in pixels
CELL_SIZE_PX = 70

# Size of the game view expressed in amount of cells
# Must be odd numbers to be able to center the character within the view
VIEW_DIMENSIONS = pygame.Vector2(7, 5)

# Size of the level expressed in amount of cells
# Must be bigger than the view dimensions
LEVEL_DIMENSIONS = pygame.Vector2(10, 10)

# Offset of the game view within the screen in pixels
VIEW_OFFSET_TOP, VIEW_OFFSET = 50, 20

# Pygame stuff
clock = pygame.time.Clock()
running = True

# Create screen
screen = pygame.display.set_mode(
    [
        (VIEW_DIMENSIONS.x * CELL_SIZE_PX) + 2 * VIEW_OFFSET,
        (VIEW_DIMENSIONS.y * CELL_SIZE_PX) + VIEW_OFFSET_TOP + VIEW_OFFSET,
    ]
)

# Create view
view = pygame.Surface(VIEW_DIMENSIONS * CELL_SIZE_PX)

# Create level
level = Level(LEVEL_DIMENSIONS, CELL_SIZE_PX)

# Create player character
player = Character(
    "../kenney_animal-pack-redux/PNG/Round without details (Outline)/chicken.png",
    CELL_SIZE_PX,
)
player.set_to_level(level, pygame.Vector2(0, 0))


# Game loop
while running:
    # Read inputs
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

    # Draw the player onto the level
    player.update_pos()
    level.surface.blit(player.sprite, player.pos * CELL_SIZE_PX)

    # Calculate the level's offset within the view
    level_offset = level.get_offset(player, VIEW_DIMENSIONS)

    # Draw the level within the view
    view.fill("black")
    view.blit(level.surface, -level_offset * CELL_SIZE_PX)

    # Draw a border around the view
    pygame.draw.rect(view, "black", view.get_rect(), 1)

    # Draw the view within the screen
    screen.fill("#828282")
    screen.blit(view, (VIEW_OFFSET, VIEW_OFFSET_TOP))

    # Display the game
    pygame.display.flip()

    # Tick the clock
    dt = clock.tick(60) / 1000


pygame.quit()
