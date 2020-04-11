import pygame
import random

pygame.init()

class Game():

    def __init__(self, width, height, ball_surface_size, ball_radius, ball_x, ball_y, ball_dx, ball_dy, FPS):
        self.screen = pygame.display.set_mode((width, height))
        self.screenrect = self.screen.get_rect()
        self.background = pygame.Surface((width, height))
        self.background.fill((255, 255, 255))
        self.background = self.background.convert()
        self.background2 = self.background.copy()
        self.ballsurface = pygame.Surface(ball_surface_size)
        self.ballsurface.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.ballsurface, (0,0,255), (25,25), ball_radius)
        self.ballsurface = self.ballsurface.convert_alpha()
        self.ballrect = self.ballsurface.get_rect()
        self.ballx, self.bally = ball_x, ball_y
        self.dx, self.dy = ball_dx, ball_dy
        self.clock = pygame.time.Clock()
        self.mainloop = True
        self.FPS = FPS
        self.playtime = 0
        self.paint_big_circles = False
        self.cleanup = True
        

    def wildPainting(self):
        pygame.draw.circle(self.background, (random.randint(0,255),
                       random.randint(0,255), random.randint(0,255)),
                       (random.randint(0,self.screenrect.width),
                       random.randint(0,self.screenrect.height)),
                       random.randint(50,500))

    def run(self):    
        while self.mainloop:
            self.milliseconds = self.clock.tick(self.FPS) 
            self.seconds = self.milliseconds / 1000.0 
            self.playtime += self.seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mainloop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.mainloop = False

                    elif event.key == pygame.K_1: 
                        self.FPS = 5
                    elif event.key == pygame.K_2:
                        self.FPS = 20
                    elif event.key == pygame.K_3:
                        self.FPS = 30
                    elif event.key == pygame.K_4:
                        self.FPS = 40
                    elif event.key == pygame.K_5:
                        self.FPS = 50
                    elif event.key == pygame.K_6:
                        self.FPS = 60
                    elif event.key == pygame.K_7:
                        self.FPS = 70
                    elif event.key == pygame.K_8:
                        self.FPS = 80
                    elif event.key == pygame.K_9:
                        self.FPS = 90
                    elif event.key == pygame.K_0:
                        self.FPS = 1000
                    elif event.key == pygame.K_x:
                        self.paint_big_circles = not self.paint_big_circles
                    elif event.key == pygame.K_y:
                        self.cleanup = not self.cleanup
                    elif event.key == pygame.K_w:
                        self.background.blit(self.background2, (0,0))

            pygame.display.set_caption("x: paint ({}) y: cleanup ({}) ,"
                                       " w: white, 0-9: limit FPS to {}"
                                       " (now: {:.2f})".format(self.paint_big_circles, 
                                                               self.cleanup, 
                                                               self.FPS, 
                                                               self.clock.get_fps()
                                                               )
                                        )
            if self.cleanup:
                self.screen.blit(self.background, (0,0))
            if self.paint_big_circles:
                self.wildPainting()

            self.ballx += self.dx * self.seconds
            self.bally += self.dy * self.seconds 

            if self.ballx < 0:
                self.ballx = 0
                self.dx *= -1 
            elif self.ballx + self.ballrect.width > self.screenrect.width:
                self.ballx = self.screenrect.width - self.ballrect.width
                self.dx *= -1
            if self.bally < 0:
                self.bally = 0
                self.dy *= -1
            elif self.bally + self.ballrect.height > self.screenrect.height:
                self.bally = self.screenrect.height - self.ballrect.height
                self.dy *= -1
 
            self.screen.blit(self.ballsurface, (round(self.ballx,0), round(self.bally,0 )))
            pygame.display.flip()


game = Game(640,480, (50, 50), 25, 550, 240, 60, 50, 60)
game.run()