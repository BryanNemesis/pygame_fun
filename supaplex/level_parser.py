import pygame
from level import Level
from entities.fields import *
from entities.objects import *
from entities.character import Character


class LevelParser:
    def __init__(self, file_path: str, cell_size_px: int):
        self.file_path = file_path
        self.cell_size_px = cell_size_px

    def create_level(self) -> tuple[Level, Character, list[Object]]:
        lines = []

        with open(self.file_path, "r") as file:
            for line in file:
                lines.append([char for char in line.strip()])

        lvl_width = len(lines)
        lvl_height = max([len(line) for line in lines])
        level = Level(pygame.Vector2(lvl_height, lvl_width), self.cell_size_px)

        objects = []

        for y, row in enumerate(lines):
            for x, entity in enumerate(row):
                cell = level.cells[x][y]
                match entity:
                    case " ":
                        cell.entity = Empty(cell.pos)
                    case "#":
                        cell.entity = Hardware(cell.pos)
                    case "-":
                        cell.entity = Base(cell.pos)
                    case "=":
                        cell.entity = Chip(cell.pos)
                    case "E":
                        cell.entity = Exit(cell.pos)

                    case "o":
                        stone = Stone(cell.pos, level)
                        cell.entity = stone
                        objects.append(stone)
                    case "e":
                        character = Character(cell.pos, level)
                        cell.entity = character
                        objects.append(character)

        return level, character, objects
