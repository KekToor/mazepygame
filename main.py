import pygame

from square import Square
from arrow import Arrow

squareArray = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]

clock = pygame.time.Clock()
Run = True


class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    FPS = 60
    width = 1280
    height = 720
    count_width = 20
    count_height = 12

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Videohra')
        self.default_width = int(self.width / self.count_width)
        self.default_height = int(self.height / self.count_height)
        self.colors = [self.WHITE, self.BLACK, self.GREEN, self.RED]
        self.squares = []
        for i in range(0, self.count_width):
            for j in range(0, self.count_height):
                self.squares.append(Square(self.screen, self.default_width, self.default_height, self.colors[squareArray[j][i]], i * self.default_width, j * self.default_height))
        self.arrow = self.findstart(2)

    def redraw(self):
        for square in self.squares:
            print(square.color, square.width, square.height, square.x, square.y)
            square.draw()
        self.arrow.draw()
        pygame.display.update()

    def findstart(self, val):
        for index, row in enumerate(squareArray):
            if val in row:
                arrow = Arrow(self.screen, (row.index(val)) * self.default_width, index * self.default_height)
                return arrow
game = Game()


while Run:
    clock.tick(game.FPS)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Run = False
    game.redraw()
    #     self.sipka = self.findstart(2)