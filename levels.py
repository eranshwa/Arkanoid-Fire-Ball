import pygame
import json
from bricks import Brick

def load_level(filename, brick_width, brick_height, UI_HEIGHT):
    with open(filename) as f:
        data = json.load(f)
        bricks = []
        for brick in data:
            x = brick['x']
            y = brick['y']
            color = tuple(brick['color'])
            brick_type = brick['type']

            brick = Brick(
                x * brick_width,
                UI_HEIGHT + y * brick_height,
                brick_width - 2,
                brick_height - 2,
                (255, 255, 255) if brick_type == 'multi' else color,
                brick_type,
                color
            )
            bricks.append(brick)
        return bricks
