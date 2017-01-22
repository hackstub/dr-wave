import sys
import src.shared as shared
import src.menuGraphics as menuGraphics
import src.scoreDisplay as scoreDisplay
import src.game as game

import pygame
from pygame.locals import *

class Menu() :

    def __init__(self) :

        # Set dimensions
        self.screen = pygame.display.set_mode(shared.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Doctor Wave")

        # Set up FPS clock
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        
        self.select, self.dy, self.menuanim = 1, 0, False

        self.click = pygame.mixer.Sound("assets/sounds/click.ogg")
        pygame.mixer.music.load("assets/music/menu.ogg")
        pygame.mixer.music.play(-1)
   
        self.scoreDisplay = scoreDisplay.ScoreDisplay()
        
    def mainLoop(self) :
        
        # Handle events
        self.eventHandler()
        
        # Update stuff
        shared.background.update()
        self.scoreDisplay.update()

        # Render stuff
        shared.game.screen.fill((0,0,0))
        shared.background.render()
        shared.menuGraphics.render(self.select, self.dy)
        self.scoreDisplay.render()
        
        if self.menuanim:
            self.dy += 8

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
                    sys.exit(0)

        if pygame.key.get_pressed()[pygame.K_RETURN] and self.select == 1:
            self.click.play()
            pygame.mixer.music.fadeout(1000)
            self.menuanim = True
        

    def getNextScene(self):
        if self.dy > 230:
            return "game"

