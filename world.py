from settings import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.player = pygame.Rect(270,180,50,50)
        self.player_colour = 'red'
        self.block_colour = 'blue'

        self.targets = []

    def draw_rects(self, y_axis):

        for _ in range(4):
            self.target_rect = pygame.Rect(150, y_axis, 50, 50)
            self.targets.append(self.target_rect)
            y_axis += 50

        #Draw rectangles
        for self.target_rect in self.targets:
            pygame.draw.rect(self.display_surface, self.block_colour, self.target_rect)


        

    def run(self):
        self.display_surface.fill('grey')

        pygame.draw.rect(self.display_surface, self.player_colour, self.player)
        #Collision

        if self.player.collidelist(self.targets) >= 0:
            self.player_colour = 'green'
        else:
            self.player_colour = 'red'


        #Draw Rectangles
        self.draw_rects(180)


        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            self.player.x -= 5
        if key[pygame.K_d] == True:
            self.player.x += 5
        if key[pygame.K_w] == True:
            self.player.y -= 5
        if key[pygame.K_s] == True:
            self.player.y += 5