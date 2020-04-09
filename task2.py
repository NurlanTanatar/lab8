import pygame
class Body(object):
    def __init__(self, FPS=60 , width=640, height=480):
        pygame.init()
        self.width=width
        self.height=height
        self.FPS=FPS
        print(FPS)#####################################
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        self.background.convert()


        self.ballsurface = pygame.Surface((50,50))
        self.ballsurface.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.ballsurface, (255,0,0), (25,25), 25)
        self.ballsurface.convert_alpha()


        self.FPS=60
        self.gametime=0.0
        self.clock = pygame.time.Clock()
        self.dx, self.dy = 228, 0
        self.x , self.y = 0, 0
        self.cleanup = True

    def run(self, ball):
        running = True
        while (running == True):
            milliseconds = self.clock.tick(self.FPS)
            seconds = milliseconds / 1000.0
            self.gametime = self.gametime + seconds
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        running = False
                    elif (event.key == pygame.K_0):
                        self.FPS = 1
                    elif (event.key == pygame.K_1):
                        self.FPS = 10
                    elif (event.key == pygame.K_2):
                        self.FPS = 20
                    elif (event.key == pygame.K_3):
                        self.FPS = 30
                    elif (event.key == pygame.K_4):
                        self.FPS = 40
                    elif (event.key == pygame.K_5):
                        self.FPS = 50
                    elif (event.key == pygame.K_6):
                        self.FPS = 60
                    elif (event.key == pygame.K_7):
                        self.FPS = 70
                    elif (event.key == pygame.K_8):
                        self.FPS = 80
                    elif (event.key == pygame.K_9):
                        self.FPS = 90
                    elif (event.key == pygame.K_DOWN):
                        self.dx = 0
                        self.dy = 228
                    elif (event.key == pygame.K_UP):
                        self.dx = 0
                        self.dy = -228
                    elif (event.key == pygame.K_RIGHT):
                        self.dx = 228
                        self.dy = 0
                    elif (event.key == pygame.K_LEFT):
                        self.dx = -228
                        self.dy = 0
                    elif (event.key == pygame.K_y):
                        self.cleanup = not self.cleanup
            
            pygame.display.set_caption("0-9: limit FPS to {}"
                            " (now): {:.2f}".format(self.FPS, self.clock.get_fps()))
            if self.cleanup:
                self.screen.blit(self.background, (0, 0))


            if (ball.checking_x( ball.x, ball.dx) == True):
                ball.dx = ball.dx * (-1)
                self.dx = ball.dx
            elif (ball.checking_y(ball.y, ball.dy) == True):
                ball.dy = ball.dy * (-1)
                self.dy = self.dy


            self.x = self.x + self.dx * seconds
            self.y = self.y + self.dy * seconds

            self.screen.blit(self.ballsurface, ( round (self.x, 0), round (self.y,0)))
            pygame.display.flip()
            
        pygame.quit()






class Ball:
    def __init__(self, x, y, radius, dx, dy, color):
        self.x=x
        self.y=y
        self.color=color
        self.dx=dx
        self.dy=dy
        self.radius=radius
    def checking_x(self, x, dx):
        if ( (x + 50 > 640 and dx == 228) or (x < 0 and dx == -228) ):
            return (True)
        else:
            return (False)
    def checking_y(self, y, dy):
        if ( (y + 50 > 480 and dy == 228) or (y < 0 and dy == -228)):
            return (True)
        else:
            return (False)


# def motion(ball, FPS, circuit):

    # def movement():
    #     if (ball.checking_x( ball.x, ball.dx) == True):
    #         ball.dx = ball.dx * (-1)
            
    #     elif (ball.checking_y(ball.y, ball.dy) == True):
    #         ball.dy = ball.dy * (-1)

        # ball.x = ball.x + ball.dx * seconds

        # ball.draw(circuit)

    # return movement()    

def main(FPS):
    circuit = Body(FPS)

    # x, y, radius, dx, dy, color
    
    ball = Ball(0, 0, 25, 228, 0, (255, 0, 0))

    # loopfunc = motion(ball, FPS, circuit)

    circuit.run(ball)




if __name__ == '__main__':

    main(70)
