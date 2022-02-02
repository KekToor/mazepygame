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
image = pygame.image.load('./vacation.jpg')


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
        self.end = ()
        for i in range(0, self.count_width):
            for j in range(0, self.count_height):
                self.squares.append(Square(self.screen, self.default_width, self.default_height, self.colors[squareArray[j][i]], i * self.default_width, j * self.default_height))
        self.arrow = self.findstart(2)

    def redraw(self, state):
        if state == 0:
            for square in self.squares:
                # print(square.color, square.width, square.height, square.x, square.y)
                square.draw()
            # self.arrow.posX += 2
            self.arrow.draw()
        elif state == 1:
            self.screen.fill(self.BLACK)
            self.screen.blit(image, [0, 0])
        pygame.display.update()

    def findstart(self, val):
        for index, row in enumerate(squareArray):
            if val in row:
                arrow = Arrow(self.screen, (row.index(val)) * self.default_width, index * self.default_height, row.index(val), index)
                return arrow

    def findend(self, val):
        for index, row in enumerate(squareArray):
            if val in row:
                return row.index(val), index

    def move(self, direction):
        print(direction)
        self.end = self.findend(3)
        print(self.end[0])
        if direction == 0:
            self.arrow.posX += self.default_width
            self.arrow.arrayX += 1
        if direction == 1:
            self.arrow.posY += self.default_height
            self.arrow.arrayY += 1
        if direction == 2:
            self.arrow.posX -= self.default_width
            self.arrow.arrayX -= 1
        if direction == 3:
            self.arrow.posY -= self.default_height
            self.arrow.arrayY -= 1
        print(self.arrow.arrayX, self.arrow.arrayY)

    def endgame(self):
        if self.arrow.arrayX == self.end[0] and self.arrow.arrayY == self.end[1]:
            print('You Won!')
            return True
        return False

    def rotate(self, posNew, posOld):
        angle = (posOld - posNew) * 90
        self.arrow.source = pygame.transform.rotate(self.arrow.source, angle)
        self.screen.blit(self.arrow.source, (self.arrow.posX, self.arrow.posY))


game = Game()

facing = 0
state = 0

# 0 - vpravo; 1 - dolů; 2 - vlevo; 3 - nahoru

while Run:
    clock.tick(game.FPS)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and facing != 0:
        game.rotate(0, facing)
        facing = 0
    elif keys[pygame.K_s] and facing != 1:
        game.rotate(1, facing)
        facing = 1
    elif keys[pygame.K_a] and facing != 2:
        game.rotate(2, facing)
        facing = 2
    elif keys[pygame.K_w] and facing != 3:
        game.rotate(3, facing)
        facing = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Run = False
            elif event.key == pygame.K_SPACE:
                game.move(facing)
                if game.endgame():
                    pygame.mixer.init()
                    pygame.mixer.music.load('vacation.mp3')
                    pygame.mixer.music.set_volume(0.25)
                    pygame.mixer.music.play()
                    state = 1

    game.redraw(state)
