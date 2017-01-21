import sys
import src.shared as shared

import pygame
from pygame.locals import *

class Game() :

    def __init__(self) :

        # Initialize PyGame
        pygame.init()

        # Set dimensions
        self.screen = pygame.display.set_mode(shared.screenSize, 0, 32)
        pygame.display.set_caption("Docteur Wavenstein")

        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
   
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

                # If F is pressed, do some stuff
                if (event.key == pygame.K_f) :
                    shared.character.handleTransformKey()




