import pygame
from entities.fields import Field
from itertools import chain
from level_parser import LevelParser
from sprite_provider import SpriteProvider

pygame.init()

# Define constants

# Size of a level cell in pixels
CELL_SIZE_PX = 48

# Size of the game view expressed in amount of cells
# Must be odd numbers to be able to center the character within the view
VIEW_DIMENSIONS = pygame.Vector2(9, 7)

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

view = pygame.Surface(VIEW_DIMENSIONS * CELL_SIZE_PX)

SpriteProvider.initialize()

level_parser = LevelParser("./test_level.txt", CELL_SIZE_PX)
level, player, objects = level_parser.create_level()

winner = pygame.image.load("assets/winner.png")
winner_rect = winner.get_rect()
winner_rect.center = (screen.get_width() / 2, screen.get_height() / 2)

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

    # Update all objects' positions and sprites and draw them onto the level
    for obj in objects:
        obj.update_pos(dt)
        player.update_sprite(pressed)
        level.surface.blit(obj.sprite, obj.pos * CELL_SIZE_PX)

    # Draw fields onto the level
    for cell in chain(*(level.cells)):
        if isinstance(cell.entity, Field):
            level.surface.blit(cell.entity.sprite, cell.pos * CELL_SIZE_PX)

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

    if player.win:
        screen.blit(winner, winner_rect)

    # Display the game
    pygame.display.set_caption("supaplex ultimate")
    pygame.display.flip()

    # Tick the clock
    dt = pygame.math.clamp(clock.tick(60), 0, 50)


pygame.quit()
