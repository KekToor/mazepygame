import pygame


class Square:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, screen, width, height, color, x, y, **kwargs):
        super(Square, self).__init__(**kwargs)
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)
