import pygame
import random

pygame.init()

width = 240
height = 320

screen = pygame.display.set_mode((width, height))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

background = background.convert()

ballx, bally = int(width / 2), int(height / 2) # start position
radius = 25
ballColor = (255, 0, 0)
dx = 20 # will be used to change position of X
dy = 20

running = True
FPS = 30
clock = pygame.time.Clock()

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                if bally + radius + 1 > 0:
                    bally -= 10
            if event.key == pygame.K_DOWN:
                if bally + radius + 1 < height:
                    bally += 10
            if event.key == pygame.K_LEFT:
                if ballx + radius + 1 > 0:
                    ballx -= 10
            if event.key == pygame.K_RIGHT:
                if ballx + radius + 1 < width:
                    ballx += 10

    if ballx - radius < 0:
        ballx = radius
        dx *= -1 
    elif ballx + radius > width:
        ballx = width - radius
        dx *= -1
    if bally - radius - 1 < 0:
        bally = radius + 1
        dy *= -1
    elif bally + radius > height:
        bally = height - radius
        dy *= -1
        '''
    ballx = ballx + dx    
    bally = bally + dy
        '''
    screen.blit(background, (0, 0))

    pygame.draw.circle(screen, ballColor, (ballx, bally), radius)

    pygame.display.flip()

pygame.quit()