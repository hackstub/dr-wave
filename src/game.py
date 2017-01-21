import sys
import src.shared as shared

import pygame
from pygame.locals import *

class Game() :

    def __init__(self) :

        # Set dimensions
        self.screen = pygame.display.set_mode(shared.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Doctor Wave")

        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()

        pygame.mixer.music.load("music/main.ogg")
        pygame.mixer.music.play(-1)

    def mainLoop(self) :

        # Handle events
        self.eventHandler()
        
        # Update stuff
        shared.character.update()
        shared.background.update()
        shared.obstacles.update()

        # Render stuff
        shared.background.render()
        shared.character.render()
        shared.obstacles.render()
            
        # Update screen
        pygame.display.update()
        self.fpsClock.tick(self.fps)
 
    def eventHandler(self) :

        for event in pygame.event.get():

            if (event.type == pygame.QUIT) :
                pygame.quit()
                sys.exit()
            
            if (event.type == pygame.KEYDOWN) :

                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()

                # If F is pressed, do some stuff
                if (event.key == pygame.K_f) :
                    shared.character.handleTransformKey()
    
    def getNextScene(self) :

        return None




