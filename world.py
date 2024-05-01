from settings import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.player = pygame.Rect(270,180,50,50)
        self.player_colour = 'red'
        self.block_colour = 'blue'

        self.targets = []

        self.move_y = 5
        self.move_x = 5



    def draw_rects(self, y_axis): #Rects that the player collides with

        for _ in range(1):
            self.target_rect = pygame.Rect(150, y_axis, 50, 50)
            self.targets.append(self.target_rect)
            y_axis += 50

        #Draw rectangles
        for self.target_rect in self.targets:
            pygame.draw.rect(self.display_surface, self.block_colour, self.target_rect)

    def collision(self):
        
        for self.target_rect in self.targets:
            #X collision Right
            if self.targets.collidelist(self.player.x + self.move_x, self.player.y , 50,50) >= 0:
                self.player.x -= 1 
            #X collision left
            if self.targets.collidelist(self.player.x - self.move_x, self.player.y , 50,50) >= 0:
                self.player.x += 1

            #Y collision Bottom
            if self.targets.collidelist(self.player.x, self.player.y + self.move_y, 50,50) >= 0:
                self.player.y -= 1

            #Y collision Top
            if self.targets.collidelist(self.player.x, self.player.y - self.move_y, 50,50) >= 0:
                self.player.y += 1

                

        

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
            self.player.x -= self.move_x
        if key[pygame.K_d] == True:
            self.player.x += self.move_x
        if key[pygame.K_w] == True:
            self.player.y -= self.move_y
        if key[pygame.K_s] == True:
            self.player.y += self.move_y

        self.collision()