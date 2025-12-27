import pygame
from itertools import chain


class SpriteProvider:
    def __init__(self):
        self.size = 16
        self.target_size = 48

        # Load the files containing the sprites
        self._fixed = pygame.image.load("./assets/sprites/Megaplex_Sprites/FIXED.GIF")
        self._moving = pygame.image.load("./assets/sprites/Megaplex_Sprites/MOVING.GIF")

        # Map regions of the sprites to specific game elements

        # Murphy
        self.murphy = self._prep_sprite(self._fixed, row=0, column=3)
        self.murphy_moving_left = self._prep_sprite(
            self._moving, 0, 4, extra_y_offset=2
        )
        self.murphy_moving_right = self._prep_sprite(
            self._moving, 3, 4, extra_y_offset=2
        )

        # TODO: this shit is ugly af!!!
        self.murphy_moving_left_list = [
            self._prep_sprite(
                self._moving, row=2, column=3 + i, extra_x_offset=(i * 14) - 2
            )
            for i in chain(range(7, 0, -1), range(8))
        ]

        self.murphy_moving_right_list = (
            [
                self._prep_sprite(
                    self._moving, row=3, column=i, extra_x_offset=(i * 18) + 4
                )
                for i in range(6, -1, -1)
            ]
            + [
                self._prep_sprite(
                    self._moving, row=2, column=11, extra_x_offset=(8 * 14) + 2
                )
            ]
            + [
                self._prep_sprite(
                    self._moving, row=3, column=i, extra_x_offset=(i * 18) + 4
                )
                for i in range(7)
            ]
        )

    def _prep_sprite(
        self,
        sprite: pygame.Surface,
        column: int,
        row: int,
        extra_y_offset=0,
        extra_x_offset=0,
    ):
        return pygame.transform.scale(
            sprite.subsurface(
                pygame.Rect(
                    (
                        self.size * column + extra_x_offset,
                        self.size * row + extra_y_offset,
                    ),
                    (self.size, self.size),
                )
            ),
            (self.target_size, self.target_size),
        )
