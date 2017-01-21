import sys
import src.shared as shared
import src.menuGraphics as menuGraphics
import src.game as game

import pygame
from pygame.locals import *

class Menu() :

    def __init__(self) :

        # Set dimensions
        self.screen = pygame.display.set_mode(shared.screenSize, 0, 32)
        pygame.display.set_caption("Docteur Wavenstein")

        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        
        self.select, self.dy, self.menuanim = 1, 0, False
   
    def mainLoop(self) :
        
        # Handle events
        self.eventHandler()
        
        # Update stuff
        shared.background.update()

        # Render stuff
        shared.game.screen.fill((0,0,0))
        shared.background.renderAt(1)
        shared.menuGraphics.render(self.select, self.dy)
        
        if self.menuanim:
            self.dy += 8
		
        if pygame.key.get_pressed()[pygame.K_RETURN] and self.select == 1: self.menuanim = True
        
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

                if (event.key == pygame.K_UP) :
                    self.select = 1
                
                if (event.key == pygame.K_DOWN) :
                    self.select = 2
                
                if (event.key == pygame.K_RETURN) and self.select == 2:
                    pygame.quit()

    def getNextScene(self):
        if self.dy > 200:
            return "game"

