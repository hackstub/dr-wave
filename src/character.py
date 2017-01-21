
import pygame
from pygame.locals import *

import math
from enum import Enum

import sys

import src.shared as shared

class CharacterState(Enum) :
    SOLID = 0
    WAVE = 1
    TRANSFORMING_TO   = 2
    TRANSFORMING_BACK = 3
    DEAD = 4


class Character() :

    def __init__(self) :

        self.run = shared.assetsdb["characterrun"]
        self.run.setCooldown(1)
   
        self.transfo = shared.assetsdb["charactertransfo"]
        self.transfo.setCooldown(1)

        self.dead = shared.assetsdb["charactermort"]
        self.dead.setCooldown(4)

        self.pos = 0

        self.status = CharacterState.SOLID
    
        self.waveStateCD = shared.Cooldown(10, start=False)
        self.transformDisabledCD = shared.Cooldown(10, start=False)
        
        self.speedUp = shared.Cooldown(30)
        self.speedUpFactor = 1.0

        self.floor = 0
        
    def update(self) :

        self.waveStateCD.tick()
        self.transformDisabledCD.tick()
        self.speedUp.tick()
        
        if (self.status == CharacterState.SOLID) :
            self.run.tick()

        elif (self.status == CharacterState.TRANSFORMING_TO) :
            idBefore = self.transfo.currentId
            self.transfo.tick()
            idAfter = self.transfo.currentId
            if (idAfter < idBefore) :
                self.doneTransformingTo()

        elif (self.status == CharacterState.TRANSFORMING_BACK) :
            idBefore = self.transfo.currentId
            self.transfo.tick()
            idAfter = self.transfo.currentId
            if (idAfter > idBefore) :
                self.doneTransformingBack()

        elif (self.status == CharacterState.DEAD) :
            idBefore = self.dead.currentId
            self.dead.tick()
            idAfter = self.dead.currentId
            if (idAfter < idBefore) :
                print("Game over lol")
                sys.exit(-1)

        if (self.waveStateCD.justStopped()) :
            self.status = CharacterState.SOLID
            #self.waveStateCD = shared.Cooldown(int(15/self.speedUpFactor), start=False)
            
            self.status = CharacterState.TRANSFORMING_BACK
            self.transfo.setCurrentSprite(len(self.transfo.sprites) - 1)
            self.transfo.reverseLoop = True

        if (self.speedUp.justStopped()) :
            self.speedUp.restart()
            self.speedUpFactor += 0.01

        self.pos += self.speed()
        
        
    def speed(self) :

        if (self.status == CharacterState.SOLID) :
            return 10*self.speedUpFactor
        if (self.status == CharacterState.TRANSFORMING_TO) :
            return (10 + 40 * self.transfo.currentId/len(self.transfo.sprites))*self.speedUpFactor
        if (self.status == CharacterState.TRANSFORMING_BACK) :
            return (10 + 40 * self.transfo.currentId/len(self.transfo.sprites))*self.speedUpFactor
        if (self.status == CharacterState.WAVE) :
            return 50*self.speedUpFactor
        else :
            return 0

    def width(self) :
        
        sprite = self.run.getCurrentSprite()
        width, height = sprite.get_size()
        return width

    def collides(self) :

        return (self.status != CharacterState.WAVE)

    def die(self) :
        
        if (self.status == CharacterState.DEAD) :
            return

        self.status = CharacterState.DEAD
        
        self.dead.setCurrentSprite(0)


    def render(self) :

        if (self.status == CharacterState.WAVE) :
            return
        elif (self.status == CharacterState.TRANSFORMING_TO) :
            sprite = self.transfo.getCurrentSprite()
        elif (self.status == CharacterState.TRANSFORMING_BACK) :
            sprite = self.transfo.getCurrentSprite()
        elif (self.status == CharacterState.DEAD) :
            sprite = self.dead.getCurrentSprite()
        else :
            sprite = self.run.getCurrentSprite()
        
        width, height = sprite.get_size()

        shared.game.screen.blit(sprite, (shared.screenSize[0] / 2 - width/2,
                                         shared.screenSize[1] - 30 - self.floor * 200 - height))


    def doneTransformingTo(self) :

        self.status = CharacterState.WAVE
        self.waveStateCD.restart()

    def doneTransformingBack(self) :

        self.status = CharacterState.SOLID
        self.transformDisabledCD.restart()
         
    def handleTransformKey(self) :

        if ((self.status == self.status.WAVE)
        or (self.status == self.status.TRANSFORMING_TO)
        or (self.transformDisabledCD.active())) :
            return

        shared.game.screen.fill((0,0,0))
        self.status = CharacterState.TRANSFORMING_TO
        self.transfo.setCurrentSprite(0)
        self.transfo.reverseLoop = False

        if (pygame.key.get_pressed()[pygame.K_UP]) :
            self.floor += 1
        if (pygame.key.get_pressed()[pygame.K_DOWN]) :
            self.floor -= 1

        if (self.floor <  0) : self.floor = 0
        if (self.floor >= 1) : self.floor = 1



