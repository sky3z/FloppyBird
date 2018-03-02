# Pygame project
import pygame
import random
import time
from settings import *


class FloppyBird():
    # initialize pygame and create window
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 608))
        self.font_name = pygame.font.match_font(FONT_NAME)
        pygame.display.set_caption(TITLE)
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert()
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        # Gap is the space between the two wall - Gap è lo spazio tra i due muri
        self.gap = 150
        # Wallx is the distance of the walls from the beginning - è la distanza dei muri dall'inizio del gioco
        self.wallx = 200
        # BirdY is the location where the bird is located at the beginning - locazione del personaggio all'inizio del gioco
        self.birdY = 300
        # Jump initialize - inizializzazione del salto
        self.jump = 0
        # JumpSpeed is the velocity of the jump - velocità del salto
        self.jumpSpeed = 20
        self.gravity = 3
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)
        self.running = True

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 0.5
            self.birdY -= self.jumpSpeed
            self.jump -= 0.5
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    """def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("Bird", 64, RED, WIDTH / 2, HEIGHT * 1 / 6)
        self.draw_text("(c) Mezzas", 22, RED, WIDTH / 2, HEIGHT * 1 / 3)
        self.draw_text("Press a key to play", 18, RED, WIDTH / 2, HEIGHT * 4 / 5)
        self.draw_text("Floppy", 64, RED, WIDTH / 2, 15)
        pygame.display.flip()
        self.wait_for_key()"""

    def draw_text(self, text, size, color, x, y):
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        self.screen.blit(self.text_surface, self.text_rect)

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        while self.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0
            # self.show_start_screen()
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()


g = FloppyBird()
while g.running:
    g.run()

pygame.quit()
