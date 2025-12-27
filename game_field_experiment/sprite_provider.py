import pygame
from itertools import chain


class SpriteProvider:
    orig_size = 16
    target_size = 48

    def __init__(self):
        raise RuntimeError('Use the SpriteProvider class directly')

    @classmethod
    def initialize(cls):

        # Load the files containing the sprites
        cls._fixed = pygame.image.load("./assets/sprites/Megaplex_Sprites/FIXED.GIF")
        cls._moving = pygame.image.load("./assets/sprites/Megaplex_Sprites/MOVING.GIF")

        # Map regions of the sprites to specific game elements

        # Murphy
        cls.murphy = cls._prep_sprite(cls._fixed, row=0, column=3)

        # TODO: this shit is ugly af!!!
        cls.murphy_moving_left = [
            cls._prep_sprite(
                cls._moving, row=2, column=3 + i, extra_x_offset=(i * 14) - 2
            )
            for i in chain(range(7, 0, -1), range(8))
        ]

        cls.murphy_moving_right = (
            [
                cls._prep_sprite(
                    cls._moving, row=3, column=i, extra_x_offset=(i * 18) + 4
                )
                for i in range(6, -1, -1)
            ]
            + [
                cls._prep_sprite(
                    cls._moving, row=2, column=11, extra_x_offset=(8 * 14) + 2
                )
            ]
            + [
                cls._prep_sprite(
                    cls._moving, row=3, column=i, extra_x_offset=(i * 18) + 4
                )
                for i in range(7)
            ]
        )

    @classmethod
    def _prep_sprite(
        cls,
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
                        cls.orig_size * column + extra_x_offset,
                        cls.orig_size * row + extra_y_offset,
                    ),
                    (cls.orig_size, cls.orig_size),
                )
            ),
            (cls.target_size, cls.target_size),
        )
