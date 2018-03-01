# Pygame template - skeleton for a new pygame project
import pygame
import random
import time
from settings import *


class FloppyBird():
    # initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.all_sprites = pygame.sprite.Group()
        # Game loop
        self.running = True
        while self.running:
            # keep loop running at the right speed
            self.clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.all_sprites.update()
            # Draw / render
            self.screen.fill(BLUE)
            self.all_sprites.draw(screen)

            # *after* drawing everything, flip the display
            pygame.display.flip()


pygame.quit()
