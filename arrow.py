import pygame


class Arrow(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, **kwargs):
        super(Arrow, self).__init__(**kwargs)
        self.posX = x
        self.posY = y
        self.screen = screen
        self.source = pygame.image.load('./arrow.png').convert_alpha()

    def draw(self):
        self.screen.blit(self.source, (self.posX, self.posY))

        # with self.canvas:
        #     Image(source='./arrow.png', pos=(self.posX + (0.1 * self.arrowW), self.posY + (0.1 * self.arrowH)), size=(0.8*self.arrowW, 0.8*self.arrowH))
        #


        