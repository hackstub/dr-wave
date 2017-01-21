
import pygame
from pygame.locals import *

import math
from enum import Enum

import src.shared as shared

class CharacterState(Enum) :
    SOLID = 0
    WAVE = 1


class Character() :

    def __init__(self) :

        self.run = shared.assetsdb["characterrun"]
        self.run.setCooldown(1)

        self.pos = 0

        self.status = CharacterState.SOLID
    
        self.transformCD = shared.Cooldown(15, start=False)
        self.transformDisabledCD = shared.Cooldown(10, start=False)
        
        self.speedUp = shared.Cooldown(30)
        self.speedUpFactor = 1.0
        
        self.viseAngleCD = shared.Cooldown(5)
        self.viseAngle = 0

    def update(self) :

        self.run.tick()
        self.transformCD.tick()
        self.transformDisabledCD.tick()
        self.speedUp.tick()

        if (self.transformCD.justStopped()) :
            self.status = CharacterState.SOLID
            #self.transformCD = shared.Cooldown(int(15/self.speedUpFactor), start=False)
            self.transformDisabledCD.restart()

        if (self.speedUp.justStopped()) :
            self.speedUp.restart()
            self.speedUpFactor += 0.01

        self.pos += self.speed()
        
        
        
        
        self.viseAngleCD.tick()
        if (self.viseAngleCD.justStopped()) :
            self.viseAngleCD.restart()
            self.viseAngle += 10


    def speed(self) :

        if (self.status == CharacterState.SOLID) :
            return 10*self.speedUpFactor
        if (self.status == CharacterState.WAVE) :
            return 30*self.speedUpFactor

    def width(self) :
        
        sprite = self.run.getCurrentSprite()
        width, height = sprite.get_size()
        return width

    def collides(self) :

        return (self.status == CharacterState.SOLID)

    def render(self) :

        if (self.status == CharacterState.WAVE) :
            return

        sprite = self.run.getCurrentSprite()
        width, height = sprite.get_size()

        shared.game.screen.blit(sprite, (shared.screenSize[0] / 2 - width /
            2,400))


        #viseX = (width/2 + 30) * math.cos(self.viseAngle * 3.141592653 / 180)
        #viseY = (width/2 + 30) * math.sin(self.viseAngle * 3.141592653 / 180)
        #pygame.draw.circle(shared.game.screen, (200,200,200),
        #        (int(shared.screenSize[0] / 2 - width/2 + viseX), int(500 - viseY)), 4)

    def handleTransformKey(self) :

        if (self.status == self.status.WAVE) :
            return
        
        if (self.transformDisabledCD.active()) :
            return

        shared.game.screen.fill((0,0,0))
        self.status = CharacterState.WAVE        
        self.transformCD.restart()



