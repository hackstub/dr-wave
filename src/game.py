import sys
import src.shared as shared
import src.timer as timer

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
        
        self.clock = timer.Timer()

        self.music = pygame.mixer.Sound("assets/music/main.ogg")
        self.music.play(-1)

        self.runnerSound = pygame.mixer.Sound("assets/sounds/runner.ogg")
        self.runStartSound = pygame.mixer.Sound("assets/sounds/run-start.ogg")
        self.runnerSound1 = pygame.mixer.Sound("assets/sounds/runner-1.ogg")

        self.runStartSound.play()
        self.runnerSound.play(-1)
        self.runnerSound1.play(-1)
        
        shared.score = 0
        shared.over = False

    def mainLoop(self) :

        # Handle events
        self.eventHandler()

        # Update stuff
        shared.character.update()
        shared.background.update()
        shared.obstacles.update()
        self.clock.update()

        # Render stuff
        shared.background.render()
        shared.character.render()
        shared.obstacles.render()
        self.clock.render()

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
                    shared.character.morphCharge()

            if (event.type == pygame.KEYUP) :

                # If F is pressed, do some stuff
                if (event.key == pygame.K_f) :
                    shared.character.morphStart()

    def getNextScene(self) :
        if shared.over:
            self.music.stop()
            self.runnerSound.stop()
            self.runStartSound.stop()
            self.music.stop()
            shared.character.reset()
            return "menu"
        else: return None




