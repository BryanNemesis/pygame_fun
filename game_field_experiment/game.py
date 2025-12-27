import pygame
from character import Character
from level import Level
from sprite_provider import SpriteProvider

pygame.init()


# Define constants

# Size of a level cell in pixels
CELL_SIZE_PX = 48

# Size of the game view expressed in amount of cells
# Must be odd numbers to be able to center the character within the view
VIEW_DIMENSIONS = pygame.Vector2(9, 7)

# Size of the level expressed in amount of cells
# Must be bigger than the view dimensions
LEVEL_DIMENSIONS = pygame.Vector2(12, 12)

# Offset of the game view within the screen in pixels
VIEW_OFFSET_TOP, VIEW_OFFSET = 50, 20

# Pygame stuff
clock = pygame.time.Clock()
dt = 0
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

SpriteProvider.initialize()

# Create player character
player = Character(CELL_SIZE_PX)
player.set_to_level(level, pygame.Vector2(0, 0))


# Game loop
while running:
    # Read inputs
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        player.move_up()
    if pressed[pygame.K_DOWN]:
        player.move_down()
    if pressed[pygame.K_LEFT]:
        player.move_left()
    if pressed[pygame.K_RIGHT]:
        player.move_right()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the level
    level.surface.fill("black")
    level.draw_coordinates()

    # Draw the player onto the level
    player.update_pos(dt)
    player.update_sprite(pressed)
    level.surface.blit(player.sprite, player.pos * CELL_SIZE_PX)

    # Calculate the level's offset within the view
    level_offset = level.get_offset(player, VIEW_DIMENSIONS)

    # Draw the level within the view
    view.fill("black")
    view.blit(level.surface, -level_offset * CELL_SIZE_PX)

    # Draw a border around the view
    pygame.draw.rect(view, "#0B8F1F", view.get_rect(), 2)

    # Draw the view within the screen
    screen.fill("#3F3F3F")
    screen.blit(view, (VIEW_OFFSET, VIEW_OFFSET_TOP))

    # Display the game
    pygame.display.set_caption("supaplex ultimate")
    pygame.display.flip()

    # Tick the clock
    dt = clock.tick(60)


pygame.quit()
