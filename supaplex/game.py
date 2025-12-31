import pygame
from character import Character
from fields.base import Base
from fields.chip import Chip
from fields.hardware import Hardware
from fields.exit import Exit
from fields.empty import Empty
from itertools import chain
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
LEVEL_DIMENSIONS = pygame.Vector2(10, 10)

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
player.set_to_level(level, pygame.Vector2(1, 1))

# Construct the level like a total fuckin noob
for cell in chain(*(level.cells)):
    cell.field = Base(cell.pos)

    if cell.pos.x in [0, LEVEL_DIMENSIONS.x - 1] or cell.pos.y in [
        0,
        LEVEL_DIMENSIONS.y - 1,
    ]:
        cell.field = Hardware(cell.pos)

    if cell.pos == pygame.Vector2(1, 1):
        cell.field = Empty(cell.pos)
    if cell.pos == pygame.Vector2(2, 2):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(3, 1):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(4, 3):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(5, 3):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(4, 5):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(4, 6):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(4, 7):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(4, 8):
        cell.field = Chip(cell.pos)
    if cell.pos == pygame.Vector2(8, 7):
        cell.field = Chip(cell.pos)

    if cell.pos == pygame.Vector2(8, 8):
        cell.field = Exit(cell.pos)

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

    # Draw shit onto the level
    for cell in chain(*(level.cells)):
        level.surface.blit(cell.field.sprite, cell.pos * CELL_SIZE_PX)

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

    if player.win:
        screen.blit(winner, winner_rect)

    # Display the game
    pygame.display.set_caption("supaplex ultimate")
    pygame.display.flip()

    # Tick the clock
    dt = clock.tick(60)


pygame.quit()
