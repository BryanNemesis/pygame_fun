import pygame


class SpriteProvider:
    def __init__(self):
        self.size = 16
        self.target_size = 48

        # Load the files containing the sprites
        self._fixed = pygame.image.load("./assets/sprites/Megaplex_Sprites/FIXED.GIF")
        self._moving = pygame.image.load("./assets/sprites/Megaplex_Sprites/MOVING.GIF")

        # Map regions of the sprites to specific game elements

        # Murphy
        self.murphy = pygame.transform.scale(
            self._fixed.subsurface(
                pygame.Rect((self.size * 3, 0), (self.size, self.size))
            ),
            (self.target_size, self.target_size),
        )
        self.murphy_moving_left = pygame.transform.scale(
            self._moving.subsurface(
                pygame.Rect((self.size * 1, 4 * self.size + 2), (self.size, self.size))
            ),
            (self.target_size, self.target_size),
        )
        self.murphy_moving_right = pygame.transform.scale(
            self._moving.subsurface(
                pygame.Rect((self.size * 4, 4 * self.size + 2), (self.size, self.size))
            ),
            (self.target_size, self.target_size),
        )
