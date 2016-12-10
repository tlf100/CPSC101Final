import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 40 # frames per second setting
fpsClock = pygame.time.Clock()

# window
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Wife\'s Complaint')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def Title():
    fontObj = pygame.font.Font('Moon Light.otf', 32)
    textSurfaceObj = fontObj.render('The Wife\'s Complaint', True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()


