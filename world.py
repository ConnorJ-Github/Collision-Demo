from settings import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.player = pygame.Rect(270,180,50,50)

    def run(self):
        self.display_surface.fill('grey')

        pygame.draw.rect(self.display_surface, 'red', self.player)

        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            self.player.x -= 5
        if key[pygame.K_d] == True:
            self.player.x += 5
        if key[pygame.K_w] == True:
            self.player.y -= 5
        if key[pygame.K_s] == True:
            self.player.y += 5